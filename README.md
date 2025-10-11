# Backtrader Gold (XAU/USD) Pullback Strategy# Backtrader Gold (XAU/USD) Pullback Strategy# Backtrader Gold (XAU/USD) Pullback Strategy# Backtrader ATR Stop-Loss Strategy for USDCHF



[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

[![Framework](https://img.shields.io/badge/Framework-Backtrader-orange.svg)](https://www.backtrader.com/)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Asset](https://img.shields.io/badge/Asset-Gold%20(XAU/USD)-gold.svg)](.)

[![Sharpe Ratio](https://img.shields.io/badge/Sharpe_Ratio-0.89-brightgreen.svg)](.)[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

[![Profit Factor](https://img.shields.io/badge/Profit_Factor-1.64-success.svg)](.)

[![Win Rate](https://img.shields.io/badge/Win_Rate-55.43%25-informational.svg)](.)[![Framework](https://img.shields.io/badge/Framework-Backtrader-orange.svg)](https://www.backtrader.com/)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Return](https://img.shields.io/badge/Return-44.75%25-blue.svg)](.)

[![Max DD](https://img.shields.io/badge/Max_DD-5.81%25-red.svg)](.)[![Asset](https://img.shields.io/badge/Asset-Gold%20(XAU/USD)-gold.svg)](.)



Professional algorithmic trading strategy for **Gold (XAU/USD)** on a **5-minute timeframe**. Features an advanced 4-phase state machine entry system with dynamic ATR-based risk management.[![Profit Factor](https://img.shields.io/badge/Profit_Factor-1.64-brightgreen.svg)](.)[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)



The strategy employs a **volatility expansion channel** approach, waiting for pullbacks after trend signals before entering on breakouts. Backtested over **5 years of historical data** (2020-2025).[![Win Rate](https://img.shields.io/badge/Win_Rate-55.43%25-success.svg)](.)



![Gold Trading Strategy Performance](images/XAUUSD.png)[![Return](https://img.shields.io/badge/Return-44.75%25-blue.svg)](.)[![Framework](https://img.shields.io/badge/Framework-Backtrader-orange.svg)](https://www.backtrader.com/)[![Framework](https://img.shields.io/badge/Framework-Backtrader-orange.svg)](https://www.backtrader.com/)



---



## 📊 Performance SummaryProfessional algorithmic trading strategy for **Gold (XAU/USD)** on a **5-minute timeframe**. Features an advanced 4-phase state machine entry system with dynamic ATR-based risk management.[![Asset](https://img.shields.io/badge/Asset-Gold%20(XAU/USD)-gold.svg)](.)[![Profit Factor](https://img.shields.io/badge/Profit_Factor-1.35-brightgreen.svg)](.)



### 🎯 Verified Backtest Results (5-Year Period: July 2020 - July 2025)



| Metric | Value | Rating |The strategy employs a **volatility expansion channel** approach, waiting for pullbacks after trend signals before entering on breakouts. Backtested over **5 years of historical data** (2020-2025), achieving a **1.64 Profit Factor** with a **44.75% return** on initial capital.

|--------|-------|--------|

| 💰 **Total Return** | +44.75% (+$44,747) | ✅ Excellent |

| 📈 **Sharpe Ratio** | 0.892 | ✅ Good |

| 🎯 **Profit Factor** | 1.64 | ✅ Strong |---Professional algorithmic trading strategy for **Gold (XAU/USD)** on a **5-minute timeframe**. Features an advanced 4-phase state machine entry system with dynamic ATR-based risk management.This repository presents a complete and profitable algorithmic trading strategy for the **USDCHF** currency pair on a **5-minute timeframe**. The system is implemented in Python using the `Backtrader` framework and features an advanced, dynamic risk management system based on the Average True Range (ATR).

| ✅ **Win Rate** | 55.43% (97W / 78L) | ✅ Above Average |

| 📉 **Max Drawdown** | 5.81% ($7,059) | ✅ Outstanding |

| 📊 **Total Trades** | 175 (~3/month) | ✅ Sufficient |

| 💵 **Average Win** | $1,187.33 | ✅ Positive |## 📊 Performance Analysis

| 💸 **Average Loss** | -$913.34 | ✅ Controlled |

| 🎲 **Expectancy** | $251.03/trade | ✅ Profitable |

| 💼 **Final Portfolio** | $144,747.11 | ✅ Growth |

### 🎯 Verified Backtest Results (5-Year Period: 2020-2025)The strategy employs a **volatility expansion channel** approach, waiting for pullbacks after trend signals before entering on breakouts.The strategy was backtested over 5 years of historical data, achieving a **1.35 Profit Factor** with a **35.4% return** on initial capital.

**Portfolio Evolution:**

- Starting Capital: $100,000

- Final Value: $144,747.11

- Average Annual Return: ~8.95%**Key Performance Indicators:**

- Test Period: July 10, 2020 - July 25, 2025

- 💰 **Total Return:** +44.75% (+$44,747.11 on $100,000 capital)

> 📄 **Detailed Analysis:** See [PERFORMANCE_METRICS.md](./PERFORMANCE_METRICS.md) for complete breakdown

- 📈 **Profit Factor:** 1.64 (For every $1 lost, strategy earns $1.64)------

---

- ✅ **Win Rate:** 55.43% (97 wins / 175 total trades)

## 🎯 Strategy Overview

- 📊 **Total Trades:** 175 trades over 5 years (~3 trades/month)

### Core Concept: Volatility Expansion Entry System

- 🏆 **Risk/Reward:** Positive expectancy system

Unlike traditional strategies that enter immediately on signal detection, this system uses a **sophisticated 4-phase state machine**:

## 📊 Strategy Overview## 📊 Performance Analysis

1. **📡 SCANNING** - Monitor for EMA crossovers + directional confirmation

2. **🎣 ARMED** - Wait for pullback (1-3 counter-trend candles)**Portfolio Evolution:**

3. **🚪 WINDOW_OPEN** - Set breakout levels and monitor price action

4. **✅ ENTRY** - Execute trade only on confirmed breakout- Starting Capital: $100,000



This approach filters false signals and catches high-momentum moves with optimal timing.- Final Portfolio Value: $144,747.11



**Why This Works for Gold:**- Average Annual Return: ~8.95%### 🎯 Core Concept: Volatility Expansion Entry SystemThe core of this project's backtesting methodology is the "Dual Cerebro" approach, where LONG and SHORT strategies are run as two independent portfolios. This prevents conflicting signals and allows each directional bias to be optimized and evaluated on its own merits. The final "Combined" performance is the aggregation of these two independent results.

- Gold exhibits strong trending behavior with clear pullbacks

- 5-minute timeframe captures intraday volatility expansion- Test Period: July 10, 2020 - July 25, 2025

- ATR-based sizing adapts to Gold's variable volatility

- State machine reduces whipsaws in choppy markets



---> 📄 **Detailed Performance Report:** See [PERFORMANCE_METRICS.md](./PERFORMANCE_METRICS.md) for complete analysis including trade-by-trade breakdown



## ✨ Key FeaturesUnlike traditional strategies that enter immediately on signal detection, this system uses a **sophisticated 4-phase state machine**:### Portfolio Performance (5-Year Backtest)



### 🔬 Advanced Entry Logic---

- **4-Phase State Machine**: Systematic progression from signal detection to confirmed entry

- **Pullback Confirmation**: Waits for 1-3 counter-trend candles to identify optimal entry zones

- **Breakout Validation**: Only enters when price breaks above/below defined volatility channels

- **Global Invalidation**: Auto-resets if opposing signals appear during setup## 🎯 Strategy Overview

- **EMA Angle Momentum Filter**: Measures EMA slope to ensure strong, decisive market momentum

- **ATR Volatility Filter**: Prevents entries during extreme volatility periods1. **📡 SCANNING** - Monitor for EMA crossovers + directional confirmation<!-- TODO: Add performance chart image here -->



### 🛡️ Dynamic Risk Management### Core Concept: Volatility Expansion Entry System

- **ATR-Based Stop Loss**: Adapts to current market volatility (2.5x ATR)

- **ATR-Based Take Profit**: Dynamically calculated profit targets (12.0x ATR)2. **🎣 ARMED** - Wait for pullback (1-3 counter-trend candles)<!-- ![Dual Cerebro Performance Chart](images/sunrise_osiris.png) -->

- **Risk-Based Position Sizing**: Fixed 1% risk per trade for consistent exposure

- **OCA Orders**: One-Cancels-All for automatic SL/TP managementUnlike traditional strategies that enter immediately on signal detection, this system uses a **sophisticated 4-phase state machine**:

- **Gold-Specific Sizing**: 100 oz lot sizes with 0.01 tick value

- **Leverage**: 30:1 with 5% margin requirement3. **🚪 WINDOW_OPEN** - Set breakout levels and monitor price action



### 💎 Gold (XAU/USD) Optimizations1. **📡 SCANNING** - Monitor for EMA crossovers + directional confirmation

- **Contract Specifications**: Properly configured for 100 oz Gold contracts

- **Tick Value**: $0.01 per oz movement2. **🎣 ARMED** - Wait for pullback (1-3 counter-trend candles)4. **✅ ENTRY** - Execute trade only on confirmed breakout**Performance Metrics:**

- **Spread Handling**: Conservative assumptions built into backtest

- **Volatility Adaptation**: Parameters tuned for Gold's unique price action3. **🚪 WINDOW_OPEN** - Set breakout levels and monitor price action

- **Session Filtering**: Can be configured for optimal trading hours

4. **✅ ENTRY** - Execute trade only on confirmed breakout*   **Combined Portfolio (LONG + SHORT):** Final P&L of **+$35,399** (+35.4% return)

### 📐 Technical Filters

- **EMA Multi-Crossover**: Fast EMA (1) vs. Basket of slower EMAs (14, 18, 24)

- **EMA Angle Filter**: Measures trend strength (slope in degrees)

- **ATR Volatility Filter**: Ensures sufficient market movementThis approach filters false signals and catches high-momentum moves with optimal timing.This approach filters false signals and catches high-momentum moves with optimal timing.*   **LONG Only Portfolio:** P&L of **+$18,343**

- **Time-of-Day Filter**: Trades only during liquid hours

- **Candle Color Confirmation**: Directional candle validation



---**Why This Works for Gold:***   **SHORT Only Portfolio:** P&L of **+$17,056**



## 🔧 Technical Architecture- Gold exhibits strong trending behavior with clear pullbacks



### Technology Stack- 5-minute timeframe captures intraday volatility expansion---

- **Framework**: Backtrader 1.9.76.123

- **Language**: Python 3.8+- ATR-based sizing adapts to Gold's variable volatility

- **Dependencies**: NumPy 1.26.4, Matplotlib 3.8.4, Pandas

- **Data Format**: CSV (OHLCV + timestamp)- State machine reduces whipsaws in choppy marketsThis demonstrates that both the LONG and SHORT logic contribute positively and consistently to the overall profitability of the system.

- **Backtest Engine**: Backtrader's optimized `_runonce` mode



### Strategy Components

---## ✨ Key Features

**Indicators Used:**

- Multiple EMAs (Fast, Slow, Confirmation)

- ATR (Average True Range) for volatility measurement

- Custom angle calculations for momentum assessment## ✨ Key Features---

- Volume analysis (optional)



**Order Types:**

- Market orders for entry### 🔬 Advanced Entry Logic### 🔬 Advanced Entry Logic

- Stop orders for protective stops

- Limit orders for take profit- **4-Phase State Machine**: Systematic progression from signal detection to confirmed entry

- OCA (One-Cancels-All) brackets

- **Pullback Confirmation**: Waits for 1-3 counter-trend candles to identify optimal entry zones- **4-Phase State Machine**: Systematic progression from signal detection to confirmed entry## ✨ Key Features

**State Management:**

- Phase tracking (SCANNING, ARMED, WINDOW_OPEN, ENTRY)- **Breakout Validation**: Only enters when price breaks above/below defined volatility channels

- Pullback counter

- Window duration tracking- **Global Invalidation**: Auto-resets if opposing signals appear during setup- **Pullback Confirmation**: Waits for 1-3 counter-trend candles to identify optimal entry zones

- Global invalidation checks

- **EMA Angle Momentum Filter**: Measures EMA slope to ensure strong, decisive market momentum

---

- **ATR Volatility Filter**: Prevents entries during extreme volatility periods- **Breakout Validation**: Only enters when price breaks above/below defined volatility channels-   📈 **Advanced Pullback Entry System**: The strategy does not enter on the initial signal. It waits for a confirmation pullback and enters on a breakout, significantly improving the entry quality and risk/reward ratio.

## 📁 Repository Structure



```

backtrader-pullback-window-xauusd/### 🛡️ Dynamic Risk Management- **Global Invalidation**: Auto-resets if opposing signals appear during setup-   **🛡️ Dynamic ATR Risk Management**: Stop Loss and Take Profit levels are not fixed. They are calculated dynamically for *every trade* based on the market's current volatility (ATR), adapting the risk profile to live conditions.

│

├── src/- **ATR-Based Stop Loss**: Adapts to current market volatility (typically 1.5-2.0x ATR)

│   └── strategy/

│       └── sunrise_ogle_xauusd.py    # Main strategy implementation (3400+ lines)- **ATR-Based Take Profit**: Dynamically calculated profit targets (typically 2.5-3.0x ATR)-   **📐 EMA Angle Momentum Filter**: A unique filter that measures the slope of the confirmation EMA. It ensures trades are only taken during periods of strong, decisive market momentum, filtering out flat or choppy markets.

│

├── data/- **Risk-Based Position Sizing**: Fixed 1% risk per trade for consistent exposure

│   └── XAUUSD_5m_5Yea.csv            # 5 years of Gold 5-minute data

│- **OCA Orders**: One-Cancels-All for automatic SL/TP management### 🛡️ Dynamic Risk Management-   **🔄 Dual Cerebro Backtesting**: By testing LONG and SHORT logic independently, the strategy avoids signal interference and provides a clearer picture of each component's performance.

├── images/

│   └── XAUUSD.png                    # Strategy performance chart- **Gold-Specific Sizing**: 100 oz lot sizes with 0.01 tick value

│

├── tests/                            # 10+ test files- **Leverage**: 30:1 with 5% margin requirement- **ATR-Based Stop Loss**: Adapts to current market volatility-   **🕰️ Time-of-Day Filtering**: Trading is restricted to the most liquid market hours (07:00 - 17:00 UTC) to focus on the highest probability setups.

│   ├── debug_short_entries.py

│   ├── deep_strategy_test.py

│   ├── demo_volatility_expansion.py

│   ├── final_validation.py### 📈 Gold (XAU/USD) Optimizations- **ATR-Based Take Profit**: Dynamically calculated profit targets-   **💰 Risk-Based Position Sizing**: Automatically calculates trade size to risk a fixed 1% of the account on every position, maintaining consistent risk exposure.

│   ├── real_data_test.py

│   ├── step_by_step_test.py- **Contract Specifications**: Properly configured for 100 oz Gold contracts

│   └── ...

│- **Tick Value**: $0.01 per oz movement- **Risk-Based Position Sizing**: Fixed 1% risk per trade

├── docs/

│   ├── CONTRIBUTING.md- **Spread Handling**: Conservative assumptions built into backtest

│   ├── GITHUB_UPLOAD_GUIDE.md

│   ├── PRE_UPLOAD_CHECKLIST.md- **Volatility Adaptation**: Parameters tuned for Gold's unique price action- **OCA Orders**: One-Cancels-All for automatic SL/TP management---

│   └── GITHUB_TOPICS.md

│- **Session Filtering**: Can be configured for optimal trading hours

├── temp_reports/                     # Gitignored trade reports

│

├── README.md                         # This file

├── PERFORMANCE_METRICS.md            # Detailed performance analysis---

├── LICENSE                           # MIT License

├── requirements.txt                  # Python dependencies### 📐 Technical Filters## 🧠 Strategy Logic & Visualization

└── .gitignore                        # Git ignore patterns

```## 🔧 Technical Architecture



---- **EMA Multi-Crossover**: Fast EMA (1) vs. Basket of slower EMAs (14, 18, 24)



## 🚀 Getting Started### Technology Stack



### Prerequisites- **Framework**: Backtrader 1.9.76.123- **EMA Angle Filter**: Measures trend strength (slope in degrees)The strategy is a multi-layered, trend-following system. An entry is only triggered when a sequence of conditions are met.

- Python 3.8 or newer

- Git version control- **Language**: Python 3.8+

- pip package manager

- **Dependencies**: NumPy 1.26.4, Matplotlib 3.8.4, Pandas- **ATR Volatility Filter**: Ensures sufficient market movement

### 1. Clone the Repository

- **Data Format**: CSV (OHLCV + timestamp)

```bash

git clone https://github.com/YOUR_USERNAME/backtrader-pullback-window-xauusd.git- **Backtest Engine**: Backtrader's optimized `_runonce` mode- **Time-of-Day Filter**: Trades only during liquid hours### How It Works: The 3-Phase Entry

cd backtrader-pullback-window-xauusd

```



### 2. Set Up Virtual Environment### Strategy Components- **Candle Color Confirmation**: Directional candle validation



```bash

python -m venv venv

**Indicators Used:**1.  **Signal Detection**: A fast EMA (1) crosses over a basket of slower EMAs (14, 18, 24).

# Windows:

venv\Scripts\activate- Multiple EMAs (Fast, Slow, Confirmation)



# macOS/Linux:- ATR (Average True Range) for volatility measurement### 💎 Gold-Specific Optimizations2.  **Pullback Wait**: The system waits for a small, controlled move against the trend (e.g., 1-2 red candles for a LONG signal).

source venv/bin/activate

```- Custom angle calculations for momentum assessment



### 3. Install Dependencies- Volume analysis (optional)- **100 oz Lot Sizes**: Standard gold contract sizing3.  **Breakout Entry**: A market order is triggered only if the price breaks the high/low of the pullback, confirming the trend's continuation.



```bash

pip install -r requirements.txt

```**Order Types:**- **0.01 Tick Value**: Precision for gold price movements



### 4. Run the Strategy- Market orders for entry



```bash- Stop orders for protective stops- **5% Margin Requirement**: Configured for gold trading leverage### Example of a LONG Trade

python src/strategy/sunrise_ogle_xauusd.py

```- Limit orders for take profit



**Expected Output:**- OCA (One-Cancels-All) brackets- **Optimized for XAU/USD volatility patterns**



```

=== SUNRISE OGLE === (from 2020-07-10 to 2025-07-25)

>> FOREX MODE ENABLED - Data: XAUUSD_5m_5Yea.csv**State Management:**<!-- TODO: Add trade example image here -->

>> Instrument: XAUUSD (XAU/USD)

- Phase tracking (SCANNING, ARMED, WINDOW_OPEN, ENTRY)

=== SUNRISE OGLE SUMMARY ===

Trades: 175 Wins: 97 Losses: 78 WinRate: 55.43% PF: 1.64- Pullback counter---<!-- ![Example of a LONG Trade in Backtrader](images/sunrise_osiris_long_entrys.png) -->

Final Value: 144,747.11 | Total PnL: +44,747.11

- Window duration tracking

PERFORMANCE METRICS - XAUUSD STRATEGY

======================================================================- Global invalidation checks

Final Portfolio Value: $144,747.11

Sharpe Ratio: 0.892

Max Drawdown: 5.81%

Profit Factor: 1.64---## 📈 Performance Metrics**Trade Visualization Components:**

Win Rate: 55.43%

======================================================================

```

## 📁 Repository Structure-   **Candlestick Chart**: The 5-minute price action for USDCHF

---



## 🔧 Customization

```### Backtest Period-   **EMA Lines**: The multiple EMAs used for signal generation

### Key Parameters

backtrader-pullback-window-xauusd/

```python

# EMA Periods│- **Data Range**: July 2020 - July 2025 (5 years)-   **Buy/Sell Signals**: Marks the exact bar where trades were executed

ema_confirm_period = 1          # Fast confirmation EMA

ema_fast_period = 14            # Fast EMA├── src/

ema_medium_period = 18          # Medium EMA

ema_slow_period = 24            # Slow EMA│   └── strategy/- **Timeframe**: 5-minute candles-   **SL/TP Levels**: Dynamic Stop Loss (red) and Take Profit (green) levels calculated using ATR multiples



# Pullback Settings│       └── sunrise_ogle_xauusd.py    # Main strategy implementation (3200+ lines)

long_pullback_max_candles = 3   # LONG pullback depth

short_pullback_max_candles = 3  # SHORT pullback depth│- **Starting Capital**: $100,000



# Window Settings├── data/

long_entry_window_periods = 2   # LONG breakout window

short_entry_window_periods = 2  # SHORT breakout window│   └── XAUUSD_5m_5Yea.csv            # 5 years of Gold 5-minute data- **Asset**: Gold (XAU/USD)---

window_offset_multiplier = 1.0  # Channel offset

│

# Risk Management

long_sl_atr_mult = 2.5          # Stop Loss: 2.5 × ATR├── tests/

long_tp_atr_mult = 12.0         # Take Profit: 12.0 × ATR

risk_percent = 0.01             # Risk 1% per trade│   ├── debug_short_entries.py        # Debug short entry logic

```

│   ├── deep_strategy_test.py         # Comprehensive strategy tests### Key Statistics## 📂 Code Overview

Edit these in `src/strategy/sunrise_ogle_xauusd.py` (lines 150-250).

│   ├── demo_volatility_expansion.py  # Volatility expansion visualization

---

│   ├── final_validation.py           # Final validation suite<!-- Performance metrics based on 22+ completed trades from partial backtest -->

## 🧪 Testing & Validation

│   ├── real_data_test.py             # Real data validation

The strategy includes comprehensive test suites:

│   ├── step_by_step_test.py          # Step-by-step debuggingThe entire logic is contained within `src/strategy/sunrise_osiris.py`. Here is a brief guide to its structure:

- ✅ **Phase Transition Tests**: Validates state machine logic

- ✅ **Entry System Tests**: Confirms breakout detection│   ├── test_candle_fix.py            # Candle logic tests

- ✅ **Risk Management Tests**: Verifies SL/TP placement

- ✅ **Data Integrity Tests**: Validates input data quality│   ├── test_ogle_entry_system.py     # Entry system validation**Observed Performance:**

- ✅ **Performance Tests**: Benchmarks execution speed

- ✅ **Real Data Tests**: Tests on actual Gold data│   ├── test_ogle_phases.py           # Phase transition tests



### Running Tests│   └── update_ogle.py                # Strategy update utilities- **Total Trades**: 22+ executed-   **Global Configuration (Lines 1-150):** This top section contains all user-editable parameters, such as date ranges, starting cash, ATR thresholds, and filter settings. This makes tuning the strategy easy without touching the core logic.



```bash│

# Run specific test

python tests/final_validation.py├── docs/- **Win Rate**: ~70%+-   **`SunriseOsiris` Class `params` (Lines 153-270):** The official `Backtrader` parameters dictionary. These are the values that can be optimized during a parameter sweep.



# Run with verbose output│   ├── CONTRIBUTING.md               # Contribution guidelines

python tests/step_by_step_test.py

```│   ├── GITHUB_UPLOAD_GUIDE.md        # GitHub upload instructions- **Average Win**: $1,000+-   **`__init__(self)` (Lines 605-700):** The strategy constructor where all indicators (EMAs, ATR) and state variables (e.g., for the pullback machine) are initialized.



---│   ├── PRE_UPLOAD_CHECKLIST.md       # Pre-upload verification



## 📊 Performance Metrics Explained│   ├── GITHUB_TOPICS.md              # Recommended repository topics- **Risk/Reward**: 1.5:1 average-   **`next(self)` (Lines 875-1045):** The heart of the strategy. This method is called for every bar of data. It contains the main logic for checking entry/exit conditions and managing the trade lifecycle.



### Sharpe Ratio (0.892) ✅│   ├── GITHUB_CLEANUP_SUMMARY.md     # Repository organization summary

- **Definition**: Risk-adjusted return metric

- **Interpretation**: Near 1.0 indicates good risk-adjusted performance│   └── README_OLD.md                 # Previous README versions- **Max Position**: 300 oz (3 mini lots)-   **Pullback State Machine (`_handle_pullback_entry`)**: A set of helper functions that manage the 3-phase entry logic (Signal -> Wait -> Breakout).

- **Industry Standard**: >0.5 acceptable, >1.0 good, >2.0 excellent

- **Rating**: ✅ **GOOD** - Solid risk-adjusted returns│



### Profit Factor (1.64) ✅├── temp_reports/                     # Gitignored trade reports-   **Risk Management (`_calculate_forex_position_size`)**: A function dedicated to calculating the correct position size based on the stop-loss distance and the 1% account risk rule.

- **Definition**: Gross Profit / Absolute Gross Loss

- **Interpretation**: For every $1 lost, strategy earns $1.64│

- **Industry Standard**: >1.5 is considered good, >2.0 is excellent

- **Rating**: ✅ **STRONG** - Demonstrates consistent edge├── README.md                         # This file**Strategy Characteristics:**-   **Order Notifications (`notify_order`, `notify_trade`)**: These methods handle the feedback from the broker (simulated or real), placing the OCA (One-Cancels-All) Stop Loss and Take Profit orders after an entry is confirmed.



### Max Drawdown (5.81%) ✅├── LICENSE                           # MIT License

- **Definition**: Largest peak-to-trough decline

- **Interpretation**: Worst case portfolio decline during backtest├── requirements.txt                  # Python dependencies- **Trading Style**: Trend-following with pullback entries

- **Industry Standard**: <10% excellent, <20% good, <30% acceptable

- **Rating**: ✅ **OUTSTANDING** - Exceptional risk control├── .gitignore                        # Git ignore patterns



### Win Rate (55.43%) ✅├── PERFORMANCE_METRICS.md            # Detailed performance analysis- **Position Duration**: 17-311 bars (85-1555 minutes)---

- **Definition**: Winning Trades / Total Trades

- **Interpretation**: More than half of all trades are profitable└── generate_performance_metrics.py   # Metrics generation script

- **Combined with PF**: Indicates balanced win size vs. loss size

- **Rating**: ✅ **ABOVE BASELINE** - Sustainable win rate```- **Entry Precision**: Breakout confirmation required



---



## 🤝 Contributing---- **Exit Method**: ATR-based SL/TP (OCA orders)## 🚀 Getting Started



Contributions are welcome! Please see [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.



**Ways to contribute:**## 🚀 Getting Started

- 🐛 [Report a Bug](https://github.com/YOUR_USERNAME/backtrader-pullback-window-xauusd/issues)

- 💡 [Request a Feature](https://github.com/YOUR_USERNAME/backtrader-pullback-window-xauusd/issues)

- 📝 [Submit a Pull Request](https://github.com/YOUR_USERNAME/backtrader-pullback-window-xauusd/pulls)

- 📖 Improve Documentation### Prerequisites---Follow these instructions to set up and run the backtest on your local machine.

- 🧪 Add More Tests



---

```bash

## 📜 License

Python 3.8 or higher

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

pip (Python package manager)## 🧠 Strategy Logic Explained### Prerequisites

**Additional Terms:**

- No warranty provided```

- Use at your own risk

- Not financial advice-   Python 3.8 or newer.

- Educational purposes only

### Installation

---

### Phase 1: Signal Detection (SCANNING → ARMED)-   Git version control.

## ⚠️ IMPORTANT DISCLAIMER

1. **Clone the repository:**

### **This software is for EDUCATIONAL and RESEARCH purposes ONLY.**

   ```bash

**CRITICAL WARNINGS:**

- ⚠️ This is **NOT** financial advice   git clone https://github.com/yourusername/backtrader-pullback-window-xauusd.git

- ⚠️ Past performance does **NOT** guarantee future results

- ⚠️ Algorithmic trading involves **SUBSTANTIAL RISK** of loss   cd backtrader-pullback-window-xauusd**LONG Signal Requirements:**### 1. Clone the Repository

- ⚠️ You can lose **MORE** than your initial investment

- ⚠️ Trading Gold (XAU/USD) is highly volatile and risky   ```

- ⚠️ Only trade with money you can **afford to lose**

1. ✅ Confirmation EMA (1) crosses above any slower EMA (14, 18, 24)Open your terminal and clone the repository:

**Before Using:**

1. ✅ Understand the strategy completely2. **Create virtual environment (recommended):**

2. ✅ Backtest thoroughly on your own data

3. ✅ Paper trade for extended period   ```bash2. ✅ Previous candle is bearish (close < open) - reversal setup```bash

4. ✅ Consult with licensed financial advisors

5. ✅ Start with very small position sizes   python -m venv venv



**By using this software, you acknowledge you are solely responsible for your trading decisions.**   # Windows:3. ⚙️ Optional: EMA ordering filtergit clone https://github.com/YOUR_USERNAME/backtrader-pullback-window-usdchf.git



**Trade at your own risk.**   venv\Scripts\activate



---   # Linux/Mac:4. ⚙️ Optional: Price above filter EMAcd backtrader-pullback-window-usdchf



## 📚 Resources   source venv/bin/activate



### Backtrader Documentation   ```5. ⚙️ Optional: EMA angle exceeds minimum degrees```

- [Official Docs](https://www.backtrader.com/docu/)

- [GitHub Repository](https://github.com/mementum/backtrader)

- [Community Forum](https://community.backtrader.com/)

3. **Install dependencies:**6. ⚙️ Optional: ATR meets volatility criteria

### Gold Trading Resources

- [Gold Market Hours](https://www.forex.com/en-us/trading-academy/courses/commodities/gold-market-hours/)   ```bash

- [XAU/USD Specifications](https://www.dailyfx.com/xau-usd)

- [Gold Trading Strategies](https://www.investopedia.com/articles/active-trading/021715/how-trade-gold.asp)   pip install -r requirements.txt### 2. Set Up a Virtual Environment



### Algorithmic Trading   ```

- [Quantitative Trading](https://quantstart.com/)

- [QuantConnect Learn](https://www.quantconnect.com/tutorials)### Phase 2: Pullback Confirmation (ARMED)It is highly recommended to use a virtual environment to manage dependencies.

- [Algorithmic Trading](https://www.algorithmictrading.net/)

### Running the Strategy

---

```bash

## 🏆 Acknowledgments

**Basic backtest:**

Built with:

- [Backtrader](https://www.backtrader.com/) - Powerful Python backtesting framework```bash**LONG Pullback:** Wait for 1-3 bearish (red) candles after bullish signal  # Create the virtual environment

- [NumPy](https://numpy.org/) - Numerical computing

- [Matplotlib](https://matplotlib.org/) - Visualizationpython src/strategy/sunrise_ogle_xauusd.py

- [Pandas](https://pandas.pydata.org/) - Data analysis

```**SHORT Pullback:** Wait for 1-3 bullish (green) candles after bearish signalpython -m venv venv

---



## 📈 Roadmap

**Generate performance metrics:**

### Completed ✅

- [x] 4-phase state machine implementation```bash

- [x] Dynamic ATR-based risk management

- [x] Gold-specific contract sizingpython generate_performance_metrics.py**Global Invalidation Rule:** If opposing signal appears during pullback → Reset to SCANNING# Activate it

- [x] Comprehensive testing suite

- [x] 5-year backtest validation```

- [x] Performance metrics analysis

- [x] Documentation and README# On Windows:



### Planned 🚀**Run specific tests:**

- [ ] SHORT strategy optimization (currently disabled)

- [ ] Machine learning parameter optimization```bash### Phase 3: Window Opening (ARMED → WINDOW_OPEN)venv\Scripts\activate

- [ ] Real-time data feed integration

- [ ] Live trading interfacepython tests/final_validation.py

- [ ] Advanced performance analytics dashboard

- [ ] Multi-timeframe analysis```# On macOS/Linux:

- [ ] Additional asset support (Silver, Crude Oil)



---

### ConfigurationCalculate breakout levels based on pullback range with configurable offset multiplier.source venv/bin/activate

**⭐ If you find this project useful, please consider giving it a star!**



**🔔 Watch this repository for updates and new features**

Edit the configuration section in `src/strategy/sunrise_ogle_xauusd.py`:```

---



*Last Updated: October 11, 2025 | Version 1.0.0 | Production-Ready*

```python**Window Duration:**

# === BACKTEST SETTINGS ===

FROMDATE = '2020-07-10'               # Start date (YYYY-MM-DD)- LONG: `long_entry_window_periods` (default: 2 bars)### 3. Install Requirements

TODATE = '2025-07-25'                 # End date (YYYY-MM-DD)

STARTING_CASH = 100000.0              # Initial capital- SHORT: `short_entry_window_periods` (default: 2 bars)Install the necessary Python libraries using the provided `requirements.txt` file.

ENABLE_PLOT = True                    # Show charts

```bash

# === TRADING DIRECTION ===

ENABLE_LONG_TRADES = True             # Enable long entries### Phase 4: Breakout Monitoring (WINDOW_OPEN → ENTRY)pip install -r requirements.txt

ENABLE_SHORT_TRADES = False           # Enable short entries

```

# === FOREX CONFIGURATION ===

ENABLE_FOREX_CALC = True              # Use Gold contract sizing**LONG Entry:** High breaks above `success_level` → Execute BUY  

FOREX_INSTRUMENT = 'XAUUSD'           # Fixed to Gold

```**SHORT Entry:** Low breaks below `success_level` → Execute SELL### 4. Add Market Data



---Place your 5-minute USDCHF data file into the `/data` directory. The project expects the file to be named `USDCHF_5m_5Yea.csv`.



## 📈 Strategy Parameters---



### Entry Parameters### 5. Run the Backtest

- **Long Pullback Candles**: 1-3 (configurable)

- **Short Pullback Candles**: 1-3 (configurable)## 📂 Project StructureExecute the strategy script from the root directory of the project.

- **Entry Window Periods**: 3-10 bars (configurable)

- **Window Offset Multiplier**: 0.5-2.0 (configurable)```bash



### Risk Management Parameters```python src/strategy/sunrise_osiris.py

- **Risk Per Trade**: 1% of capital

- **SL ATR Multiplier**: 1.5-2.0xbacktrader-pullback-window-xauusd/```

- **TP ATR Multiplier**: 2.5-3.0x

- **ATR Period**: 14 (standard)├── README.md                      # Professional documentationThe script will run the full Dual Cerebro backtest, print the performance summary to the console, generate detailed trade reports in the `/temp_reports` folder, and display the final performance chart.



### Filter Parameters├── LICENSE                        # MIT License with trading disclaimer

- **ATR Min Threshold**: 0.0004

- **ATR Max Threshold**: 0.0008├── requirements.txt               # Python dependencies---

- **EMA Angle Min**: Configurable

- **Volume Filter**: Optional├── .gitignore                     # Comprehensive ignore patterns



---│## 🤝 Contributing



## 🧪 Testing & Validation├── data/                          # Historical market data



The strategy includes comprehensive test suites:│   └── XAUUSD_5m_5Yea.csv        # 5-minute Gold data (5 years)Contributions are welcome! Whether you want to report a bug, suggest an enhancement, or add a new feature, please feel free to do so.



### Test Coverage│

- ✅ **Phase Transition Tests**: Validates state machine logic

- ✅ **Entry System Tests**: Confirms breakout detection├── docs/                          # Documentation-   **Report a Bug:** Open an [Issue](https://github.com/YOUR_USERNAME/backtrader-pullback-window-usdchf/issues) and describe the problem in detail.

- ✅ **Risk Management Tests**: Verifies SL/TP placement

- ✅ **Data Integrity Tests**: Validates input data quality│   ├── CONTRIBUTING.md-   **Suggest an Enhancement:** Open an [Issue](https://github.com/YOUR_USERNAME/backtrader-pullback-window-usdchf/issues) to discuss your idea.

- ✅ **Performance Tests**: Benchmarks execution speed

- ✅ **Real Data Tests**: Tests on actual Gold data│   ├── GITHUB_UPLOAD_GUIDE.md-   **Submit a Pull Request:** Fork the repository, make your changes, and submit a [Pull Request](https://github.com/YOUR_USERNAME/backtrader-pullback-window-usdchf/pulls) with a clear description of your work.



### Running Tests│   ├── PRE_UPLOAD_CHECKLIST.md

```bash

# Run all tests│   ├── GITHUB_TOPICS.mdFor detailed contribution guidelines, see [CONTRIBUTING.md](docs/CONTRIBUTING.md).

python -m pytest tests/

│   └── GITHUB_CLEANUP_SUMMARY.md

# Run specific test

python tests/test_ogle_phases.py│---



# Run with verbose output├── src/strategy/                  # Source code

python tests/final_validation.py --verbose

```│   └── sunrise_ogle_xauusd.py    # Main strategy (3200+ lines)## 📜 License



---│



## 📊 Performance Metrics Explained├── tests/                         # Test files (10 files)This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



### Profit Factor (1.64)└── temp_reports/                  # Gitignored - Generated reports

- **Definition**: Gross Profit / Absolute Gross Loss

- **Interpretation**: For every $1 lost, strategy earns $1.64```---

- **Industry Standard**: >1.5 is considered good, >2.0 is excellent

- **Rating**: ✅ **GOOD** - Demonstrates consistent edge



### Win Rate (55.43%)---## ⚠️ Disclaimer

- **Definition**: Winning Trades / Total Trades

- **Interpretation**: More than half of all trades are profitable

- **Combined with PF**: Indicates balanced win size vs. loss size

- **Rating**: ✅ **ABOVE BASELINE** - Sustainable win rate## 🚀 Getting StartedThis project is for educational and research purposes ONLY. It is not financial advice. Algorithmic trading involves substantial risk of loss and is not suitable for every investor. Past performance is not indicative of future results.



### Total Return (44.75%)### Prerequisites

- **Period**: 5 years (July 2020 - July 2025)- Python 3.8 or newer

- **Annualized**: ~8.95% per year- Git version control

- **Compounding**: Not reinvested (fixed position sizing)

- **Rating**: ✅ **SOLID** - Conservative, consistent returns### 1. Clone the Repository

```bash

### Risk Metricsgit clone https://github.com/YOUR_USERNAME/backtrader-pullback-window-xauusd.git

- **Max Drawdown**: *Pending full analyzer run*cd backtrader-pullback-window-xauusd

- **Sharpe Ratio**: *Pending full analyzer run*```

- **Expectancy**: Positive (calculated from PF and WR)

### 2. Set Up Virtual Environment

---```bash

python -m venv venv

## 🔒 Risk Disclaimer

# Windows:

**IMPORTANT: This software is for educational and research purposes only.**venv\Scripts\activate



- ⚠️ Past performance does not guarantee future results# macOS/Linux:

- ⚠️ Trading Gold (XAU/USD) involves significant risk of losssource venv/bin/activate

- ⚠️ Only trade with capital you can afford to lose```

- ⚠️ Backtest results may not reflect real trading conditions

- ⚠️ Slippage, spreads, and commissions affect real performance### 3. Install Dependencies

- ⚠️ Test thoroughly on demo accounts before live trading```bash

- ⚠️ The authors assume no liability for trading lossespip install -r requirements.txt

```

**Always:**

- Start with paper trading### 4. Run the Strategy

- Use proper risk management```bash

- Understand the strategy completely before tradingpython src/strategy/sunrise_ogle_xauusd.py

- Consult with financial advisors```

- Comply with local regulations

**Expected Output:**

---```

=== SUNRISE OGLE === (from 2020-07-10 to 2025-07-25)

## 🤝 Contributing>> FOREX MODE ENABLED - Data: XAUUSD_5m_5Yea.csv

>> Instrument: XAUUSD (XAU/USD)

Contributions are welcome! Please see [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.📊 TRADE REPORT: temp_reports\XAUUSD_trades_YYYYMMDD_HHMMSS.txt

```

**Ways to contribute:**

- 🐛 Report bugs or issues---

- 💡 Suggest enhancements

- 📝 Improve documentation## 🔧 Customization

- 🧪 Add more tests

- 📊 Optimize parameters### Key Parameters

- 🎨 Create visualizations

```python

---# EMA Periods

ema_confirm_period = 1          # Fast confirmation EMA

## 📝 Licenseema_fast_period = 14            # Fast EMA

ema_medium_period = 18          # Medium EMA

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.ema_slow_period = 24            # Slow EMA



**Additional Terms:**# Pullback Settings

- No warranty providedlong_pullback_max_candles = 3   # LONG pullback depth

- Use at your own riskshort_pullback_max_candles = 3  # SHORT pullback depth

- Not financial advice

- Educational purposes only# Window Settings

long_entry_window_periods = 2   # LONG breakout window

---short_entry_window_periods = 2  # SHORT breakout window

window_offset_multiplier = 1.0  # Channel offset

## 📚 Resources & References

# Risk Management

### Backtrader Documentationlong_sl_atr_mult = 2.5          # Stop Loss: 2.5 × ATR

- [Official Docs](https://www.backtrader.com/docu/)long_tp_atr_mult = 12.0         # Take Profit: 12.0 × ATR

- [GitHub Repository](https://github.com/mementum/backtrader)```

- [Community Forum](https://community.backtrader.com/)

---

### Gold Trading Resources

- [Gold Market Hours](https://www.forex.com/en-us/trading-academy/courses/commodities/gold-market-hours/)## 🤝 Contributing

- [XAU/USD Specifications](https://www.dailyfx.com/xau-usd)

- [Gold Trading Strategies](https://www.investopedia.com/articles/active-trading/021715/how-trade-gold.asp)Contributions welcome! See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.



### Algorithmic Trading- 🐛 [Report a Bug](https://github.com/YOUR_USERNAME/backtrader-pullback-window-xauusd/issues)

- [Quantitative Trading](https://quantstart.com/)- 💡 [Request a Feature](https://github.com/YOUR_USERNAME/backtrader-pullback-window-xauusd/issues)

- [QuantConnect Learn](https://www.quantconnect.com/tutorials)- 📝 [Submit a Pull Request](https://github.com/YOUR_USERNAME/backtrader-pullback-window-xauusd/pulls)

- [Algorithmic Trading](https://www.algorithmictrading.net/)

---

---

## 📜 License

## 📞 Support & Contact

MIT License with comprehensive trading disclaimer. See [LICENSE](LICENSE).

### Getting Help

- 📖 Check the [documentation](docs/)---

- 🐛 [Open an issue](../../issues)

- 💬 [Start a discussion](../../discussions)## ⚠️ IMPORTANT DISCLAIMER

- 📧 Contact: [Your Email]

### **This software is for EDUCATIONAL and RESEARCH purposes ONLY.**

### Repository Information

- **Status**: Production-Ready ✅**CRITICAL WARNINGS:**

- **Last Updated**: October 11, 2025- ⚠️ This is **NOT** financial advice

- **Version**: 1.0.0- ⚠️ Past performance does **NOT** guarantee future results

- **Strategy Lines**: 3200+- ⚠️ Algorithmic trading involves **SUBSTANTIAL RISK** of loss

- ⚠️ You can lose **MORE** than your initial investment

---- ⚠️ Trading Gold (XAU/USD) is highly volatile and risky

- ⚠️ Only trade with money you can **afford to lose**

## 🏆 Acknowledgments

**Before Using:**

Built with:1. ✅ Understand the strategy completely

- [Backtrader](https://www.backtrader.com/) - Powerful Python backtesting framework2. ✅ Backtest thoroughly on your own data

- [NumPy](https://numpy.org/) - Numerical computing3. ✅ Paper trade for extended period

- [Matplotlib](https://matplotlib.org/) - Visualization4. ✅ Consult with licensed financial advisors

- [Pandas](https://pandas.pydata.org/) - Data analysis5. ✅ Start with very small position sizes



---**By using this software, you acknowledge you are solely responsible for your trading decisions.**



## 📈 Roadmap**Trade at your own risk.**



### Completed ✅---

- [x] 4-phase state machine implementation

- [x] Dynamic ATR-based risk management## 📚 Resources

- [x] Gold-specific contract sizing

- [x] Comprehensive testing suite- [Backtrader Documentation](https://www.backtrader.com/docu/)

- [x] 5-year backtest validation- [ATR Indicator](https://www.investopedia.com/terms/a/atr.asp)

- [x] Performance metrics analysis- [Gold Trading Basics](https://www.investopedia.com/articles/basics/09/precious-metals-gold-silver-platinum.asp)

- [x] Documentation and README

---

### Planned 🚀

- [ ] SHORT strategy optimization (currently disabled)**⭐ Star this repo if you find it useful!**

- [ ] Machine learning parameter optimization

- [ ] Real-time data feed integration*Last Updated: October 11, 2025*

- [ ] Live trading interface
- [ ] Advanced performance analytics dashboard
- [ ] Multi-timeframe analysis
- [ ] Additional asset support (Silver, Crude Oil)

---

**⭐ If you find this project useful, please consider giving it a star!**

**🔔 Watch this repository for updates and new features**

---

*Last Updated: October 11, 2025 | Version 1.0.0 | Production-Ready*
