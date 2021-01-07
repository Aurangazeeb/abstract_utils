import string
import time
alphabets = (','.join(string.ascii_lowercase)).split(',')

if __name__ == '__main__':
	for alphabet in alphabets:
		time.sleep(1)
		print('Letter is : ', alphabet)