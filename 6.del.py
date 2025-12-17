import pymongo as p

if __name__=="__main__":
    client= p.MongoClient("mongodb://localhost:27017/")
    db=client['harry']
    collection=db['sampleclollection']

    dele={"name":"samar"}
    
    collection.delete_one(dele) 