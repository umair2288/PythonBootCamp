# Write a program that takes a paragraph and prints a dictionary containing the frequency 
# of each word in a paragraph. 
# Print the top 5 most frequent words and largest word.
from collections import defaultdict


pragraph = '''In academic terms,,,, a text is anything that conveys a set of meanings to the person who examines it. You might have thought that texts were limited to written'''

pragraph = pragraph.lower()
pragraph = pragraph.replace(".", "")
pragraph = pragraph.replace(",", "")

count =  defaultdict(int)

for word in pragraph.split():
    count[word] += 1

print(count)

for abc in count:
    print(abc)
    print(count[abc])

