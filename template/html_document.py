"A HTML document concrete class of AbstractDocument"
from abstract_document import AbstractDocument


class HTMLDocument(AbstractDocument):
    "Prints out a HTML formatted document"
    @staticmethod
    def title(document):
        document["title"] = "New HTML Document"

    @staticmethod
    def text(document, text):
        "Putting multiple lines into there own p tags"
        lines = text.splitlines()
        markup = ""
        for line in lines:
            markup = markup + "    <p>" + f"{line}</p>\n"
        document["text"] = markup[:-1]

    @staticmethod
    def print(document):
        "overriding print to output with html tags"
        print("<html>")
        print("  <head>")
        for attribute in document:
            if attribute in ["title", "description", "author"]:
                print(
                    f"    <{attribute}>{document[attribute]}"
                    f"</{attribute}>"
                )
            if attribute == "background_colour":
                print("    <style>")
                print("      body {")
                print(
                    f"        background-color: "
                    f"{document[attribute]};")
                print("      }")
                print("    </style>")
        print("  </head>")
        print("  <body>")
        print(f"{document['text']}")
        print("  </body>")
        print("</html>")
