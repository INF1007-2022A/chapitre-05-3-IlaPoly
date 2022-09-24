#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	num = 0
	for char in text:
		if char.isalnum():
			num += 1
	return num

def get_word_length_histogram(text):
	histogram = [0]
	for words in text.split():
		while get_num_letters(words) > len(histogram):
			histogram += [0]
		if get_num_letters(words) <= len(histogram):
			i = get_num_letters(words) - 1
			histogram[i] += 1
	return histogram

def format_histogram(histogram):
	ROW_CHAR = "*"
	ROW = ''
	i = 1
	for element in histogram:
		if i < 10:
			ROW += ' ' + str(i) + ' ' + ROW_CHAR * element + '\n'
			i += 1
		else:
			ROW += str(i) + ' ' + ROW_CHAR * element + '\n'
			i += 1
	return ROW

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	HEIGHT = max(histogram)
	FINAL = ''
	for i in range(HEIGHT, -1, -1):
		FINAL += ''.join([BLOCK_CHAR if nb >= i + 1 else ' ' for nb in histogram[1:]]) + '\n'
	FINAL += LINE_CHAR * len(histogram)

	return FINAL


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))