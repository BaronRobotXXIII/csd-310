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

john = {
    "student_ID": 1010,
    "first_name": "John",
    "last_name": "Doe"
}

john_doc_id = db.students.insert_one(john).inserted_id

print("-- INSERT STATEMENTS --")
print(f"Inserted student record into the students collection with document_id {john_doc_id}")
print()

doc = db.students.find_one({'student_ID': 1010})

print("-- DISPLAYING STUDENT TEST DOC --")

print(f"Student ID: {doc['student_ID']}")
print(f"First Name: {doc['first_name']}")
print(f"Last Name: {doc['last_name']}")
print()

db.students.delete_one({'student_ID': 1010})

docs = db.students.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    print(f"Student ID: {doc['student_ID']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}")
    print()