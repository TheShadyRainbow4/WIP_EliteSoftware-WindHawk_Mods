import re
with open('explorer-ctrlq-new-folder.wh.cpp', 'r', encoding='utf-8') as f:
    code = f.read()

# I will rewrite the settings block and GetModifierVK / GetHotkeyVK
new_settings = """// ==WindhawkModSettings==
/*
- modifier1: ctrl
  $name: First Modifier
  $description: Primary modifier key
  $options:
  - ctrl: Ctrl
  - shift: Shift
  - alt: Alt
  - win: Windows Key
- modifier2: none
  $name: Second Modifier (Optional)
  $description: Secondary modifier key
  $options:
  - none: None
  - ctrl: Ctrl
  - shift: Shift
  - alt: Alt
  - win: Windows Key
- hotkey: q
  $name: Hotkey Character
  $description: The letter or character for the hotkey
  $options:"""

for i in range(ord('a'), ord('z')+1):
    c = chr(i)
    upper_c = c.upper()
    new_settings += f'\n  - {c}: {upper_c}'
for i in range(ord('0'), ord('9')+1):
    c = chr(i)
    new_settings += f"\n  - '{c}': '{c}'"

symbols = [
    ("comma", '", (Comma)"'),
    ("slash", '"/ (Slash)"'),
    ("semicolon", '"; (Semicolon)"'),
    ("quote", '"\' (Quote)"'),
    ("lbracket", '"[ (Left Bracket)"'),
    ("rbracket", '"] (Right Bracket)"'),
    ("backslash", '"\\\\ (Backslash)"'),
    ("minus", '"- (Minus)"'),
    ("equals", '"= (Equals)"'),
    ("backtick", '"` (Backtick)"'),
    ("multiply", '"* (Multiply)"')
]
for k, v in symbols:
    new_settings += f'\n  - {k}: {v}'

new_settings += """
- folderName: New folder
  $name: Default Folder Name
  $description: The default name for the new folder
*/
// ==/WindhawkModSettings=="""

code = re.sub(r'// ==WindhawkModSettings==.*?// ==/WindhawkModSettings==', new_settings, code, flags=re.DOTALL)

# Update GetModifierVK
get_mod = """static int GetModifierVK(const std::wstring& modStr) {
    if (modStr == L"ctrl") return VK_CONTROL;
    if (modStr == L"shift") return VK_SHIFT;
    if (modStr == L"alt") return VK_MENU;
    if (modStr == L"win") return VK_LWIN;
    return 0;
}"""
code = re.sub(r'static int GetModifierVK.*?return 0;\n\}', get_mod, code, flags=re.DOTALL)

# Update GetHotkeyVK
get_hotkey = """static int GetHotkeyVK(const std::wstring& keyStr) {
    if (keyStr.empty()) return 'Q';
    
    if (keyStr.length() == 1) {
        wchar_t c = towupper(keyStr[0]);
        if (c >= L'A' && c <= L'Z') return c;
        if (c >= L'0' && c <= L'9') return c;
        switch (c) {
            case L',': return VK_OEM_COMMA;
            case L'/': return VK_OEM_2;
            case L';': return VK_OEM_1;
            case L'\\'': return VK_OEM_7;
            case L'[': return VK_OEM_4;
            case L']': return VK_OEM_6;
            case L'\\\\': return VK_OEM_5;
            case L'-': return VK_OEM_MINUS;
            case L'=': return VK_OEM_PLUS;
            case L'`': return VK_OEM_3;
            case L'*': return VK_MULTIPLY;
        }
    }
    
    if (keyStr == L"comma") return VK_OEM_COMMA;
    if (keyStr == L"slash") return VK_OEM_2;
    if (keyStr == L"semicolon") return VK_OEM_1;
    if (keyStr == L"quote") return VK_OEM_7;
    if (keyStr == L"lbracket") return VK_OEM_4;
    if (keyStr == L"rbracket") return VK_OEM_6;
    if (keyStr == L"backslash") return VK_OEM_5;
    if (keyStr == L"minus") return VK_OEM_MINUS;
    if (keyStr == L"equals") return VK_OEM_PLUS;
    if (keyStr == L"backtick") return VK_OEM_3;
    if (keyStr == L"multiply") return VK_MULTIPLY;
    
    return 'Q';
}"""
code = re.sub(r'static int GetHotkeyVK.*?return \'Q\';\n\}', get_hotkey, code, flags=re.DOTALL)

# Update LoadSettings default fallbacks
code = code.replace('L"Ctrl"', 'L"ctrl"').replace('L"None"', 'L"none"').replace('L"Q"', 'L"q"')

with open('explorer-ctrlq-new-folder.wh.cpp', 'w', encoding='utf-8') as f:
    f.write(code)
