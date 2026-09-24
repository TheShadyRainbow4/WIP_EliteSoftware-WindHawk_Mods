import re
with open('explorer-ctrlq-new-folder.wh.cpp', 'r', encoding='utf-8') as f:
    code = f.read()

for i in range(10):
    code = code.replace(f"- {i}: {i}", f"- '{i}': '{i}'")

with open('explorer-ctrlq-new-folder.wh.cpp', 'w', encoding='utf-8') as f:
    f.write(code)
