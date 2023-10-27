from bson import ObjectId
from pydantic import BaseModel

from src.utils.py_object_id import PyObjectId


class WithIdSchema(BaseModel):
    """
    Base schema to add PyObjectId at schemas
    """

    id: PyObjectId

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}
        arbitrary_types_allowed = True
