"""
Run backtests for all timeframes using respective JSONL data files
"""
import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime

# Timeframe configurations
TIMEFRAMES = {
    '1m': {'file': 'XAU_1m_data.jsonl', 'compression': 1},
    '5m': {'file': 'XAU_5m_data.jsonl', 'compression': 5},
    '15m': {'file': 'XAU_15m_data.jsonl', 'compression': 15},
    '30m': {'file': 'XAU_30m_data.jsonl', 'compression': 30},
    '1h': {'file': 'XAU_1h_data.jsonl', 'compression': 60},
    '4h': {'file': 'XAU_4h_data.jsonl', 'compression': 240},
}

DATA_DIR = Path(__file__).parent / 'data'
RESULTS_DIR = Path(__file__).parent / 'backtest_results'
RESULTS_DIR.mkdir(exist_ok=True)

def convert_jsonl_to_csv(jsonl_file, csv_file):
    """Convert JSONL to CSV format for backtesting"""
    print(f"  Converting {jsonl_file.name}...")
    
    count = 0
    with open(jsonl_file, 'r') as f_in, open(csv_file, 'w') as f_out:
        f_out.write('Date,Time,Open,High,Low,Close,Volume\n')
        
        for line in f_in:
            try:
                data = json.loads(line.strip())
                dt_str = data['Date']
                date_part, time_part = dt_str.split(' ')
                date_formatted = date_part.replace('.', '')
                time_formatted = time_part + ':00'
                
                row = f"{date_formatted},{time_formatted},{data['Open']},{data['High']},{data['Low']},{data['Close']},{data['Volume']}\n"
                f_out.write(row)
                count += 1
            except Exception as e:
                continue
    
    print(f"    Converted {count:,} rows")
    return count

def get_date_range(csv_file):
    """Get first and last date from CSV file"""
    first_date = None
    last_date = None
    
    with open(csv_file, 'r') as f:
        lines = f.readlines()
        if len(lines) > 1:
            # First data line
            parts = lines[1].strip().split(',')
            first_date = parts[0]  # YYYYMMDD format
            
            # Last data line
            parts = lines[-1].strip().split(',')
            last_date = parts[0]
    
    # Convert YYYYMMDD to YYYY-MM-DD
    if first_date:
        first_date = f"{first_date[:4]}-{first_date[4:6]}-{first_date[6:8]}"
    if last_date:
        last_date = f"{last_date[:4]}-{last_date[4:6]}-{last_date[6:8]}"
    
    return first_date, last_date

def run_backtest(timeframe, csv_file, compression, from_date, to_date):
    """Run backtest for a specific timeframe"""
    print(f"\n{'='*60}")
    print(f"  BACKTEST: {timeframe.upper()} Timeframe")
    print(f"  Data: {csv_file.name}")
    print(f"  Period: {from_date} to {to_date}")
    print(f"{'='*60}")
    
    # Create a temporary config override script
    backtest_script = f'''
import sys
sys.path.insert(0, r"{Path(__file__).parent}")

# Override CONFIG before importing
import xauusd_trading_bot
xauusd_trading_bot.CONFIG['data_file'] = '{csv_file.name}'
xauusd_trading_bot.CONFIG['from_date'] = '{from_date}'
xauusd_trading_bot.CONFIG['to_date'] = '{to_date}'
xauusd_trading_bot.CONFIG['timeframe'] = '{timeframe.upper()}'

# Run backtest
bot = xauusd_trading_bot.XAUUSDTradingBot()
bot.setup_cerebro()
bot.run()
'''
    
    # Write temp script
    temp_script = Path(__file__).parent / f'_temp_backtest_{timeframe}.py'
    with open(temp_script, 'w', encoding='utf-8') as f:
        f.write(backtest_script)
    
    # Run backtest with UTF-8 encoding
    import os
    env = os.environ.copy()
    env['PYTHONIOENCODING'] = 'utf-8'
    
    result = subprocess.run(
        [sys.executable, str(temp_script)],
        capture_output=True,
        text=True,
        cwd=str(Path(__file__).parent),
        env=env,
        encoding='utf-8',
        errors='replace'
    )
    
    # Save output
    output_file = RESULTS_DIR / f'backtest_{timeframe}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"BACKTEST RESULTS - {timeframe.upper()} Timeframe\n")
        f.write(f"Period: {from_date} to {to_date}\n")
        f.write(f"Data File: {csv_file.name}\n")
        f.write("="*60 + "\n\n")
        f.write(result.stdout)
        if result.stderr:
            f.write("\n\nERRORS:\n")
            f.write(result.stderr)
    
    # Print summary from output
    print(result.stdout[-3000:] if len(result.stdout) > 3000 else result.stdout)
    
    # Cleanup temp script
    temp_script.unlink()
    
    print(f"\n  Results saved to: {output_file.name}")
    return output_file

def main():
    print("="*60)
    print("  MULTI-TIMEFRAME BACKTEST SUITE")
    print("  Running backtests for: 1m, 5m, 15m, 30m, 1h, 4h")
    print("="*60)
    
    results = {}
    
    for tf, config in TIMEFRAMES.items():
        jsonl_file = DATA_DIR / config['file']
        csv_file = DATA_DIR / f"XAU_{tf}_converted.csv"
        
        print(f"\n{'='*60}")
        print(f"  Processing {tf.upper()} timeframe...")
        print(f"{'='*60}")
        
        # Check if JSONL exists
        if not jsonl_file.exists():
            print(f"  ⚠️ SKIPPING: {jsonl_file.name} not found")
            continue
        
        # Convert JSONL to CSV
        row_count = convert_jsonl_to_csv(jsonl_file, csv_file)
        
        if row_count == 0:
            print(f"  ⚠️ SKIPPING: No data converted")
            continue
        
        # Get date range
        from_date, to_date = get_date_range(csv_file)
        print(f"  Date range: {from_date} to {to_date}")
        
        # Run backtest
        try:
            output_file = run_backtest(tf, csv_file, config['compression'], from_date, to_date)
            results[tf] = {'status': 'success', 'file': output_file}
        except Exception as e:
            print(f"  ❌ ERROR: {e}")
            results[tf] = {'status': 'error', 'error': str(e)}
    
    # Summary
    print("\n" + "="*60)
    print("  BACKTEST SUMMARY")
    print("="*60)
    for tf, result in results.items():
        status = "✅" if result['status'] == 'success' else "❌"
        print(f"  {status} {tf.upper()}: {result.get('file', result.get('error', 'Unknown'))}")
    print("="*60)

if __name__ == '__main__':
    main()
