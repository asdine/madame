import datetime
import json
from bson.objectid import ObjectId

class APIEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.ctime()
        elif isinstance(obj, datetime.time):
            return obj.isoformat()
        elif isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


def jsonify(data):
    return json.dumps(data, cls=APIEncoder)

def send_json(obj):
    return jsonify(obj)

