import pymongo
import os
from dotenv import load_dotenv

load_dotenv()
mongo_db_password=os.environ.get("MONGODB_PASSWORD")

client=pymongo.MongoClient("mongodb+srv://sibims00:mongo_db_password@cluster0.fdy9vmg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db=client.sample_mflix
collection=db.movies
