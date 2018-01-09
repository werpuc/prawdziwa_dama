import sys

if len(sys.argv)<4 :
	print('Some arguments are missing.')
	print('Please provide word, start date, end date and, if you wish, language (polish default).')
else:
	word = sys.argv[1]
	start_date = sys.argv[2]
	end_date = sys.argv[3]
	language = sys.argv[4]