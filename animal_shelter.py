from pymongo import MongoClient

class AnimalShelter(object):
    def __init__(self, username, password):
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30752
        DB ='aac'
        COL = 'animals'

        self.client = MongoClient(f'mongodb://{username}:{password}@{HOST}:{PORT}/{DB}?authSource=admin')
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data: dict):
        if data and isinstance(data, dict):
            result = self.collection.insert_one(data)
            return str(result.inserted_id)
        raise Exception("Nothing to save, data parameter is empty")

    def read(self, query: dict = None):
        if query is None: 
            query = {}
        if isinstance(query, dict):
            return list(self.collection.find(query, {"_id": 0}))
        raise Exception("Query parameter must be a dict")
            
    def update(self, query: dict, new_data: dict):
        if query and new_data and isinstance(query, dict) and isinstance(new_data, dict):
            result = self.collection.update_many(query, {"$set": new_data})
            return result.modified_count
        raise Exception("Update failed: query or new data is empty or invalid")

    def delete(self, query):
        if query and isinstance(query, dict):
            result = self.collection.delete_many(query)
            return result.deleted_count 
        raise Exception("Delete failed: query is empty or invalid")