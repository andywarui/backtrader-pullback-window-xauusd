import pandas as pd

# Read the Excel file carefully
df = pd.read_excel('ReportHistory-100693856.xlsx', skiprows=6)

# The actual trades section starts after headers
# Look for rows where Time_Open looks like a datetime
df.columns = ['Time_Open', 'Ticket', 'Symbol', 'Type', 'Volume', 'Price_Open', 
              'SL', 'TP', 'Time_Close', 'Price_Close', 'Commission', 'Swap', 'Profit', 'Extra']

# Filter only actual closed trades (with valid numeric profit)
df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')
df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce')
trades = df[(df['Profit'].notna()) & (df['Volume'].notna()) & (df['Volume'] > 0)].copy()

print('=' * 80)
print('XAUUSD TRADING BOT - PERFORMANCE ANALYSIS')
print('=' * 80)

print('\n📊 OVERALL STATS')
print(f'  Total Closed Trades: {len(trades)}')
print(f'  Net Profit/Loss: ${trades["Profit"].sum():.2f}')
print(f'  Account Impact: {trades["Profit"].sum() / 10000 * 100:.2f}% (from $10k start)')

print('\n✅ WIN/LOSS BREAKDOWN')
wins = trades[trades['Profit'] > 0]
losses = trades[trades['Profit'] < 0]
print(f'  Winners: {len(wins)} ({len(wins)/len(trades)*100:.1f}%)')
print(f'  Losers: {len(losses)} ({len(losses)/len(trades)*100:.1f}%)')

if len(wins) > 0:
    print(f'\n💰 WINNING TRADES')
    print(f'  Average Win: ${wins["Profit"].mean():.2f}')
    print(f'  Biggest Win: ${wins["Profit"].max():.2f}')
    print(f'  Total Win Amount: ${wins["Profit"].sum():.2f}')

if len(losses) > 0:
    print(f'\n💸 LOSING TRADES')
    print(f'  Average Loss: ${losses["Profit"].mean():.2f}')
    print(f'  Biggest Loss: ${losses["Profit"].min():.2f}')
    print(f'  Total Loss Amount: ${losses["Profit"].sum():.2f}')

if len(wins) > 0 and len(losses) > 0:
    print(f'\n📈 PERFORMANCE METRICS')
    print(f'  Profit Factor: {abs(wins["Profit"].sum() / losses["Profit"].sum()):.3f}')
    print(f'  Win/Loss Ratio: {abs(wins["Profit"].mean() / losses["Profit"].mean()):.2f}:1')

print(f'\n🎯 POSITION SIZING')
print(f'  Smallest lot: {trades["Volume"].min():.2f}')
print(f'  Largest lot: {trades["Volume"].max():.2f}')
print(f'  Average lot: {trades["Volume"].mean():.2f}')

print('\n📋 LOT SIZE PERFORMANCE')
lot_groups = trades.groupby('Volume').agg({
    'Profit': ['count', 'sum', 'mean']
}).round(2)
lot_groups.columns = ['Trades', 'Total P/L', 'Avg P/L']
print(lot_groups.sort_index())

print('\n🔄 BUY vs SELL PERFORMANCE')
buy_trades = trades[trades['Type'] == 'buy']
sell_trades = trades[trades['Type'] == 'sell']

if len(buy_trades) > 0:
    buy_wins = len(buy_trades[buy_trades['Profit'] > 0])
    print(f'  BUY: {len(buy_trades)} trades, {buy_wins} wins ({buy_wins/len(buy_trades)*100:.1f}%), P/L: ${buy_trades["Profit"].sum():.2f}')
if len(sell_trades) > 0:
    sell_wins = len(sell_trades[sell_trades['Profit'] > 0])
    print(f'  SELL: {len(sell_trades)} trades, {sell_wins} wins ({sell_wins/len(sell_trades)*100:.1f}%), P/L: ${sell_trades["Profit"].sum():.2f}')

print('\n📝 ALL CLOSED TRADES (Chronological)')
print('-' * 80)
for idx, row in trades.iterrows():
    result = '✅ WIN' if row['Profit'] > 0 else '❌ LOSS'
    print(f"{row['Time_Open']} | {row['Type']:4s} | {row['Volume']:.2f} lots | ${row['Profit']:8.2f} | {result}")

print('\n' + '=' * 80)
print('⚠️  CRITICAL ISSUES IDENTIFIED:')
print('=' * 80)

if len(buy_trades) > 0 and len(buy_trades[buy_trades['Profit'] > 0]) == 0:
    print('🔴 ALL BUY TRADES LOST MONEY - BUY ENTRY LOGIC IS BROKEN!')
    
if trades['Volume'].max() > 0.1:
    print(f'🔴 OVERSIZED POSITIONS: Max lot {trades["Volume"].max():.2f} risks ${trades["Volume"].max() * 100:.0f} per $1 move!')
    print(f'   For FTMO $10k account: Should use 0.01-0.02 lots maximum')

if len(losses) > 0 and abs(losses['Profit'].mean()) > 500:
    print(f'🔴 LARGE AVERAGE LOSS: ${losses["Profit"].mean():.2f} per losing trade is too big!')
    print(f'   FTMO requires max $500 daily loss (5% of $10k)')

net_pnl = trades['Profit'].sum()
if net_pnl < -1000:
    print(f'🔴 SIGNIFICANT DRAWDOWN: ${net_pnl:.2f} loss would fail FTMO challenge immediately')
    print(f'   FTMO max loss: $1,000 (10% of $10k)')

print('\n✅ RECOMMENDATIONS:')
print('  1. Fix BUY entry logic - investigate why all BUY trades fail')
print('  2. Reduce position sizing to 0.01-0.02 lots for FTMO compliance')
print('  3. Implement tighter stop losses (currently losing $600-1000 per trade)')
print('  4. Add daily loss limit of $500 (5% of account)')
print('  5. Add trailing stop at break-even when 50% to TP')
print('  6. Consider trading SELL signals only until BUY logic is fixed')
print('=' * 80)
