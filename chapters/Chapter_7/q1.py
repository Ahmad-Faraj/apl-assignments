1. Which Python module is included in the standard library for working with SQLite
1. SQLite databases are stored in memory only and cannot be written to a file. Answer = F
2. Using parameterized queries helps prevent SQL injection attacks. Answer = T
3. The rollback() method can undo uncommitted changes in a transaction. Answer = T
Answer = T
5. cursor.execute() always returns a list of results. Answer = F
Answer:
Problem 1:
import pymysql
connect = pymysql.connect(
host="localhost",
user="root",
password="your_password",
database="school"
)
cur = connect.cursor()
students = [("Ali", 85.5),("Sara", 92.0),("Mohamed",
rows = cur.fetchall()
for row in rows:
print(row)
Problem 2:
import pymysql
connect = pymysql.connect(
host="localhost",
user="root",
password="your_password",
database="school"
)
curson = connect.cursor()
name = input("Enter name: ")
grade = float(input("Enter grade: "))
for row in curson.fetchall():
print(row)
Problem 3:
import pymysql
connect = pymysql.connectect(
host="localhost",
user="root",
password="your_password",
database="school"
)
curson = connect.cursonsor()
try:
except Exception as e:
print("Error:", e)
print("Transaction rolled back!")
for row in curson.fetchall():
print(row)
Problem 4:
from sqlalchemy import create_engine, Column, Integer,
from sqlalchemy.orm import declarative_base,
Base = declarative_base()
class Student(Base):
__tablename__ = "students"
id = Column(Integer, primary_key=True)
name = Column(String(100))
grade = Column(Float)
def __repr__(self):
return f"Student(id={self.id},
name='{self.name}', grade={self.grade})"
engine =
Session = sessionmaker(bind=engine)
session = Session()
student1 = Student(name="Hassan", grade=88.5)
student2 = Student(name="Nada", grade=91.2)
students = session.query(Student).all()
for s in students:
print(s)