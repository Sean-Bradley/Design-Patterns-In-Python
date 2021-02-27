"A File class"
from interface_component import IComponent


class File(IComponent):
    "The File Class. The files are leaves"

    def __init__(self, name):
        self.name = name

    def dir(self, indent):
        parent_id = (id(self.reference_to_parent)
                     if self.reference_to_parent is not None else None)
        print(
            f"{indent}<FILE> {self.name}\t\t"
            f"id:{id(self)}\tParent:\t{parent_id}"
        )

    def detach(self):
        "Detaching this file (leaf) from its parent composite"
        if self.reference_to_parent is not None:
            self.reference_to_parent.delete(self)
