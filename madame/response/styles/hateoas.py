from .styles import ResponseStyle

class Hateoas(ResponseStyle):
    def root(self, data):
        content = {}
        if 'resource' in data:
            content = data['resource']
        if 'children' in data:
            content['links'] = data['children']
        return content

    def collection(self, data):
        return ''
