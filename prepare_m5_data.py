"""
Convert M5 CSV to Backtrader Format for Scalping Bot
Converts xauusd_M5.csv to XAUUSD_M5_2020-2025.csv in correct format
"""

import pandas as pd
from datetime import datetime
from pathlib import Path

def convert_m5_for_backtrader(input_file, output_file, start_date='2020-07-10', end_date='2025-07-25'):
    """Convert M5 CSV to Backtrader format"""

    print(f"Converting M5 data for scalping bot...")
    print(f"Input: {input_file}")
    print(f"Output: {output_file}")

    # Read M5 data
    df = pd.read_csv(input_file)
    print(f"Total rows: {len(df):,}")

    # Parse datetime
    df['datetime'] = pd.to_datetime(df['time'])

    # Filter date range
    start_dt = pd.to_datetime(start_date)
    end_dt = pd.to_datetime(end_date)
    df = df[(df['datetime'] >= start_dt) & (df['datetime'] <= end_dt)]

    print(f"Filtered ({start_date} to {end_date}): {len(df):,} rows")

    if len(df) == 0:
        print("ERROR: No data in date range!")
        return False

    # Convert to Backtrader CSV format
    print("Converting to Backtrader format...")

    output_rows = []
    for idx, row in df.iterrows():
        dt = row['datetime']
        date_str = dt.strftime('%Y%m%d')
        time_str = dt.strftime('%H:%M:%S')

        output_rows.append({
            'Date': date_str,
            'Time': time_str,
            'Open': f"{row['open']:.2f}",
            'High': f"{row['high']:.2f}",
            'Low': f"{row['low']:.2f}",
            'Close': f"{row['close']:.2f}",
            'Volume': int(row['volume'])
        })

        if len(output_rows) % 100000 == 0:
            print(f"  Processed {len(output_rows):,} rows...")

    # Save
    output_df = pd.DataFrame(output_rows)
    output_df.to_csv(output_file, index=False)

    print(f"\nSUCCESS!")
    print(f"Output rows: {len(output_df):,}")
    print(f"Date range: {output_df['Date'].iloc[0]} to {output_df['Date'].iloc[-1]}")
    print(f"File: {output_file}")

    return True


if __name__ == '__main__':
    data_dir = Path(__file__).parent / 'data'

    input_file = data_dir / 'xauusd_M5.csv'
    output_file = data_dir / 'XAUUSD_M5_2020-2025.csv'

    if not input_file.exists():
        print(f"ERROR: Input file not found: {input_file}")
        exit(1)

    success = convert_m5_for_backtrader(
        input_file=input_file,
        output_file=output_file,
        start_date='2020-07-10',
        end_date='2025-07-25'
    )

    if success:
        print(f"\n>>> Ready for scalping! Run:")
        print(f"    python xauusd_trading_bot.py --mode backtest")
    else:
        print(f"\nFailed to convert")
