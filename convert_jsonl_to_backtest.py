"""Convert JSONL data to CSV format for backtesting"""
import json
from pathlib import Path

# Read JSONL and convert to CSV
input_file = Path(r'D:\goldbot\backtrader-pullback-window-xauusd\data\XAU_5m_data.jsonl')
output_file = Path(r'D:\goldbot\backtrader-pullback-window-xauusd\data\XAU_5m_converted.csv')

print(f'Converting {input_file.name}...')

with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    # Write header
    f_out.write('Date,Time,Open,High,Low,Close,Volume\n')
    
    count = 0
    for line in f_in:
        data = json.loads(line.strip())
        # Parse date: '2004.06.11 07:15' -> 20040611,07:15:00
        dt_str = data['Date']
        date_part, time_part = dt_str.split(' ')
        # Convert 2004.06.11 to 20040611
        date_formatted = date_part.replace('.', '')
        # Add seconds to time
        time_formatted = time_part + ':00'
        
        row = f"{date_formatted},{time_formatted},{data['Open']},{data['High']},{data['Low']},{data['Close']},{data['Volume']}\n"
        f_out.write(row)
        count += 1
        if count % 100000 == 0:
            print(f'  Processed {count:,} rows...')

print(f'Done! Converted {count:,} rows to {output_file.name}')
