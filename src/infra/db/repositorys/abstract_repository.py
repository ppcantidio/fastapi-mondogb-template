from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

import pymongo
from bson import ObjectId

from config import settings


def validate_inputs(func):
    def validate(*args):
        print("testeee")
        variables_value_map = dict(zip(func.__code__.co_varnames, args))
        for key, value in func.__annotations__.items():
            assert isinstance(variables_value_map[key], value), "Invalid Attribute"
        return func(*args)

    return validate


class AbstractRepository(ABC):
    def __init__(self, collection_name: str, entity_class: dataclass) -> None:
        self.entity_class = entity_class
        self.collection = MongoCollection(collection=collection_name, entity_class=entity_class)

    def select_by_id(self, object_id: ObjectId) -> Any:
        where = {"_id": object_id}
        return self.collection.find_one(where=where)

    def select_with_pagination(self, where: dict, page: int, per_page: int) -> list:
        total_documents = self.collection.count_documents(where)
        start_index = (page - 1) * per_page

        documents = list(self.collection.find(where, start_index, per_page))
        if not documents:
            return [], None

        pagination_infos = self._create_pagination(page=page, per_page=per_page, total_documents=total_documents)
        return documents, pagination_infos

    def delete_by_id(self, id: ObjectId):
        where = {"_id": id}
        return self.collection.delete_one(where=where)

    def _create_pagination(self, total_documents, page, per_page):
        total_pages = (total_documents + per_page - 1) // per_page
        has_next_page = page < total_pages
        has_previous_page = page > 1
        pagination_infos = {
            "current_page": page,
            "next_page": page + 1 if has_next_page else None,
            "previous_page": page - 1 if has_previous_page else None,
            "total_pages": total_pages,
            "items_per_page": per_page,
            "total_items": total_documents,
        }
        return pagination_infos
