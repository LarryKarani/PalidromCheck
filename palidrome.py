def palidrome_check(string):
	if not isinstance(string, str):

		print("please provide a valid input")

	else:
		reversed_string = ''.join(reversed(string))

		if reversed_string == string:
			return(string, "True")

		elif reversed_string != string:
			return(string, "False")