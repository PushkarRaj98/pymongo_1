import pymongo as p

if __name__=="__main__":
    print("welcome to pymongo ")
    client = p.MongoClient("mongodb://localhost:27017/")
    print("connected.......")
    db=client['harry'] 
    collection= db['sampleclollection']
    


    # one =collection.find_one ({'name':'sam'})
    # print(one)

    #there is no find many() so we have to find it manualy using loop 
    alldocs= collection.find({'name':'samar'},{'name': 1,'marks':1,'_id':0})
    for i in alldocs:
        print(i)         
        

