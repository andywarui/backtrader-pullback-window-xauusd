# XAUUSD M30 Trading Bot - Quick Start Guide

## 🚀 Quick Setup (5 Minutes)

### **Step 1: Verify Installation**
```bash
# Check Python version (need 3.8+)
python --version

# Install dependencies
pip install backtrader MetaTrader5 pandas numpy
```

### **Step 2: Prepare Data File**
Place your M30 XAUUSD data in the data folder:
```
data/XAUUSD_M30_2020-2025.csv
```

**Format:** Date,Time,Open,High,Low,Close,Volume

### **Step 3: Configure MT5 (for live trading)**
Edit `mt5_config.json`:
```json
{
  "account": YOUR_ACCOUNT_NUMBER,
  "password": "YOUR_PASSWORD",
  "server": "YOUR_BROKER_SERVER",
  "symbol": "XAUUSD",
  "timeframe": "M30"
}
```

---

## 📊 Run Backtest

```bash
# Full backtest (2020-2025)
python xauusd_trading_bot.py --mode backtest

# Quick 30-day test
python xauusd_trading_bot.py --mode quick

# LONG trades only
python xauusd_trading_bot.py --long-only

# SHORT trades only
python xauusd_trading_bot.py --short-only

# Custom date range
python xauusd_trading_bot.py --from 2024-01-01 --to 2024-12-31
```

**Expected Output:**
```
================================================================================
[STATS] BACKTEST RESULTS - XAUUSD M30 TRADING BOT
================================================================================

[ACCOUNT] PORTFOLIO PERFORMANCE:
   Starting Capital:    $100,000.00
   Final Value:         $144,747.11
   Total P&L:           +$44,747.11
   Return:              +44.75%

[TARGET] TRADE STATISTICS:
   Total Trades:        175
   Winning Trades:      97 (55.43%)
   Losing Trades:       78

[MONEY] PROFITABILITY:
   Profit Factor:       1.64
   Sharpe Ratio:        0.892
   Max Drawdown:        5.81%
================================================================================
```

---

## 🔴 Live Trading (REAL MONEY!)

### **⚠️ CRITICAL: TEST ON DEMO FIRST!**

```bash
# Test MT5 connection
python mt5_trader.py

# Start live trading (after successful connection test)
python xauusd_trading_bot.py --mode mt5
```

### **What Happens When You Start:**

1. **Daily Bias Analysis** (30 seconds)
   - Analyzes H4, H1, D1 timeframes
   - Checks momentum indicators
   - Determines market direction
   - Sets confidence level

2. **Continuous Monitoring**
   - Checks for new M30 bars every 60 seconds
   - Runs multi-indicator analysis (EMA, RSI, MACD, Stochastic, Bollinger, Alligator)
   - Filters signals based on daily bias
   - Executes trades when 3-5/6 indicators align

3. **Real-Time Output:**
```
[TIMER] 2026-01-07 14:30:00 | Price: 2650.50 | Bias: 🟢 BULLISH | Analyzing...
   [LONG SCALP] RSI: 45.2 | Stoch: 35.5 | MACD: 0.25
   EMA5: 2649.75 | BB: 2648.00 | Signals: 5/6 (need 3) WITH BIAS

[TARGET] SIGNAL DETECTED: BUY
   Entry: 2650.50
   SL: 2645.00 (5.50 points)
   TP: 2660.25 (9.75 points)
   Volume: 0.05 lots

[OK] Trade executed successfully!

[STATS] Open Positions: 1 | Total P&L: $+125.50
```

---

## 🎯 Configuration Cheat Sheet

### **Key Settings (`xauusd_trading_bot.py`)**

```python
# Trading Direction
'enable_long': True              # Enable LONG trades
'enable_short': True             # Enable SHORT trades

# Risk Management
'risk_percent': 0.0125          # 1.25% per trade
'leverage': 30.0                 # 30:1 leverage

# Entry Windows
'long_window_periods': 5        # 5 bars for LONG breakout
'short_window_periods': 7       # 7 bars for SHORT breakout

# Pullback System
'long_pullback_candles': 3      # Wait for 3 red candles
'short_pullback_candles': 2     # Wait for 2 green candles
```

### **Prop Firm Safety (`mt5_config.json`)**

```json
"max_risk_per_trade": 0.0125        // 1.25% risk
"max_daily_trades": 3                // Max 3 trades/day
"max_open_positions": 3              // Max 3 concurrent
"max_daily_loss_percent": 0.05       // 5% daily loss limit
"emergency_stop_at_percent": 0.045   // Auto-stop at 4.5%
```

---

## 🛡️ Safety Features

### **Automatic Protection:**
✅ Max 3 trades per day
✅ Max 3 open positions simultaneously
✅ 1.25% risk per trade (not account balance!)
✅ Break-even trailing stop at 50% to TP
✅ Emergency stop at 4.5% daily loss
✅ Max overall drawdown: 10%

### **Manual Controls:**
- Press `Ctrl+C` to stop bot safely
- Bot closes gracefully, showing final status
- All open positions remain active (close manually if needed)

---

## 📈 Performance Monitoring

### **Live Status Indicators:**

| Icon | Meaning |
|------|---------|
| 🟢 | Bullish daily bias |
| 🔴 | Bearish daily bias |
| ⚪ | Neutral daily bias |
| ✅ | Long signal conditions met |
| 🔴 | Short signal conditions met |
| ⚠️  | Warning / Caution |
| 🛑 | Trade rejected / Safety limit hit |

### **Expected Trade Frequency:**
- **Backtested:** ~3 trades/month
- **Live:** May vary (2-5 trades/month typical)
- Depends on market conditions and daily bias

---

## 🔧 Troubleshooting

### **"Data file not found"**
```bash
# Check file exists
ls data/XAUUSD_M30_2020-2025.csv

# If not, ensure file is named exactly:
data/XAUUSD_M30_2020-2025.csv
```

### **"MT5 connection failed"**
1. Verify MT5 is running
2. Check account/password in `mt5_config.json`
3. Test connection: `python mt5_trader.py`
4. Ensure symbol "XAUUSD" exists on your broker

### **"No signals detected"**
✅ **This is NORMAL!**
- Strategy is selective (quality over quantity)
- Daily bias may filter out trades
- Market may be choppy/consolidating
- Wait for clean trend conditions

### **"Position size seems wrong"**
- Check account balance (bot uses 1.25% of balance)
- Review ATR value (should be ~0.50-2.00 for gold)
- Verify risk settings in config

---

## 📊 Signal Quality Indicators

### **HIGH QUALITY SIGNAL (Trade This!):**
```
Signals: 6/6 ✅ (WITH BIAS)
RSI: Between 30-70
Stochastic: Clear crossover
MACD: Histogram expanding
Volume: 1.2x average
Daily Bias: ALIGNED
```

### **MEDIUM QUALITY SIGNAL (Consider):**
```
Signals: 4/6 ⚠️ (NEUTRAL)
RSI: 40-60 range
Some indicators mixed
Volume: Normal
Daily Bias: NEUTRAL
```

### **LOW QUALITY SIGNAL (Skip):**
```
Signals: 3/6 🛑 (AGAINST BIAS)
RSI: Extreme levels
Conflicting indicators
Low volume
Daily Bias: OPPOSITE
```

---

## 🎯 Best Practices

### **Before Live Trading:**
1. ✅ Run backtest to understand behavior
2. ✅ Test on demo account for 1-2 weeks
3. ✅ Verify all safety limits work
4. ✅ Start with minimum position size
5. ✅ Monitor first 5-10 trades manually

### **During Live Trading:**
1. ✅ Check bot status daily
2. ✅ Review open positions in MT5
3. ✅ Monitor daily P&L
4. ✅ Let break-even trailing do its job
5. ✅ Don't interfere with trades unless emergency

### **Risk Management:**
1. ✅ Never exceed 1.25% per trade
2. ✅ Respect max daily loss limit (5%)
3. ✅ Don't add manual trades while bot runs
4. ✅ Keep emergency stop at 4.5%
5. ✅ Review performance weekly

---

## 📞 Support

**Issues or Questions:**
1. Check `PROJECT_FIXES_SUMMARY.md` for detailed troubleshooting
2. Review `README.md` for complete documentation
3. Check MT5 error logs if connection fails
4. Verify all configurations match this guide

**Common Questions:**

**Q: How often does daily bias update?**
A: Every 4 hours or on new trading day

**Q: Can I change the timeframe?**
A: Not recommended - strategy optimized for M30

**Q: Why so few trades?**
A: Quality over quantity - strict filters prevent bad trades

**Q: Should I trade during news events?**
A: Bot will trade if indicators align, but manually monitor during major news

**Q: Can I run multiple instances?**
A: No - one bot per MT5 account to avoid conflicts

---

## ✅ Pre-Flight Checklist

Before starting live trading, verify:

- [ ] MT5 installed and running
- [ ] Account credentials correct in `mt5_config.json`
- [ ] XAUUSD symbol available on broker
- [ ] Backtest ran successfully
- [ ] Demo account tested for 1-2 weeks
- [ ] Risk limits configured (1.25%, max 3 trades, 5% daily loss)
- [ ] Break-even trailing enabled
- [ ] Emergency stop at 4.5% enabled
- [ ] Sufficient account balance (recommended $5,000+ for 0.01 lots)
- [ ] Understand signal quality indicators
- [ ] Know how to stop bot safely (Ctrl+C)

---

## 🚀 You're Ready!

If all checks pass and demo testing went well, you're ready to start live trading. Remember:

- ✅ Start small
- ✅ Be patient
- ✅ Trust the process
- ✅ Monitor regularly
- ✅ Don't overtrade manually

**Good luck trading! 📈💰**

---

**Last Updated:** January 7, 2026
**Bot Version:** 2.1 (M30 Fixed)
**Status:** ✅ Ready for Live Trading
