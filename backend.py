import sqlite3

def Create_db():
    connected = sqlite3.connect("book.db")
    cur = connected.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (Id INTEGER PRIMARY KEY, Title text, Author text, Year INTEGER, ISBN INTEGER)") 
    connected.commit()
    connected.close()

def ViewAll():
    connected = sqlite3.connect("book.db")
    cur = connected.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    connected.close()
    return rows

def Insert(Title, Author, Year, ISBN):
    connected = sqlite3.connect("book.db")
    cur = connected.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?) ", (Title, Author, Year, ISBN))
    connected.commit()
    connected.close()

def Search(Title = "", Author = "", Year = "", ISBN = ""):
    connected = sqlite3.connect("book.db")
    cur = connected.cursor()
    cur.execute("SELECT * FROM book WHERE Title = ? OR Author = ? OR Year = ? OR ISBN = ?", (Title, Author, Year, ISBN))
    rows = cur.fetchall()
    connected.close()
    return rows

def Update(Id,Title, Author, Year, ISBN):
    connected = sqlite3.connect("book.db")
    cur = connected.cursor()
    cur.execute("UPDATE book SET Title = ? , Author = ? , Year = ? , ISBN = ? WHERE Id = ?", (Title, Author, Year, ISBN, Id))
    connected.commit()
    connected.close()


def Delete(Id):
    connected = sqlite3.connect("book.db")
    cur = connected.cursor()
    cur.execute("DELETE FROM book WHERE Id = ?", (Id,))
    connected.commit()
    connected.close()




#def Search():
#Create_db()
#Insert("The Sea", "John Tablet", 1918, 9134567291)
#Insert("The Earth", "John Smith", 1988, 1343672915)
print(ViewAll())
#print(Update(3, 'The Ocean', 'Jane Doe', 1999, 546432345))
print(Search(Author="Jane Doe"))
#print(Delete(1))





