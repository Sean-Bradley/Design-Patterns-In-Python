"A use case of the composite pattern."

from folder import Folder
from file import File

FILESYSTEM = Folder("root")
FILE_1 = File("abc.txt")
FILE_2 = File("123.txt")
FILESYSTEM.attach(FILE_1)
FILESYSTEM.attach(FILE_2)
FOLDER_A = Folder("folder_a")
FILESYSTEM.attach(FOLDER_A)
FILE_3 = File("xyz.txt")
FOLDER_A.attach(FILE_3)
FOLDER_B = Folder("folder_b")
FILE_4 = File("456.txt")
FOLDER_B.attach(FILE_4)
FILESYSTEM.attach(FOLDER_B)
FILESYSTEM.dir()

# now move FOLDER_A and its contents to FOLDER_B
print()
FOLDER_B.attach(FOLDER_A)
FILESYSTEM.dir()
