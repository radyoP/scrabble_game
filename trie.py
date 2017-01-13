import time
import string
import random
import sys

class Trie():
    def __init__(self, words):
        self._end = "_end_"
        self.root = dict()
        for word in words:
            curr_dict = self.root
            for letter in word:
                curr_dict = curr_dict.setdefault(letter,{})
            curr_dict[self._end] = self._end

    def __contains__(self, item):
        curr_dict = self.root
        for letter in item:
            if letter in curr_dict:
                curr_dict = curr_dict[letter]
            else:
                return False
        else:
            if self._end in curr_dict:
                return True
            else:
                return False

    def __str__(self):
        return str(self.root)

if __name__ == "__main__":
    lowercase = string.ascii_lowercase
    words = list()
    for i in range(1000000):
        word = ""
        for i in range(random.randint(1,16)):
            word += random.choice(lowercase)
        words.append(word)
    print("Created list of 1 000 000 random words")
    #with open("wordsEn.txt", "r") as file:
    #    words = file.read().split()
    t_i1 = time.time()
    trie = Trie(words)
    t_i2 = time.time()

    t1 = time.time()
    is_li = 0
    is_tri = 0
    for i in range(10000):
        word = ""
        for i in range(10):
            word += random.choice(lowercase)
        if word in words:
            is_li += 1
    words = []
    t2 = time.time()
    for i in range(10000):
        word = ""
        for i in range(10):
            word += random.choice(lowercase)
        if word in trie:
            is_tri +=1
    t3 = time.time()
    is_ok = "OK" if is_li-is_tri else "NOT OK"
    print(is_li)
    print("Testing on 10k random words. List:",t2-t1,"s   Trie", t3-t2, "s    init time:", t_i2-t_i1, "s   test was:", is_ok)


