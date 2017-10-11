import palidrome as p

def test_palidrome_check():

	results = p.palidrome_check('racecar')

	assert results == ('racecar', "True")