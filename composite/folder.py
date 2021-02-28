"A Folder, that acts as a composite."
from interface_component import IComponent


class Folder(IComponent):
    "The Folder class can contain other folders and files"

    def __init__(self, name):
        self.name = name
        self.components = []

    def dir(self, indent=""):
        print(
            f"{indent}<DIR>  {self.name}\t\tid:{id(self)}\t"
            f"Components: {len(self.components)}")
        for component in self.components:
            component.dir(indent + "..")

    def attach(self, component):
        """
        Detach file/folder from any current parent reference
        and then set the parent reference to this folder
        """
        component.detach()
        component.reference_to_parent = self
        self.components.append(component)

    def delete(self, component):
        """
        Removes file/folder from this folder so that self.components"
        is cleaned
        """
        self.components.remove(component)

    def detach(self):
        "Detaching this folder from its parent folder"
        if self.reference_to_parent is not None:
            self.reference_to_parent.delete(self)
            self.reference_to_parent = None
