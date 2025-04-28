from pymongo import MongoClient
client=MongoClient("mongodb+srv://db_slr:db_slr@cluster0.qkqgck3.mongodb.net/?retryWrites=true&w=majority")
db=client.get_database("SLR")
rec=db.ACTION

def getAll():
    return list(rec.find())

def get(x):
    return rec.find_one({'action':x})

def find(x):
    return rec.find({'action':{ "$regex": x }})

# for x in get("ย"):
#     print(x)
#print(action)
#print(rec.count_documents({}))
#print(rec.find_one({'action':'รัก'}))


