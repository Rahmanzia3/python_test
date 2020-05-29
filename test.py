import os
from argparse import ArgumentParser
import argparse

if __name__ == "__main__":
	# parser = ArgumentParser()
	# parser = argparse.ArgumentParser(description='Process some integers.')
	# parser.add_argument('--numbers', metavar='N',required=True, type=int, 
	# 	nargs='+',help='enter numbers you want to add')

	# opt = parser.parse_args()

	# numbers = opt.numbers

	# numbers = input("Enter a two value: ")


	numbers = list(map(int, input("Enter a multiple value: ").split())) 
	print(sum(numbers))
