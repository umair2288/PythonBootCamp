my_list = [1,2,3,4,5]
new_list = [ n*2 for n in my_list ]
print(new_list)


my_list = [1,2,3,4,5]
new_list = [ n*2 for n in my_list if n % 2 == 0  ]
print(new_list)



my_list = [1,2,3,4,5, 6]
new_list = [ n*2 for n in my_list if (n % 2 == 0) and (n % 3 == 0)]
print(new_list)

#find only word which has vowels

vowels = "aeiou"

text = "Apple is a good fruit"

words_with_vowels = [ word for word in text.lower().split() if "a" in word or  "e" in word or "i" in word ]

print(words_with_vowels)


my_list = [1,2,3,4,5, 6]
new_list = [ n*2 if (n % 2 == 0) and (n % 3 == 0) else n  for n in my_list ]
print(new_list)

