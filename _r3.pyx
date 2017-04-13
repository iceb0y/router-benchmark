cimport _cr3
from libc.stdlib cimport free

METHOD_GET = _cr3.METHOD_GET
METHOD_POST = _cr3.METHOD_POST
METHOD_PUT = _cr3.METHOD_PUT
METHOD_DELETE = _cr3.METHOD_DELETE
METHOD_PATCH = _cr3.METHOD_PATCH
METHOD_HEAD = _cr3.METHOD_HEAD
METHOD_OPTIONS = _cr3.METHOD_OPTIONS

cdef class R3Tree:
    cdef _cr3.node* root
    cdef list objects

    def __cinit__(self):
        self.root = _cr3.r3_tree_create(128)
        self.objects = list()

    def __dealloc__(self):
        _cr3.r3_tree_free(self.root)

    def insert_route(self, int method, bytes path, obj):
        _cr3.r3_tree_insert_routel(self.root, method, path, len(path), <void*>obj)
        self.objects.append(obj)

    def compile(self):
        cdef char* errstr
        if _cr3.r3_tree_compile(self.root, &errstr):
            err = <bytes>errstr
            free(errstr)
            raise Exception(err)

    def match_route(self, int method, bytes path):
        # TODO(iceboy): return match info
        cdef _cr3.match_entry* entry = _cr3.match_entry_createl(path, len(path))
        cdef _cr3.route* route
        try:
            entry.request_method = method
            route = _cr3.r3_tree_match_route(self.root, entry)
            if route:
                return <object>route.data
        finally:
            _cr3.match_entry_free(entry)
