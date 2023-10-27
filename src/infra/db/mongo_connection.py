class MongoConnection:
    client = pymongo.MongoClient(settings("mongodb-connection"))
    db = client.get_database(settings("MONGO_DB_NAME"))

    def __init__(self, collection, entity_class: dataclass):
        self.entity_class = entity_class
        self.__collection = self.db.get_collection(collection)

    def insert_one(self, document: Any) -> ObjectId:
        document_json = (document).asmongo()
        inserted_id = self.__collection.insert_one(document_json).inserted_id
        return inserted_id

    def find_one(self, where: dict) -> Any:
        document = self.__collection.find_one(where)
        return self.entity_class(**document) if isinstance(document, dict) else None

    def delete_one(self, where: dict):
        self.__collection.delete_one(where=where)

    def update_one(self, filter, update):
        self.__collection.update_one(filter=filter, update=update)

    def count_documents(self, where: dict):
        return self.__collection.count_documents(where)

    def find(self, where: dict, skip=None, limit=None) -> Any:
        documents = self.__collection.find(where)
        if skip:
            documents = documents.skip(skip)

        if limit:
            documents = documents.limit(limit)
        return [self.entity_class(**document) for document in documents]
