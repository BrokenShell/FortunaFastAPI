from os import getenv
from pymongo import MongoClient


__all__ = ('DataBase',)


class DataBase:
    """ Data Model for Astrological Sign Prediction """

    def connect(self):
        """ Returns MongoDB connection handle """
        return MongoClient(
            f"mongodb+srv://{getenv('MONGODB_USER')}:{getenv('MONGODB_PASS')}"
            f"@{getenv('MONGODB_URI')}/test?retryWrites=true&w=majority"
        ).fortuna.numbers

    def query(self, obj: dict) -> dict:
        """ Returns datum from database """
        return next(self.connect().find(obj))

    def store(self, obj: dict) -> None:
        """ Puts datum in the database """
        db = self.connect()
        db.insert_many(obj)
