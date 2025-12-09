4. The output of re.findall(r"[aeiou]", "Python Programming") is:
6. The metacharacter ^ inside brackets [^...] means:
8. Which function is best for replacing substrings using regex?
1. re.match() scans the entire string for a pattern.
5. re.sub() can be used for both searching and replacing.
# import re
# from collections import Counter
# pattern = r"^[A-Za-z0-9._]+@[A-Za-z0-9.-
]+\.(com|org|edu)$"
# emails = ["user@example.com", "bad-email",
# valid = [email for email in emails if
# print(valid)
# Texts = "I love #Python and #AI"
# hashtags = re.findall(r"#\w+", Texts)
# print(hashtags)
# phones = ["+1-555-1234", "5551234", "123-456-7890"]
# pattern = r"^\+?\d{1,3}[-]?\d{3}[-]?\d{4}$"
# for p in phones:
# print(f"{p}: {bool(re.match(pattern, p))}")
# Str = "Python, Python! AI is great; Python AI."
# words = re.findall(r"\w+", Str)
# freq = dict(Counter(words))
# print(freq)
# Str = "This is is a test test"
# duplicates = re.findall(r"\b(\w+)\s+\1\b", Str)
# print([f"{w} {w}" for w in duplicates])
# event = "The events are on 2023-05-12 and 2024-01-01."
# pattern = r"\d{4}-\d{2}-\d{2}"
# event_dates = re.findall(pattern, event)
# print(event_dates)
# credit_Card = "Card: 1234-5678-9012-3456"
# masked_Card = re.sub(r"\d(?=[\d-]*\d{4})",
# print(masked_Card)
# Str = "I know Python, Java, and C++ but not Ruby."
# pattern =
# langs = re.findall(pattern,Str,re.IGNORECASE)
# print(langs)