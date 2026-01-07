"""
Convert JSONL Gold Data to Backtrader CSV Format
Converts XAU_30m_data.jsonl to XAUUSD_M30_2020-2025.csv
"""

import json
import csv
from datetime import datetime
from pathlib import Path

def convert_jsonl_to_csv(jsonl_file, csv_file):
    """Convert JSONL format to Backtrader CSV format"""

    print(f"Converting {jsonl_file} to {csv_file}...")

    rows_written = 0
    errors = 0

    try:
        with open(jsonl_file, 'r', encoding='utf-8') as f_in, \
             open(csv_file, 'w', newline='', encoding='utf-8') as f_out:

            csv_writer = csv.writer(f_out)

            # Write header
            csv_writer.writerow(['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume'])

            for line_num, line in enumerate(f_in, 1):
                line = line.strip()
                if not line:
                    continue

                try:
                    # Try to parse as JSON
                    data = json.loads(line)

                    # Extract fields (adjust field names based on your JSON structure)
                    # Common field names: timestamp, time, datetime, date
                    # Common OHLCV names: open, high, low, close, volume

                    # Try different timestamp field names
                    timestamp = None
                    for ts_field in ['timestamp', 'time', 'datetime', 'date', 't']:
                        if ts_field in data:
                            timestamp = data[ts_field]
                            break

                    if timestamp is None:
                        print(f"Line {line_num}: No timestamp field found. Keys: {list(data.keys())[:5]}")
                        errors += 1
                        if errors <= 3:
                            print(f"  Sample data: {str(data)[:200]}")
                        continue

                    # Convert timestamp to datetime
                    if isinstance(timestamp, (int, float)):
                        # Unix timestamp (seconds or milliseconds)
                        if timestamp > 10000000000:  # Milliseconds
                            dt = datetime.fromtimestamp(timestamp / 1000)
                        else:  # Seconds
                            dt = datetime.fromtimestamp(timestamp)
                    elif isinstance(timestamp, str):
                        # String datetime - try common formats
                        for fmt in ['%Y-%m-%d %H:%M:%S', '%Y-%m-%dT%H:%M:%S',
                                   '%Y-%m-%d %H:%M:%S.%f', '%Y-%m-%dT%H:%M:%S.%f',
                                   '%Y/%m/%d %H:%M:%S']:
                            try:
                                dt = datetime.strptime(timestamp.split('.')[0].replace('T', ' '), '%Y-%m-%d %H:%M:%S')
                                break
                            except:
                                continue
                        else:
                            print(f"Line {line_num}: Could not parse timestamp: {timestamp}")
                            errors += 1
                            continue
                    else:
                        print(f"Line {line_num}: Unknown timestamp type: {type(timestamp)}")
                        errors += 1
                        continue

                    # Extract OHLCV data
                    try:
                        open_price = float(data.get('open', data.get('o', 0)))
                        high_price = float(data.get('high', data.get('h', 0)))
                        low_price = float(data.get('low', data.get('l', 0)))
                        close_price = float(data.get('close', data.get('c', 0)))
                        volume = float(data.get('volume', data.get('v', data.get('tick_volume', 1000))))
                    except (ValueError, TypeError) as e:
                        print(f"Line {line_num}: Error parsing OHLCV data: {e}")
                        errors += 1
                        continue

                    # Format for Backtrader
                    date_str = dt.strftime('%Y%m%d')
                    time_str = dt.strftime('%H:%M:%S')

                    # Write row
                    csv_writer.writerow([
                        date_str,
                        time_str,
                        f"{open_price:.2f}",
                        f"{high_price:.2f}",
                        f"{low_price:.2f}",
                        f"{close_price:.2f}",
                        int(volume)
                    ])

                    rows_written += 1

                    # Progress indicator
                    if rows_written % 10000 == 0:
                        print(f"  Processed {rows_written:,} rows...")

                except json.JSONDecodeError as e:
                    print(f"Line {line_num}: JSON decode error: {e}")
                    errors += 1
                    if errors <= 3:
                        print(f"  Line content: {line[:200]}")
                except Exception as e:
                    print(f"Line {line_num}: Unexpected error: {e}")
                    errors += 1

    except Exception as e:
        print(f"ERROR: Failed to open files: {e}")
        return False

    print(f"\nConversion complete!")
    print(f"  Rows written: {rows_written:,}")
    print(f"  Errors: {errors:,}")
    print(f"  Output file: {csv_file}")

    return rows_written > 0


if __name__ == '__main__':
    # Define paths
    data_dir = Path(__file__).parent / 'data'

    jsonl_file = data_dir / 'XAU_30m_data.jsonl'
    csv_file = data_dir / 'XAUUSD_M30_2020-2025.csv'

    # Check if JSONL file exists
    if not jsonl_file.exists():
        print(f"ERROR: Input file not found: {jsonl_file}")
        print("\nAvailable files in data directory:")
        for f in data_dir.glob('*'):
            print(f"  - {f.name}")
        exit(1)

    # Convert
    success = convert_jsonl_to_csv(jsonl_file, csv_file)

    if success:
        print(f"\n✅ SUCCESS! CSV file created: {csv_file}")
        print(f"\nYou can now run:")
        print(f"  python xauusd_trading_bot.py --mode backtest")
    else:
        print(f"\n❌ FAILED to convert data")
