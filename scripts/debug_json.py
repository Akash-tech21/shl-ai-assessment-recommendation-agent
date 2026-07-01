from pathlib import Path

path = Path("data/raw/shl_catalog.json")

text = path.read_text(encoding="utf-8", errors="replace")

pos = 197732

print("=" * 80)
print("Characters around the error:\n")
print(repr(text[pos-200:pos+200]))
print("=" * 80)

print("\nLines around the error:\n")

with open(path, "r", encoding="utf-8", errors="replace") as f:
    lines = f.readlines()

for i in range(4790, 4801):
    print(f"{i}: {repr(lines[i-1])}")