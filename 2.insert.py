import pymongo as p

if __name__=="__main__":
    print("welcome to pymongo ")
    client = p.MongoClient("mongodb://localhost:27017/")
    print("connected.......")
    db=client['harry'] 
    collection= db['sampleclollection']
    # Insert one
    #dictionary = {'name': 'Harry', 'marks': 50}
    #collection.insert_one(dictionary)
    #insertmany
    # insertthese=[
    #     {'name': 'ram', 'location':'delhi', 'marks': 85 },
    #     {'name': 'sam', 'location':'chennai', 'marks': 98 },
    #     {'name': 'samar', 'location':'goa', 'marks': 38 },
    #     {'name': 'aman', 'location':'kolkata', 'marks': 65 }
    # ]
    # collection.insert_many(insertthese)
    
    #python gives it automatic _id, but  we can also give _id manually 
    insertthese=[
        {'_id':1,'name': 'ram', 'location':'delhi', 'marks': 85 },
        {'_id':2,'name': 'sam', 'location':'chennai', 'marks': 98 },
        {'_id':3,'name': 'samar', 'location':'goa', 'marks': 38 },
        {'_id':4,'name': 'aman', 'location':'kolkata', 'marks': 65 }
    ]
    collection.insert_many(insertthese)