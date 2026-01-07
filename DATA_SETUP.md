# Data Files Setup Guide

## 📁 Large Data Files Notice

Due to GitHub's file size limitations, the large CSV data files are not included in this repository:

- `data/xauusd_M1.csv` (457.57 MB) - 1-minute Gold data
- `data/xauusd_M5.csv` (97.59 MB) - 5-minute Gold data

## 🔧 Setting Up Data Files

### Option 1: Use Included Sample Data
The repository includes `data/XAUUSD_5m_5Yea.csv` which contains 5 years of 5-minute Gold data for backtesting.

### Option 2: Download Your Own Data
1. Download Gold (XAU/USD) data from your broker or data provider
2. Place CSV files in the `data/` directory
3. Update the file path in the strategy configuration

### Option 3: Generate Sample Data
```python
# Create minimal test data
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate sample OHLCV data
dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='5T')
data = pd.DataFrame({
    'datetime': dates,
    'open': 2000 + np.random.randn(len(dates)).cumsum() * 0.1,
    'high': lambda x: x['open'] + np.random.rand(len(x)) * 2,
    'low': lambda x: x['open'] - np.random.rand(len(x)) * 2,
    'close': lambda x: x['open'] + np.random.randn(len(x)) * 0.5,
    'volume': np.random.randint(100, 1000, len(dates))
})

data.to_csv('data/sample_xauusd_5m.csv', index=False)
```

## 🚀 Running the Strategy

Once you have data files in place, run:
```bash
python src/strategy/sunrise_ogle_xauusd.py
```

The strategy will automatically detect available CSV files in the `data/` directory.