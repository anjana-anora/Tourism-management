from pymongo import MongoClient

connection = MongoClient()

PACKAGES = connection['trip']['packages']
PASSENGERS = connection['trip']['passengers']