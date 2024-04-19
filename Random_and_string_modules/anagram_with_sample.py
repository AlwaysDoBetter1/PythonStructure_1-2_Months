'''
An anagram is a word formed by rearranging the letters that make up another word.
For example, the words saw and linden or post and stop are anagrams.

Write a program that reads one word and outputs its random anagram using the random module.
'''

from random import sample as S

anagram = input()

print(''.join(S(anagram, len(anagram))))
