words = ['one', 'two', 'three', 'four', 'five']

for word in range(words):
  del words[word]

print("Length of words: " + str(len(words)))