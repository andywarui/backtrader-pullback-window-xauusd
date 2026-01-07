"""
Fix encoding issues in Python files for Windows compatibility
Replaces emoji characters with ASCII equivalents
"""

import re

# Files to fix
files_to_fix = ['mt5_trader.py', 'xauusd_trading_bot.py']

# Replace emojis and unicode box drawing with ASCII equivalents
replacements = {
    '🔌': '[CONNECT]',
    '✅': '[OK]',
    '❌': '[ERROR]',
    '⚠️': '[WARNING]',
    '🚨': '[ALERT]',
    '📊': '[STATS]',
    '💰': '[MONEY]',
    '🛡️': '[SHIELD]',
    '📈': '[UP]',
    '📅': '[DATE]',
    '🎯': '[TARGET]',
    '═': '=',
    '║': '|',
    '╔': '+',
    '╗': '+',
    '╚': '+',
    '╝': '+',
    '💼': '[ACCOUNT]',
    '🟢': '[GREEN]',
    '🔴': '[RED]',
    '⏱️': '[TIMER]',
    '🚀': '[ROCKET]',
    '🤖': '[BOT]',
    '⏹️': '[STOP]',
}

for filename in files_to_fix:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        for emoji, ascii_char in replacements.items():
            content = content.replace(emoji, ascii_char)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"[OK] Fixed {filename}")

    except FileNotFoundError:
        print(f"[WARNING] Skipping {filename} (not found)")
    except Exception as e:
        print(f"[ERROR] Failed to fix {filename}: {e}")

print("\n[OK] Encoding fixed! Emojis replaced with ASCII characters.")
print("You can now run: python xauusd_trading_bot.py --mode mt5")
