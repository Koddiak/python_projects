import sqlite3

with sqlite3.connect(':memory:') as connection:
	c = connection.cursor()
	c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
	c.executemany("INSERT INTO Roster VALUES (?, ?, ?)",
		      (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('Ak''not', 'Mangalore', -5)))
	c.execute("UPDATE Roster SET Species = 'Human' WHERE Name = 'Korben Dallas'")
	c.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
	for x in c.fetchall():
		print(x)
