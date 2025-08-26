from pymongo import MongoClient

Mongo_URI = "mongodb+srv://prajapatiarjun2801:760097@cluster0.nkwapof.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(Mongo_URI)

db = client['Ride_Hailing_App_Kivy']  
try:
    print("MongoDb Connection To :- ", client.server_info()['version'])
except Exception as e:
    print('Problem occurred during MongoDB connection:', e)
