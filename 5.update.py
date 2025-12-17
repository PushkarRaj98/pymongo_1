import pymongo as p

if __name__=="__main__":
    client= p.MongoClient("mongodb://localhost:27017/")
    print("connected----->",client)
    db=client['harry']
    collection=db['sampleclollection']

    prev={"name":"samar"}
    nextt={"$set": {"location":"Punjab"}}
    up=collection.update_many(prev,nextt) 
    print(up.modified_count)  