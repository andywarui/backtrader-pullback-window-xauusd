"""
Convert M5 Gold Data to M30 Format
Resamples 5-minute candles to 30-minute candles for backtesting
"""

import pandas as pd
from datetime import datetime
from pathlib import Path

def convert_m5_to_m30(m5_file, m30_file, start_date='2020-07-10', end_date='2025-07-25'):
    """
    Convert M5 CSV to M30 CSV in Backtrader format

    Args:
        m5_file: Input M5 CSV file
        m30_file: Output M30 CSV file
        start_date: Filter start date (YYYY-MM-DD)
        end_date: Filter end date (YYYY-MM-DD)
    """

    print(f"Loading M5 data from: {m5_file}")

    # Read M5 data
    df = pd.read_csv(m5_file)

    print(f"  Total M5 rows: {len(df):,}")

    # Parse datetime
    df['datetime'] = pd.to_datetime(df['time'])

    # Filter date range
    start_dt = pd.to_datetime(start_date)
    end_dt = pd.to_datetime(end_date)

    df = df[(df['datetime'] >= start_dt) & (df['datetime'] <= end_dt)]

    print(f"  Filtered rows ({start_date} to {end_date}): {len(df):,}")

    if len(df) == 0:
        print(f"ERROR: No data in specified date range!")
        return False

    # Set datetime as index for resampling
    df.set_index('datetime', inplace=True)

    # Resample to 30-minute candles
    print(f"Resampling to M30 candles...")

    m30_df = df.resample('30T').agg({
        'open': 'first',    # First open in 30-min period
        'high': 'max',      # Highest high
        'low': 'min',       # Lowest low
        'close': 'last',    # Last close
        'volume': 'sum'     # Sum of volumes
    })

    # Drop rows with NaN (incomplete periods)
    m30_df = m30_df.dropna()

    print(f"  M30 candles generated: {len(m30_df):,}")

    # Prepare output in Backtrader format
    print(f"Converting to Backtrader CSV format...")

    output_rows = []
    for idx, row in m30_df.iterrows():
        date_str = idx.strftime('%Y%m%d')
        time_str = idx.strftime('%H:%M:%S')

        output_rows.append({
            'Date': date_str,
            'Time': time_str,
            'Open': f"{row['open']:.2f}",
            'High': f"{row['high']:.2f}",
            'Low': f"{row['low']:.2f}",
            'Close': f"{row['close']:.2f}",
            'Volume': int(row['volume'])
        })

    # Create output DataFrame
    output_df = pd.DataFrame(output_rows)

    # Save to CSV
    print(f"Saving to: {m30_file}")
    output_df.to_csv(m30_file, index=False)

    print(f"\n✅ SUCCESS!")
    print(f"   Input (M5):  {len(df):,} rows")
    print(f"   Output (M30): {len(output_df):,} rows")
    print(f"   Date Range:  {output_df['Date'].iloc[0]} to {output_df['Date'].iloc[-1]}")
    print(f"   Output File: {m30_file}")

    return True


if __name__ == '__main__':
    # Define paths
    data_dir = Path(__file__).parent / 'data'

    m5_file = data_dir / 'xauusd_M5.csv'
    m30_file = data_dir / 'XAUUSD_M30_2020-2025.csv'

    # Check if M5 file exists
    if not m5_file.exists():
        print(f"ERROR: M5 file not found: {m5_file}")
        exit(1)

    # Convert
    success = convert_m5_to_m30(
        m5_file=m5_file,
        m30_file=m30_file,
        start_date='2020-07-10',
        end_date='2025-07-25'
    )

    if success:
        print(f"\n🚀 You can now run the backtest:")
        print(f"   python xauusd_trading_bot.py --mode backtest")
    else:
        print(f"\n❌ Conversion failed")
