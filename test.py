import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

print(sys.argv)
print(sys.argv[0])
print(sys.argv[1])

if len(sys.argv)<4 :
	print('Some arguments are missing.')
	print('Please provide word, start date, end date and, if you wish, language (polish default).')
else:
	word = sys.argv[1]
	start_date = sys.argv[2]
	end_date = sys.argv[3]
	language = sys.argv[4]