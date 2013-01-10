import json
from simplejson import JSONDecodeError

def to_json(data):
    try:
        data = json.loads(data)
    except JSONDecodeError:
        return None
    return data

mimetable = {
    'application/json' : to_json
}

def mimeloader(data, mimetype):
    if mimetype in mimetable:
        return mimetable[mimetype](data)
    return None
