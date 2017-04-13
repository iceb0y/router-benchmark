cdef extern from "r3/r3.h":
    cdef enum:
        METHOD_GET
        METHOD_POST
        METHOD_PUT
        METHOD_DELETE
        METHOD_PATCH
        METHOD_HEAD
        METHOD_OPTIONS

    ctypedef struct node

    ctypedef struct route:
        void* data

    ctypedef struct match_entry:
        int request_method

    node* r3_tree_create(int cap)
    void r3_tree_free(node* tree)
    route* r3_tree_insert_routel(node* tree, int method, const char* path, int path_len, void* data)
    int r3_tree_compile(node* n, char** errstr)
    route* r3_tree_match_route(const node* n, match_entry* entry)
    match_entry* match_entry_createl(const char* path, int path_len)
    void match_entry_free(match_entry* entry)
