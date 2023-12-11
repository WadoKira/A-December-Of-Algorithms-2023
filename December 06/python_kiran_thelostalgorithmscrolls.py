# -*- coding: utf-8 -*-
"""python_kiran_TheLostAlgorithmScrolls.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18aJnLUNMEvEA-OFOEEC8t_4xJPoJZdPF
"""

from collections import deque
def find_word_chain(words):
    word_set = set(words)
    queue = deque([([], words[0])])
    while queue:
        path, current_word = queue.popleft()
        for next_word in word_set.copy():
            if is_one_letter_difference(current_word, next_word):
                new_path = path + [current_word]
                if next_word == words[-1]:
                    return new_path + [next_word]
                queue.append((new_path, next_word))
                word_set.remove(next_word)
    return None
def is_one_letter_difference(word1, word2):
    diff_count = sum(c1 != c2 for c1, c2 in zip(word1, word2))
    return diff_count == 1
string_list=input("Enter the strings separte by comma:")
encoded_words = string_list.split()
word_chain = find_word_chain(encoded_words)
if word_chain:
    print("Output:", word_chain)
else:
    print("No valid word chain found.")