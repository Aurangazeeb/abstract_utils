import string
import time
alphabets = (','.join(string.ascii_lowercase)).split(',')

#action
def some_action(alphabets):
	for alphabet in alphabets:
		time.sleep(1)
		print('Letter is : ', alphabet)

#adding state logic - python decorator/annotator
def recall_state(func):
	with open('memory.txt') as memory:
		current_pos = memory.read()
	def recalled_func(sequences):
		

if __name__ == '__main__':
	some_action(alphabets)