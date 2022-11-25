#ex 1
"""
str1 = 'Hello my name is John'
words = str1.split()



temp = []
for word in words:
    temp.append(word + str(len(word)))
    print(temp)

str1_count = ' '.join(temp)
print(str1_count)
"""
#ex2
"""
#remove words with length equal 2
str1 = 'Hello my name is Bob'
words = str1.split()
for word in words:

    if len(word) == 2:

        words.remove(word)
print(words)
"""

#task3



l = ['spam', 'eggs', 'ham', 'bacon', 'spam', 'spam']


d = {}
for item in l:
    d[0::] = None

unique_key_list = list(d.keys())



print(unique_key_list) # dict_keys(['spam', 'eggs', 'ham', 'bacon'])

#{'a': 'bla', 'b': 'bla'}.keys() returns dict_keys(['a', 'b'])


