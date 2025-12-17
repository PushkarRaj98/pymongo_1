import pymongo as p

if __name__=="__main__":
    print("welcome to pymongo ")
    client = p.MongoClient("mongodb://localhost:27017/")
    print("connected.......",client)

    # #show dbs
    # alldbs=client.list_database_names()
    # print(alldbs)
    #show collections 
    collecti=client['harry']
    print(collecti.list_collection_names())