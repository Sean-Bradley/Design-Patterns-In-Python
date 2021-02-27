"A sample document to be used in the Prototype example"
import copy  # a python library useful for deep copying
from interface_prototype import IProtoType


class Document(IProtoType):
    "A Concrete Class"

    def __init__(self, name, l):
        self.name = name
        self.list = l

    def clone(self, mode):
        " This clone method uses different copy techniques "
        if mode == 1:
            # results in a 1 level shallow copy of the Document
            doc_list = self.list
        if mode == 2:
            # results in a 2 level shallow copy of the Document
            # since it also create new references for the 1st level list
            # elements aswell
            doc_list = self.list.copy()
        if mode == 3:
            # recursive deep copy. Slower but results in a new copy
            # where no sub elements are shared by reference
            doc_list = copy.deepcopy(self.list)

        return type(self)(
            self.name,  # a shallow copy is returned of the name property
            doc_list  # copy method decided by mode argument
        )

    def __str__(self):
        " Overriding the default __str__ method for our object."
        return f"{id(self)}\tname={self.name}\tlist={self.list}"
