word1 = ('Good')
word2 = ('Cheese')
word3 = ('Man')
Word4 = ('Spoon')

word1 = word1.replace ('oo', 'ooooo')
word2 = word2.replace ('ee', 'eeeee')
word3 = word3.replace ('a', 'aaaaa')
Word4 = Word4.replace ('oo', 'ooooo')

words = [word1, word2, word3, Word4]

for word in words:
    print(word)
