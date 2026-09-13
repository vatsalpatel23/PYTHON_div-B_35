"""Program 3.6: count words by frequency."""
paragraph = input("Enter a paragraph: ").lower()
counts = {}
for word in paragraph.replace(".", "").replace(",", "").split(): counts[word] = counts.get(word, 0) + 1
for word, count in sorted(counts.items(), key=lambda item: item[1], reverse=True): print(word + ":", count)
