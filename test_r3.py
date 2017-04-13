from _r3 import R3Tree, METHOD_GET, METHOD_POST, METHOD_PUT, METHOD_DELETE, METHOD_PATCH, METHOD_HEAD, METHOD_OPTIONS
from fixture import register

METHOD_DICT = {
    '*': METHOD_GET | METHOD_POST | METHOD_PUT | METHOD_DELETE | METHOD_PATCH | METHOD_HEAD | METHOD_OPTIONS,
    'GET': METHOD_GET,
    'POST': METHOD_POST,
    'PUT': METHOD_PUT,
    'DELETE': METHOD_DELETE,
    'PATCH': METHOD_PATCH,
    'HEAD': METHOD_HEAD,
    'OPTIONS': METHOD_OPTIONS,
}

tree = R3Tree()
register(lambda method, path, name: tree.insert_route(METHOD_DICT[method], path.encode(), name))
tree.compile()

for i in range(100000):
    tree.match_route(METHOD_GET, b'/d/twd2/records-conn/iframe.html')
