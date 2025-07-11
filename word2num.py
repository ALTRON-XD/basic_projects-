# turn string into number for eg 
# three hundred million = 300,000,000

# install word2number

from word2number import w2n
text = input("enter the number to be converted : ")
number = w2n.word_to_num(text)
print(number)
