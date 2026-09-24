import re
with open('explorer-ctrlq-new-folder.wh.cpp', 'r', encoding='utf-8') as f:
    code = f.read()

# Change setting IDs to force Windhawk to drop cached settings
code = code.replace('- modifier1:', '- mod1:')
code = code.replace('L"modifier1"', 'L"mod1"')

code = code.replace('- modifier2:', '- mod2:')
code = code.replace('L"modifier2"', 'L"mod2"')

code = code.replace('- hotkey:', '- hotkey_char:')
code = code.replace('L"hotkey"', 'L"hotkey_char"')

code = re.sub(
    r'(// @version\s+1\.)(\d+)\.(\d+)\.(\d+)',
    lambda m: f"{m.group(1)}4.8.9", 
    code
)

with open('explorer-ctrlq-new-folder.wh.cpp', 'w', encoding='utf-8') as f:
    f.write(code)
