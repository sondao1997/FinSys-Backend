import pymongo
import numpy

class FSDatabase: 
    def __init__(self):
        self.path = "mongodb+srv://dbAdmin:sapassword@finnsys-tjtha.mongodb.net/FinSys?retryWrites=true&w=majority"
        self.db = pymongo.MongoClient(self.path)
        self.dbContext = self.db["FinSys"] 

    def getCrrWithDate(self):
        list_crr_pair = []
        list_value_date = []
        settlement_date_context = self.dbContext["Settlement Date"]
        for row in settlement_date_context.find():
            list_crr_pair.append(row["crr_pair"])
            list_value_date.append(row["settlement_date"])
        list_Sdate = {"ccr_pair": list_crr_pair, "settlement_date": list_value_date} 
        return list_Sdate
        
if __name__ == "__main__":
    print(FSDatabase().getCrrWithDate())
        
