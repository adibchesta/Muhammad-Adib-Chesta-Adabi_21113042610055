from pathlib import Path

path = Path(__file__).parent / "text1.txt"
contents = path.read_text()

word_count = contents.lower().count("the")

print(f"Jumlah kata 'the': {word_count}")

word_count_space = contents.lower().count("the ")

print(f"Jumlah kata 'the ' dengan spasi: {word_count_space}")