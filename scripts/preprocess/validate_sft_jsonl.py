import json, sys
from pathlib import Path

path = Path(sys.argv[1])
required = {'id','category','input','output'}
for i, line in enumerate(path.read_text(encoding='utf-8').splitlines(), start=1):
    obj = json.loads(line)
    missing = required - set(obj)
    if missing:
        raise ValueError(f'Line {i} missing {missing}')
    if not isinstance(obj['output'], dict):
        raise ValueError(f'Line {i} output must be object')
print(f'Validated {i} examples from {path}')
