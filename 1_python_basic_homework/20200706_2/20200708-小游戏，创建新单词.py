#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao

word = input('Please input your word: ')
new_word = word[1:] + '-' + word[0] + 'y'
print('The created new word is: ' + new_word)