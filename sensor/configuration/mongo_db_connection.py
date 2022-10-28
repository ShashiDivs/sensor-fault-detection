from http import client
import pymongo
import certifi
from sensor.constant.database import DATABASE_NAME

ca = certifi.where()


class MongoDBClient:
    client = None
    def __init__(self,database_name = DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = "mongodb://shashi:sasidiv@ac-qknzvyo-shard-00-00.xt5e03i.mongodb.net:27017,ac-qknzvyo-shard-00-01.xt5e03i.mongodb.net:27017,ac-qknzvyo-shard-00-02.xt5e03i.mongodb.net:27017/?ssl=true&replicaSet=atlas-qss8nw-shard-0&authSource=admin&retryWrites=true&w=majority"
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e