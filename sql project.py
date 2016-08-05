import wikipedia as w
import csv 
import sqlite3

con = sqlite3.connect('turtleDatabase.db')
c = con.cursor()

data_in = open('turtleKeys.csv', 'r')
data_reader = csv.reader(data_in)

column_headers = data_reader.next()

def menu():
	print('Welcome to the Turtle Database \n')
	print(w.summary('Turtles', sentences=5 ))
	print('\n You can learn about turtles from our database. Some queries have already been listed for you. \n')
	print('1. Turtle Species Sizes')
	print('2. Trap Types in Ponds')
	print('3. Age and Amount of Captures')
	print('4. Quit \n')
	choice(int(input('To choose an option, enter the number that it corresponds with. \n ')))

def choice(x):
	while x != 4:
		if x == 1:
			query1()
		elif x == 2:
			query2()
		elif x == 3:
			query3()
		else:
			print("Choose a valid option!")
			choice(int(input('To choose an option, enter the number that it corresponds with. \n ')))
		choice(int(input('To choose an option, enter the number that it corresponds with. \n ')))
	if x == 4:
		print("Thank you for using the Turtle Database! Goodbye.")
		quit()

def query1():
	choice1 = c.execute("SELECT Profile.Species, AVG(Size.Carapace_L) FROM BigTable JOIN Profile JOIN Size ON BigTable.Profile_ID = Profile.Profile_ID and BigTable.Size_ID = Size.Size_ID GROUP BY Profile.Species")   
	query1 = []
	for row in choice1:
		name, size = row
		query1.append([name.encode('ascii'), size])	

	
	for row in query1:
		print('The species '+row[0]+' has an average carapace length of '+str(row[1]))
	

def query2():
	choice2 = c.execute("SELECT DISTINCT Pond.Pond_Loc, Capture.Trap_Type FROM BigTable JOIN Pond JOIN Capture ON BigTable.Loc_ID = Pond.Loc_ID AND BigTable.Cap_ID = Capture.Cap_ID")
	
	query2 = []
	for row in choice2:
		loc, cap = row
		query2.append([loc.encode('ascii'), cap])	

	for row in query2:
		print('In the location: '+row[0]+' scientists used '+row[1])

def query3():
	choice3 = c.execute("SELECT BigTable.Turtle, Profile.Age, Capture.New_Recap FROM BigTable JOIN Profile JOIN Capture ON BigTable.Profile_ID = Profile.Profile_ID AND BigTable.Cap_ID = Capture.Cap_ID")
	
	query3 = []
	for row in choice3:
		name, age, cap = row
		query3.append([name.encode('ascii'), age, cap])	
	
	for row in query3:
		if row[2] == 'N':
			print('The turtle '+row[0]+' at age '+row[1]+' was newly captured.')
		if row[2] == 'R':
			print('The turtle '+row[0]+' at age '+row[1]+' was recapture.')


menu()

con.commit()
con.close()
data_in.close()

