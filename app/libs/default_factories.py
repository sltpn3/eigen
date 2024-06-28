from datetime import datetime
import uuid

def current_time():
    return datetime.now()

def generate_uuid():
    return uuid.uuid4().hex