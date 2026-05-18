import os
import uuid
from datetime import datetime, timezone

try:
    from pymongo import MongoClient
    from pymongo.errors import PyMongoError
except ImportError:  # pragma: no cover - exercised when dependency is absent locally.
    MongoClient = None
    PyMongoError = Exception


def new_guest_user_id():
    return f"guest-{uuid.uuid4().hex}"


class NullFeedbackStore:
    def save_feedback_event(self, **event):
        return False


class MongoFeedbackStore:
    def __init__(self, uri=None, db_name=None):
        self.uri = uri or os.environ.get("MONGODB_URI")
        self.db_name = db_name or os.environ.get("MONGODB_DB", "pulsescape")
        self.client = None
        self.collection = None

        if not self.uri or MongoClient is None:
            return

        self.client = MongoClient(self.uri, serverSelectionTimeoutMS=3000, connect=False)
        self.collection = self.client[self.db_name]["feedback"]

    def save_feedback_event(self, **event):
        if self.collection is None:
            return False

        document = dict(event)
        document["created_at"] = datetime.now(timezone.utc)

        try:
            self.collection.insert_one(document)
        except PyMongoError:
            return False
        return True


def create_feedback_store():
    if not os.environ.get("MONGODB_URI"):
        return NullFeedbackStore()
    return MongoFeedbackStore()
