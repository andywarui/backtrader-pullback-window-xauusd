"""
+==============================================================================+
|                    MT5 TRADING INTERFACE MODULE                              |
|           MetaTrader 5 Live Trading Integration                              |
|                   For XAUUSD Trading Bot                                     |
+==============================================================================+

This module handles all MetaTrader 5 platform interactions:
- Connection and authentication
- Live price data retrieval
- Order execution (market, stop loss, take profit)
- Position monitoring and management
- Trade notifications and logging
"""

import MetaTrader5 as mt5
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time
import json
from pathlib import Path
from typing import Optional, Dict, List, Tuple


class MT5Trader:
    """MetaTrader 5 Trading Interface"""
    
    def __init__(self, config_path: str = "mt5_config.json"):
        """Initialize MT5 trader with configuration"""
        self.config_path = Path(config_path)
        self.config = self._load_config()
        self.connected = False
        self.symbol = self.config.get('symbol', 'XAUUSD')
        self.magic_number = self.config.get('magic_number', 234567)
        self.timeframe = self._parse_timeframe(self.config.get('timeframe', 'M1'))

        # Risk management
        self.max_risk_per_trade = self.config['risk_settings']['max_risk_per_trade']
        self.max_daily_trades = self.config['risk_settings']['max_daily_trades']
        self.max_open_positions = self.config['risk_settings']['max_open_positions']

        # Prop firm safety features
        self.max_daily_loss_percent = self.config['risk_settings'].get('max_daily_loss_percent', 0.05)
        self.max_overall_loss_percent = self.config['risk_settings'].get('max_overall_loss_percent', 0.10)
        self.emergency_stop_percent = self.config['risk_settings'].get('emergency_stop_at_percent', 0.045)

        # Advanced settings
        self.use_breakeven_trailing = self.config['advanced'].get('use_breakeven_trailing', True)
        self.breakeven_trigger_percent = self.config['advanced'].get('breakeven_trigger_percent', 0.50)
        self.min_stop_distance = self.config['advanced'].get('min_stop_distance_points', 20)

        # Trading statistics
        self.daily_trades_count = 0
        self.last_trade_date = None
        self.daily_start_balance = None
        self.initial_balance = None
        self.trading_halted = False
        self.halt_reason = None

        # Trade history for rational martingale
        self.trade_history = []  # List of recent trade results (True=win, False=loss)
        
    def _load_config(self) -> dict:
        """Load MT5 configuration from JSON file"""
        if not self.config_path.exists():
            raise FileNotFoundError(
                f"[ERROR] MT5 config not found: {self.config_path}\n"
                "Please create mt5_config.json with your broker credentials."
            )
        
        with open(self.config_path, 'r') as f:
            config = json.load(f)
        
        # Validate required fields
        required = ['account', 'password', 'server', 'symbol']
        missing = [field for field in required if field not in config]
        if missing:
            raise ValueError(f"Missing required config fields: {missing}")
        
        return config
    
    def _parse_timeframe(self, tf_str: str) -> int:
        """Convert timeframe string to MT5 constant"""
        timeframes = {
            'M1': mt5.TIMEFRAME_M1,
            'M5': mt5.TIMEFRAME_M5,
            'M15': mt5.TIMEFRAME_M15,
            'M30': mt5.TIMEFRAME_M30,
            'H1': mt5.TIMEFRAME_H1,
            'H4': mt5.TIMEFRAME_H4,
            'D1': mt5.TIMEFRAME_D1,
        }
        return timeframes.get(tf_str.upper(), mt5.TIMEFRAME_M1)
    
    def connect(self) -> bool:
        """Connect to MT5 terminal and login"""
        print("\n[CONNECT] Connecting to MetaTrader 5...")
        
        # Initialize MT5
        if not mt5.initialize():
            print(f"[ERROR] MT5 initialization failed: {mt5.last_error()}")
            return False
        
        # Get MT5 version
        version = mt5.version()
        print(f"[OK] MT5 Version: {version}")
        
        # Login to account
        account = self.config['account']
        password = self.config['password']
        server = self.config['server']
        
        authorized = mt5.login(account, password=password, server=server)
        
        if authorized:
            account_info = mt5.account_info()
            if account_info is not None:
                self.connected = True

                # Initialize balance tracking for prop firm rules
                if self.initial_balance is None:
                    self.initial_balance = account_info.balance
                if self.daily_start_balance is None:
                    self.daily_start_balance = account_info.balance

                print(f"[OK] Connected to MT5")
                print(f"   Account: {account}")
                print(f"   Server: {server}")
                print(f"   Balance: ${account_info.balance:,.2f}")
                print(f"   Equity: ${account_info.equity:,.2f}")
                print(f"   Leverage: 1:{account_info.leverage}")

                # Display prop firm limits
                max_daily_loss = self.initial_balance * self.max_daily_loss_percent
                max_overall_loss = self.initial_balance * self.max_overall_loss_percent
                emergency_threshold = self.initial_balance * self.emergency_stop_percent

                print(f"\n[SHIELD]  PROP FIRM SAFETY LIMITS:")
                print(f"   Max Daily Loss: ${max_daily_loss:,.2f} ({self.max_daily_loss_percent*100}%)")
                print(f"   Max Overall Loss: ${max_overall_loss:,.2f} ({self.max_overall_loss_percent*100}%)")
                print(f"   Emergency Stop: ${emergency_threshold:,.2f} ({self.emergency_stop_percent*100}%)")
                print(f"   Max Open Positions: {self.max_open_positions}")
                print(f"   Risk Per Trade: {self.max_risk_per_trade*100}%")

                # Check symbol availability
                if not self._check_symbol():
                    return False

                return True
        
        print(f"[ERROR] Login failed: {mt5.last_error()}")
        return False
    
    def _check_symbol(self) -> bool:
        """Verify symbol is available and enabled"""
        symbol_info = mt5.symbol_info(self.symbol)
        
        if symbol_info is None:
            print(f"[ERROR] Symbol {self.symbol} not found")
            return False
        
        if not symbol_info.visible:
            print(f"[WARNING]  Symbol {self.symbol} not visible, trying to enable...")
            if not mt5.symbol_select(self.symbol, True):
                print(f"[ERROR] Failed to enable {self.symbol}")
                return False
        
        print(f"[OK] Symbol {self.symbol} ready")
        print(f"   Bid: {symbol_info.bid}")
        print(f"   Ask: {symbol_info.ask}")
        print(f"   Spread: {symbol_info.spread} points")
        print(f"   Min Lot: {symbol_info.volume_min} | Max Lot: {symbol_info.volume_max} | Step: {symbol_info.volume_step}")
        
        return True
    
    def disconnect(self):
        """Disconnect from MT5"""
        if self.connected:
            mt5.shutdown()
            self.connected = False
            print("[CONNECT] Disconnected from MT5")
    
    def get_account_info(self) -> Optional[Dict]:
        """Get current account information"""
        if not self.connected:
            return None
        
        account_info = mt5.account_info()
        if account_info is None:
            return None
        
        return {
            'balance': account_info.balance,
            'equity': account_info.equity,
            'profit': account_info.profit,
            'margin': account_info.margin,
            'margin_free': account_info.margin_free,
            'margin_level': account_info.margin_level,
            'leverage': account_info.leverage,
        }
    
    def get_current_price(self) -> Optional[Tuple[float, float]]:
        """Get current bid and ask prices"""
        tick = mt5.symbol_info_tick(self.symbol)
        if tick is None:
            return None
        return (tick.bid, tick.ask)
    
    def get_historical_data(self, bars: int = 500) -> Optional[pd.DataFrame]:
        """Fetch historical price data"""
        if not self.connected:
            print("[ERROR] Not connected to MT5")
            return None
        
        rates = mt5.copy_rates_from_pos(self.symbol, self.timeframe, 0, bars)
        
        if rates is None or len(rates) == 0:
            print(f"[ERROR] Failed to get historical data: {mt5.last_error()}")
            return None
        
        # Convert to DataFrame
        df = pd.DataFrame(rates)
        df['time'] = pd.to_datetime(df['time'], unit='s')
        
        return df
    
    def calculate_position_size(self,
                               entry_price: float,
                               stop_loss: float,
                               risk_amount: Optional[float] = None) -> float:
        """Calculate position size - FIXED at 0.1 lots for standard trading"""
        # FIXED LOT SIZE: 0.1 standard lots
        fixed_lots = 0.10
        
        print(f"[STATS] Position Sizing: FIXED at {fixed_lots} lots")
        
        return fixed_lots
    
    def open_position(self, 
                     order_type: str,
                     volume: float,
                     stop_loss: Optional[float] = None,
                     take_profit: Optional[float] = None,
                     comment: str = "") -> Optional[Dict]:
        """
        Open a new position
        
        Args:
            order_type: 'BUY' or 'SELL'
            volume: Lot size
            stop_loss: Stop loss price
            take_profit: Take profit price
            comment: Order comment
        """
        if not self.connected:
            print("[ERROR] Not connected to MT5")
            return None
        
        # Check daily trade limit
        if not self._check_trade_limits():
            print("[WARNING]  Daily trade limit reached")
            return None
        
        # Get current price
        symbol_info = mt5.symbol_info(self.symbol)
        if symbol_info is None:
            print(f"[ERROR] Failed to get symbol info")
            return None
        
        # Determine order type and price
        if order_type.upper() == 'BUY':
            trade_type = mt5.ORDER_TYPE_BUY
            price = symbol_info.ask
        elif order_type.upper() == 'SELL':
            trade_type = mt5.ORDER_TYPE_SELL
            price = symbol_info.bid
        else:
            print(f"[ERROR] Invalid order type: {order_type}")
            return None
        
        # Normalize prices
        point = symbol_info.point
        digits = symbol_info.digits
        
        if stop_loss:
            stop_loss = round(stop_loss, digits)
        if take_profit:
            take_profit = round(take_profit, digits)
        
        # Prepare request
        deviation = self.config['advanced'].get('deviation', 10)
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": self.symbol,
            "volume": volume,
            "type": trade_type,
            "price": price,
            "deviation": deviation,
            "magic": self.magic_number,
            "comment": comment or self.config['advanced'].get('comment', 'XAUUSD_Bot'),
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_FOK,
        }
        
        if stop_loss:
            request["sl"] = stop_loss
        if take_profit:
            request["tp"] = take_profit
        
        # Send order
        result = mt5.order_send(request)
        
        if result is None:
            print(f"[ERROR] Order send failed: {mt5.last_error()}")
            return None
        
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print(f"[ERROR] Order failed: {result.retcode} - {result.comment}")
            return None
        
        # Update trade counter
        self._update_trade_counter()
        
        print(f"\n[OK] {order_type} ORDER EXECUTED")
        print(f"   Ticket: {result.order}")
        print(f"   Volume: {volume} lots")
        print(f"   Price: {result.price}")
        if stop_loss:
            print(f"   Stop Loss: {stop_loss}")
        if take_profit:
            print(f"   Take Profit: {take_profit}")
        print(f"   Comment: {comment}")
        
        return {
            'ticket': result.order,
            'type': order_type,
            'volume': volume,
            'price': result.price,
            'sl': stop_loss,
            'tp': take_profit,
            'time': datetime.now(),
        }
    
    def close_position(self, ticket: int) -> bool:
        """Close an open position by ticket"""
        if not self.connected:
            return False
        
        # Get position info
        position = mt5.positions_get(ticket=ticket)
        if not position or len(position) == 0:
            print(f"[ERROR] Position {ticket} not found")
            return False
        
        position = position[0]
        
        # Determine close order type
        if position.type == mt5.ORDER_TYPE_BUY:
            trade_type = mt5.ORDER_TYPE_SELL
            price = mt5.symbol_info_tick(self.symbol).bid
        else:
            trade_type = mt5.ORDER_TYPE_BUY
            price = mt5.symbol_info_tick(self.symbol).ask
        
        # Close request
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": self.symbol,
            "volume": position.volume,
            "type": trade_type,
            "position": ticket,
            "price": price,
            "deviation": 10,
            "magic": self.magic_number,
            "comment": "Close by bot",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_FOK,
        }
        
        result = mt5.order_send(request)
        
        if result is None or result.retcode != mt5.TRADE_RETCODE_DONE:
            print(f"[ERROR] Failed to close position: {result.comment if result else mt5.last_error()}")
            return False
        
        print(f"[OK] Position {ticket} closed")
        return True
    
    def get_open_positions(self) -> List[Dict]:
        """Get all open positions for this symbol"""
        if not self.connected:
            return []
        
        positions = mt5.positions_get(symbol=self.symbol)
        if positions is None or len(positions) == 0:
            return []
        
        result = []
        for pos in positions:
            result.append({
                'ticket': pos.ticket,
                'type': 'BUY' if pos.type == mt5.ORDER_TYPE_BUY else 'SELL',
                'volume': pos.volume,
                'price_open': pos.price_open,
                'price_current': pos.price_current,
                'sl': pos.sl,
                'tp': pos.tp,
                'profit': pos.profit,
                'time': datetime.fromtimestamp(pos.time),
            })
        
        return result
    
    def modify_position(self, ticket: int, 
                       stop_loss: Optional[float] = None,
                       take_profit: Optional[float] = None) -> bool:
        """Modify stop loss and/or take profit of existing position"""
        if not self.connected:
            return False
        
        # Get position
        position = mt5.positions_get(ticket=ticket)
        if not position or len(position) == 0:
            print(f"[ERROR] Position {ticket} not found")
            return False
        
        position = position[0]
        
        # Use existing values if not provided
        if stop_loss is None:
            stop_loss = position.sl
        if take_profit is None:
            take_profit = position.tp
        
        # Normalize prices
        symbol_info = mt5.symbol_info(self.symbol)
        digits = symbol_info.digits
        stop_loss = round(stop_loss, digits) if stop_loss else 0
        take_profit = round(take_profit, digits) if take_profit else 0
        
        # Modify request
        request = {
            "action": mt5.TRADE_ACTION_SLTP,
            "symbol": self.symbol,
            "position": ticket,
            "sl": stop_loss,
            "tp": take_profit,
        }
        
        result = mt5.order_send(request)
        
        if result is None or result.retcode != mt5.TRADE_RETCODE_DONE:
            print(f"[ERROR] Failed to modify position: {result.comment if result else mt5.last_error()}")
            return False
        
        print(f"[OK] Position {ticket} modified (SL: {stop_loss}, TP: {take_profit})")
        return True

    def monitor_breakeven_trailing(self):
        """Monitor open positions and move SL to break-even when profit reaches trigger level"""
        if not self.use_breakeven_trailing:
            return

        if not self.connected:
            return

        positions = self.get_open_positions()

        for pos in positions:
            ticket = pos['ticket']
            entry_price = pos['price_open']
            current_price = pos['price_current']
            tp_price = pos['tp']
            sl_price = pos['sl']
            position_type = pos['type']

            # Skip if no TP set
            if tp_price == 0:
                continue

            # Calculate distance to TP
            if position_type == 'BUY':
                distance_to_tp = tp_price - entry_price
                current_profit_distance = current_price - entry_price
            else:  # SELL
                distance_to_tp = entry_price - tp_price
                current_profit_distance = entry_price - current_price

            # Skip if already at break-even or better
            if position_type == 'BUY':
                if sl_price >= entry_price:
                    continue  # Already moved to BE or better
            else:  # SELL
                if sl_price <= entry_price and sl_price > 0:
                    continue  # Already moved to BE or better

            # Check if we've reached the trigger percentage
            if distance_to_tp > 0:
                profit_percentage = current_profit_distance / distance_to_tp

                if profit_percentage >= self.breakeven_trigger_percent:
                    # Move SL to break-even (entry price)
                    print(f"\n[TARGET] Break-Even Trigger Reached!")
                    print(f"   Ticket: {ticket}")
                    print(f"   Type: {position_type}")
                    print(f"   Entry: {entry_price}")
                    print(f"   Current: {current_price}")
                    print(f"   Progress: {profit_percentage*100:.1f}% to TP")
                    print(f"   Moving SL to break-even: {entry_price}")

                    # Move stop loss to entry price (break-even)
                    success = self.modify_position(
                        ticket=ticket,
                        stop_loss=entry_price,
                        take_profit=tp_price  # Keep existing TP
                    )

                    if success:
                        print(f"[OK] Stop loss moved to break-even! Risk eliminated.")
                    else:
                        print(f"[WARNING] Failed to move SL to break-even")

    def _check_trade_limits(self) -> bool:
        """Check if trading limits are within bounds"""
        # Check if trading has been halted
        if self.trading_halted:
            print(f"[ALERT] TRADING HALTED: {self.halt_reason}")
            return False

        # Reset counter if new day
        today = datetime.now().date()
        if self.last_trade_date != today:
            self.daily_trades_count = 0
            self.last_trade_date = today
            # Reset daily start balance
            account_info = self.get_account_info()
            if account_info:
                self.daily_start_balance = account_info['balance']
                print(f"[DATE] New trading day - Daily start balance: ${self.daily_start_balance:,.2f}")

        # Check prop firm safety limits
        if not self._check_prop_firm_limits():
            return False

        # Daily trade limit removed - unlimited trades allowed
        # if self.daily_trades_count >= self.max_daily_trades:
        #     print(f"[WARNING]  Daily trade limit reached ({self.daily_trades_count}/{self.max_daily_trades})")
        #     return False

        # Check max open positions
        open_positions = len(self.get_open_positions())
        if open_positions >= self.max_open_positions:
            print(f"[WARNING]  Max open positions ({self.max_open_positions}) reached")
            return False

        return True
    
    def _check_prop_firm_limits(self) -> bool:
        """Check prop firm daily loss and overall drawdown limits"""
        account_info = self.get_account_info()
        if not account_info:
            return True  # Can't check, allow trade

        current_balance = account_info['balance']

        # Check daily loss limit
        if self.daily_start_balance is not None:
            daily_loss = self.daily_start_balance - current_balance
            daily_loss_percent = daily_loss / self.initial_balance if self.initial_balance else 0

            if daily_loss_percent >= self.emergency_stop_percent:
                self.trading_halted = True
                self.halt_reason = f"Daily loss limit reached: ${daily_loss:,.2f} ({daily_loss_percent*100:.2f}%)"
                print(f"\n[ALERT] EMERGENCY STOP TRIGGERED! [ALERT]")
                print(f"   {self.halt_reason}")
                print(f"   All positions will be closed. Trading halted for today.")
                # Close all positions
                self._emergency_close_all_positions()
                return False

            # Warning at 75% of daily limit
            if daily_loss_percent >= (self.emergency_stop_percent * 0.75):
                print(f"[WARNING]  WARNING: Daily loss at {daily_loss_percent*100:.2f}% - Approaching limit!")

        # Check overall drawdown limit
        if self.initial_balance is not None:
            overall_loss = self.initial_balance - current_balance
            overall_loss_percent = overall_loss / self.initial_balance

            if overall_loss_percent >= (self.max_overall_loss_percent * 0.95):
                self.trading_halted = True
                self.halt_reason = f"Overall drawdown limit reached: ${overall_loss:,.2f} ({overall_loss_percent*100:.2f}%)"
                print(f"\n[ALERT] CRITICAL: Overall Drawdown Limit! [ALERT]")
                print(f"   {self.halt_reason}")
                print(f"   All positions will be closed. Trading permanently halted.")
                self._emergency_close_all_positions()
                return False

            # Warning at 80% of overall limit
            if overall_loss_percent >= (self.max_overall_loss_percent * 0.80):
                print(f"[WARNING]  CAUTION: Overall drawdown at {overall_loss_percent*100:.2f}% - Approaching max limit!")

        return True

    def _emergency_close_all_positions(self):
        """Close all open positions immediately"""
        positions = self.get_open_positions()
        if positions:
            print(f"[ALERT] Closing {len(positions)} open position(s)...")
            for pos in positions:
                self.close_position(pos['ticket'])

    def _update_trade_counter(self):
        """Update daily trade counter"""
        today = datetime.now().date()
        if self.last_trade_date != today:
            self.daily_trades_count = 0
            self.last_trade_date = today

        self.daily_trades_count += 1

    def _record_trade_result(self, is_win: bool):
        """Record trade result for position sizing logic"""
        self.trade_history.append(is_win)
        # Keep only last 10 trades
        if len(self.trade_history) > 10:
            self.trade_history.pop(0)

    def _get_consecutive_wins(self) -> int:
        """Count consecutive wins from most recent trades"""
        consecutive = 0
        for result in reversed(self.trade_history):
            if result:  # Win
                consecutive += 1
            else:
                break
        return consecutive

    def _get_consecutive_losses(self) -> int:
        """Count consecutive losses from most recent trades"""
        consecutive = 0
        for result in reversed(self.trade_history):
            if not result:  # Loss
                consecutive += 1
            else:
                break
        return consecutive

    def get_trading_status(self) -> Dict:
        """Get current trading status summary"""
        account_info = self.get_account_info()
        open_positions = self.get_open_positions()
        
        return {
            'connected': self.connected,
            'account': account_info,
            'open_positions': len(open_positions),
            'daily_trades': self.daily_trades_count,
            'positions': open_positions,
        }


# ===============================================================================
# HELPER FUNCTIONS
# ===============================================================================

def test_mt5_connection(config_path: str = "mt5_config.json"):
    """Test MT5 connection and display account info"""
    trader = MT5Trader(config_path)
    
    if trader.connect():
        print("\n" + "="*60)
        print("[STATS] MT5 CONNECTION TEST SUCCESSFUL")
        print("="*60)
        
        # Get account info
        account = trader.get_account_info()
        if account:
            print(f"\n[ACCOUNT] Account Information:")
            print(f"   Balance: ${account['balance']:,.2f}")
            print(f"   Equity: ${account['equity']:,.2f}")
            print(f"   Profit: ${account['profit']:+,.2f}")
            print(f"   Margin: ${account['margin']:,.2f}")
            print(f"   Free Margin: ${account['margin_free']:,.2f}")
            if account['margin'] > 0:
                print(f"   Margin Level: {account['margin_level']:.2f}%")
        
        # Get current price
        price = trader.get_current_price()
        if price:
            bid, ask = price
            spread = ask - bid
            print(f"\n[MONEY] {trader.symbol} Price:")
            print(f"   Bid: {bid}")
            print(f"   Ask: {ask}")
            print(f"   Spread: {spread:.5f}")
        
        # Get open positions
        positions = trader.get_open_positions()
        print(f"\n[UP] Open Positions: {len(positions)}")
        for pos in positions:
            print(f"   Ticket {pos['ticket']}: {pos['type']} {pos['volume']} lots @ {pos['price_open']} | P&L: ${pos['profit']:+.2f}")
        
        print("\n" + "="*60)
        
        trader.disconnect()
        return True
    else:
        print("\n[ERROR] MT5 connection test failed")
        return False


if __name__ == '__main__':
    # Test MT5 connection
    test_mt5_connection()
