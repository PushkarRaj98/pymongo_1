import pymongo as p

if __name__=="__main__":
    print("welcome to pymongo ")
    client = p.MongoClient("mongodb://localhost:27017/")
    print("connected.......")
    db=client['harry'] 
    collection= db['sampleclollection']
    

    
    #dictionary = {'name': 'Harry', 'marks': 50}
    #collection.insert_one(dictionary)
   
    insertthese=[
        {'name': 'ram', 'location':'delhi', 'marks': 85 },
        {'name': 'sam', 'location':'chennai', 'marks': 98 },
        {'name': 'samar', 'location':'goa', 'marks': 38 },
        {'name': 'aman', 'location':'kolkata', 'marks': 65 }
    ]
    collection.insert_many(insertthese)


    