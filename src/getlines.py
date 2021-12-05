from inspect import stack

_importer = [frame for frame in stack() if "frozen importlib._bootstrap" not in frame.filename][1]
_day = _importer.filename.split("\\")[-1][:-3]

with open(f"inputs/{_day}", "r", encoding="utf-8") as f:
    _input = f.read()

lines = _input.splitlines()
