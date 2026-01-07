import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)

# Read Excel file
df = pd.read_excel('ReportHistory-100693856.xlsx', skiprows=6)
df.columns = ['Time_Open', 'Ticket', 'Symbol', 'Type', 'Volume', 'Price_Open', 
              'SL', 'TP', 'Time_Close', 'Price_Close', 'Commission', 'Swap', 'Profit', 'Extra']

# Filter valid trades
df = df[df['Ticket'].notna()]
df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')

print('=' * 80)
print('COMPREHENSIVE TRADE ANALYSIS')
print('=' * 80)

print('\n=== OVERALL PERFORMANCE ===')
print(f'Total Trades: {len(df)}')
print(f'Total Profit/Loss: ${df["Profit"].sum():.2f}')
print(f'Winning Trades: {len(df[df["Profit"] > 0])} ({len(df[df["Profit"] > 0])/len(df)*100:.1f}%)')
print(f'Losing Trades: {len(df[df["Profit"] < 0])} ({len(df[df["Profit"] < 0])/len(df)*100:.1f}%)')
print(f'Break-even Trades: {len(df[df["Profit"] == 0])}')

print('\n=== PROFIT/LOSS STATISTICS ===')
wins = df[df['Profit'] > 0]['Profit']
losses = df[df['Profit'] < 0]['Profit']
if len(wins) > 0:
    print(f'Average Win: ${wins.mean():.2f}')
    print(f'Biggest Win: ${wins.max():.2f}')
    print(f'Total Wins: ${wins.sum():.2f}')
if len(losses) > 0:
    print(f'Average Loss: ${losses.mean():.2f}')
    print(f'Biggest Loss: ${losses.min():.2f}')
    print(f'Total Losses: ${losses.sum():.2f}')
if len(wins) > 0 and len(losses) > 0:
    print(f'Win/Loss Ratio: {abs(wins.mean() / losses.mean()):.2f}')
    print(f'Profit Factor: {abs(wins.sum() / losses.sum()):.3f}')

print('\n=== LOT SIZE ANALYSIS ===')
lot_analysis = df.groupby('Volume')['Profit'].agg(['count', 'sum', 'mean']).round(2)
lot_analysis.columns = ['Trades', 'Total P/L', 'Avg P/L']
print(lot_analysis)

print('\n=== TRADE TYPE ANALYSIS (BUY vs SELL) ===')
type_analysis = df.groupby('Type').apply(lambda x: pd.Series({
    'Trades': len(x),
    'Wins': len(x[x['Profit'] > 0]),
    'Losses': len(x[x['Profit'] < 0]),
    'Win%': len(x[x['Profit'] > 0])/len(x)*100 if len(x) > 0 else 0,
    'Total P/L': x['Profit'].sum(),
    'Avg P/L': x['Profit'].mean()
})).round(2)
print(type_analysis)

print('\n=== CHRONOLOGICAL TRADE HISTORY ===')
print(df[['Time_Open', 'Type', 'Volume', 'Price_Open', 'Price_Close', 'Profit']].to_string(index=False))

print('\n=== POSITION SIZING EVOLUTION ===')
print('Checking if position sizing improved over time...')
df_sorted = df.sort_values('Time_Open')
df_sorted['Trade_Num'] = range(1, len(df_sorted) + 1)
print(df_sorted[['Trade_Num', 'Time_Open', 'Volume', 'Profit']].to_string(index=False))

print('\n=== KEY FINDINGS ===')
print(f'1. Position sizing ranged from {df["Volume"].min():.2f} to {df["Volume"].max():.2f} lots')
print(f'2. Most common lot size: {df["Volume"].mode()[0]:.2f} lots ({len(df[df["Volume"] == df["Volume"].mode()[0]])} trades)')
print(f'3. Net P/L: ${df["Profit"].sum():.2f} from {len(df)} trades')
print(f'4. Account impact: {df["Profit"].sum() / 10000 * 100:.2f}% of initial $10,000')

if len(df[df['Type'] == 'buy']) > 0 and len(df[df['Type'] == 'buy'][df['Profit'] > 0]) == 0:
    print('⚠️  WARNING: ALL BUY TRADES LOST MONEY - BUY LOGIC IS BROKEN!')
