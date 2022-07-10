from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.gp8u6ok.mongodb.net/test"
client = MongoClient(url)
db = client.pytech

docs = db.students.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    print(f"Student ID: {doc['student_ID']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}")
    print()

result = db.students.update_one({'student_ID': 1007}, {'$set': {"last_name": "Oakenshield II"} })

print("--DISPLAYING STUDENT DOCUMENT 1007--")

doc = db.students.find_one({'student_ID': 1007})

print(f"Student ID: {doc['student_ID']}")
print(f"First Name: {doc['first_name']}")
print(f"Last Name: {doc['last_name']}")
print()