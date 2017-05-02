firstname = raw_input("What is your first name? ")				# get their first name
dateOfBirth = 0													# using 0 as a placeholder for DOB
print "Using the format mm/dd/YYYY, please tell us your birthday, %s:" %(firstname)
while dateOfBirth == 0:											# until they get the format correct, DOB will loop
	dateOfBirth = raw_input()									# entry for DOB
	dobLIST = dateOfBirth.split("/")							# splits the DOB using the "/"
	if len(dobLIST) != 3:										# wrong separator or number of entries will ask to repeat
		print "Please use the correct mm/dd/YYYY format."
		print "Try again:"
		dateOfBirth = 0											# resets loop
	else:
		counter = 0												# counter for birthday splits
		for num in dobLIST:										# conerts each birthday split into integer
			num = int(num)
			dobLIST[counter] = num
			counter += 1

		if dobLIST[0] > 12 or dobLIST[0] < 1:					# checks month
			print "You listed %s as your birth month." %(dobLIST[0])
			print "The birthday month [mm] must be 1-12."
			print "Do you need a birth month calculator? "
			monthCalculator = raw_input()
			monthCalculator = monthCalculator.upper()
			if monthCalculator == "YES" or monthCalculator == "Y":
				print "JAN - 1"
				print "FEB - 2"
				print "MAR - 3"
				print "APR - 4"
				print "MAY - 5"
				print "JUN - 6"
				print "JUL - 7"
				print "AUG - 8"
				print "SEP - 9"
				print "OCT - 10"
				print "NOV - 11"
				print "DEC - 12"
				print "Let's try again! Enter your correct DOB (mm/dd/YYYY):"
			else:
				print "Let's try again! Enter your correct DOB (mm/dd/YYYY):"
			dateOfBirth = 0
		else:
			if dobLIST[0] == 2 and (dobLIST[1] > 29 or dobLIST[1] < 1):
				print "You are indicating you that your birthday is in February. However, February only has 29 days."
				print "Let's try again! Enter your correct DOB (mm/dd/YYYY):"
				dateOfBirth = 0
			elif dobLIST[1] > 31 or dobLIST[1] < 1:
				print "There are only 31 days in each month."
				print "Let's try again! Enter your correct DOB (mm/dd/YYYY):"
				dateOfBirth = 0
			else:
				if dobLIST[2] > 2017:
					print "Sorry, you can't have been born in the future."
					print "Let's try again! Enter your correct DOB (mm/dd/YYYY):"
					dateOfBirth = 0
				elif dobLIST[2] < 1900:
					print "Sorry, but nobody who was born before the 20th century can use this."
					print "Let's try again! Ener your correct DOB (mm/dd/YYYY):"
					dateOfBirth = 0

dobDICTIONARY = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}



print "Great! We've got your birthday as %s %s, %s. Is this correct?" %(dobDICTIONARY[dobLIST[0]], dobLIST[1], dobLIST[2])
correctBDAY = raw_input()
if correctBDAY.upper == "YES":
	print "YAY!"
else:
	print "Let's try again!"

print dobLIST[2] % 4





