thorin = {
    "first_name": "Thorin",
    "last_name": "Oakenshield",
    "student_ID": 1007
}
bilbo = {
    "first_name": "Bilbo",
    "last_name": "Baggins",
    "student_ID": 1008
}
frodo = {
    "first_name": "Frodo",
    "last_name": "Baggins",
    "student_ID": 1009
}

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.gp8u6ok.mongodb.net/test"
client = MongoClient(url)
db = client.pytech

print("-- INSERT STATEMENTS --")

thorin_doc_id = db.students.insert_one(thorin).inserted_id
print(f"Inserted student record Thorin Oakenshield into the students collection with document_id {thorin_doc_id}")

bilbo_doc_id = db.students.insert_one(bilbo).inserted_id
print(f"Inserted student record Bilbo Baggins into the students collection with document_id {bilbo_doc_id}")

frodo_doc_id = db.students.insert_one(frodo).inserted_id
print(f"Inserted student record Frodo Baggins into the students collection with document_id {frodo_doc_id}")

