import sqlite3

conn = sqlite3.connect("emaildb.sqlite")
cur = conn.cursor()

# Setup
cur.executescript('''
DROP TABLE IF EXISTS Count;
DROP TABLE IF EXISTS Counts;

CREATE TABLE Counts (
  org TEXT,
  count INTEGAR
) ;
''')

fname = input("Enter file name: ")
if len(fname) < 1 : fname = 'mbox.txt'
fhand = open(fname)
 
for line in fhand: 
  if not line.startswith("From:"): continue
  line = line.rstrip()
  pieces = line.split()
  email = pieces[1].split("@")
  org = email[1]

  cur.execute('''SELECT count FROM Counts WHERE org = ?''', (org, ))
  row = cur.fetchone()

  if row is None: 
    cur.execute('''INSERT INTO Counts (org, count)
      VALUES (? , 1)''', (org, ))
    
  else: 
    cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org, ))

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
  print(str(row[0]), row[1])

  conn.commit()
  