# 🤖 XAUUSD Trading Bot - MT5 Integration Guide

## 📋 Overview

This bot now supports **live trading on MetaTrader 5** platform in addition to backtesting.

## 🚀 Quick Start

### 1. Install MT5 Package

```powershell
.\venv\Scripts\Activate.ps1
pip install MetaTrader5 pandas
```

### 2. Configure MT5 Credentials

Edit `mt5_config.json` with your broker details:

```json
{
  "account": 12345678,
  "password": "your_password",
  "server": "YourBroker-Demo",
  "symbol": "XAUUSD",
  "timeframe": "M1",
  "magic_number": 234567
}
```

### 3. Test MT5 Connection

```powershell
python mt5_trader.py
```

This will test your MT5 connection and display account info.

### 4. Run Live Trading

```powershell
# MT5 Live Trading (⚠️ REAL TRADES!)
python xauusd_trading_bot.py --mode mt5

# Backtest Mode (Safe Testing)
python xauusd_trading_bot.py --mode backtest

# Quick 30-day Test
python xauusd_trading_bot.py --mode quick
```

## ⚙️ Configuration

### MT5 Settings (`mt5_config.json`)

| Parameter | Description | Example |
|-----------|-------------|---------|
| `account` | MT5 account number | 12345678 |
| `password` | MT5 password | "MyPass123" |
| `server` | Broker server name | "XM-Demo" |
| `symbol` | Trading symbol | "XAUUSD" |
| `timeframe` | Chart timeframe | "M1" or "M5" |
| `magic_number` | Unique bot identifier | 234567 |

### Risk Settings

| Parameter | Description | Default |
|-----------|-------------|---------|
| `max_risk_per_trade` | Risk per trade (%) | 0.01 (1%) |
| `max_daily_trades` | Maximum trades per day | 20 |
| `max_open_positions` | Maximum simultaneous positions | 3 |

## 📊 MT5 Live Trading Features

✅ **Automatic Connection** - Connects to MT5 on startup
✅ **Live Price Data** - Fetches real-time market data
✅ **Signal Detection** - Monitors for EMA crossovers and ATR conditions
✅ **Auto Position Sizing** - Calculates lot size based on risk %
✅ **Stop Loss & Take Profit** - Automatic SL/TP placement
✅ **Position Monitoring** - Tracks open positions and P&L
✅ **Daily Trade Limits** - Prevents over-trading
✅ **Safe Shutdown** - Graceful exit with Ctrl+C

## 🔄 Trading Workflow

1. **Connect** - Bot connects to MT5 terminal
2. **Monitor** - Fetches historical data for indicators
3. **Analyze** - Calculates EMAs and ATR
4. **Signal** - Detects crossovers and entry conditions
5. **Execute** - Opens position with SL/TP
6. **Track** - Monitors open positions
7. **Repeat** - Checks every 60 seconds (configurable)

## 🛡️ Safety Features

### Risk Controls
- ✅ Maximum risk per trade (1% default)
- ✅ Daily trade limit (20 trades max)
- ✅ Maximum open positions (3 max)
- ✅ Automatic position sizing based on stop loss

### Error Handling
- ✅ Connection loss detection
- ✅ Invalid symbol protection
- ✅ Order execution validation
- ✅ Position verification

## ⚠️ Important Notes

### Before Going Live

1. **Test on Demo Account First**
   - Always start with a demo account
   - Verify all signals and executions
   - Monitor for at least 1 week

2. **Check MT5 Terminal**
   - Ensure MT5 terminal is running
   - Symbol XAUUSD must be available
   - Check your broker's spread and commissions

3. **Risk Management**
   - Start with minimum risk (0.5% per trade)
   - Never risk more than 2% per trade
   - Keep max open positions at 1-3

4. **Monitor Performance**
   - Check bot logs regularly
   - Monitor open positions
   - Track daily P&L

### Common Issues

**Connection Failed**
```
❌ MT5 initialization failed
```
Solution: Ensure MT5 terminal is running and logged in

**Symbol Not Found**
```
❌ Symbol XAUUSD not found
```
Solution: Enable XAUUSD in Market Watch (right-click → Show All)

**Order Execution Failed**
```
❌ Order failed: 10006 - Request rejected
```
Solution: Check account balance, margin, and broker restrictions

## 📈 Monitoring Live Trading

### Real-time Display

The bot shows:
- 🟢 Current open positions
- 💰 Total P&L
- 📊 Daily trade count
- ⚡ Signal detections
- ✅ Trade executions

### Example Output

```
═════════════════════════════════════════════════════════════════════════════
🤖 XAUUSD BOT - MT5 LIVE TRADING MODE
═════════════════════════════════════════════════════════════════════════════

✅ Connected to MT5
   Account: 12345678
   Server: XM-Demo
   Balance: $100,000.00
   Equity: $100,500.00

🎯 Trading Mode: 🟢 LONG 🔴 SHORT
⏱️  Check Interval: 60 seconds
🛡️  Risk Per Trade: 1.0%

🚀 Bot is now running... Press Ctrl+C to stop

🎯 SIGNAL DETECTED: BUY
   Entry: 2050.50
   SL: 2045.00 (5.50 points)
   TP: 2065.00 (14.50 points)
   Volume: 0.10 lots

✅ Trade executed successfully!

📊 Open Positions: 1 | Total P&L: $+150.00
```

## 🔧 Advanced Configuration

### Custom Check Interval

```python
# In xauusd_trading_bot.py CONFIG section
'mt5_check_interval': 60,  # Check every 60 seconds
```

### Timeframe Selection

```json
// In mt5_config.json
"timeframe": "M1"  // M1, M5, M15, M30, H1, H4, D1
```

### Trading Hours Filter

```json
// In mt5_config.json
"trading_hours": {
  "enabled": true,
  "start_hour": 7,
  "end_hour": 17,
  "timezone": "UTC"
}
```

## 📞 Support

For issues or questions:
1. Check MT5 connection: `python mt5_trader.py`
2. Review `mt5_config.json` settings
3. Test with `--mode backtest` first
4. Verify symbol availability in MT5
5. Check broker's trading conditions

## ⚖️ Disclaimer

**Educational purposes only. Trading involves substantial risk of loss.**

- Not financial advice
- Past performance ≠ future results
- Test thoroughly on demo account
- Never risk more than you can afford to lose
- Monitor your account regularly

---

**Ready to trade?** 

Start with: `python mt5_trader.py` to test your connection! 🚀
