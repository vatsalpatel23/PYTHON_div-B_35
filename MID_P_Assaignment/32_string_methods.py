"""Program 2.8: common string methods."""
sentence = input("Enter a sentence: ")
print("Upper:", sentence.upper())
print("Lower:", sentence.lower())
print("Title:", sentence.title())
print("Stripped:", sentence.strip())
print("Words:", sentence.split())
print("Underscores:", sentence.replace(" ", "_"))
print("First 'a':", sentence.find("a"))
