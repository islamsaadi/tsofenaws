mydic = {}
with open("Alice.txt", "r") as f:
        for line in f:
                for word in line.split():
                        c = mydic.get(word, 0)
                        if( c > 0):
                                mydic.update({word: c+1})
                        else:
                                mydic.update({word: 1})
fin_max_word_count = max(mydic, key=mydic.get)
print(fin_max_word_count, mydic[fin_max_word_count])
