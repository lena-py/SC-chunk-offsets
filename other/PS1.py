__author__ = 'lena'
import os

# os.walk to traverse a directory tree
# returns a tuple
path = "/Users/lena/PycharmProjects/SC-chunk-offsets2/chunk_templates"

# for each tuple...
for root, dirs, files in os.walk(path):
    # print path/name for each file in the dir
    for name in files:
        print(os.path.join(root, name))
    # print subdirectory
    for name in dirs:
        print("*", os.path.join(root, name))

# Use os.walk to create a list of files
for root, subdirs, files in os.walk(path):
    newlist = [name for name in files if ".dat" in name]

print(newlist) # why is this yellow?


# Type coercion with formatting options
b = [b'0']
c = ("{!r}".format(b))
print(type(c))
print(type(b))


# Directory name
print(os.path.dirname("/Users/lena/PycharmProjects/SC-chunk-offsets2/other/Chunk_out.dat"))


# Get the file size
statinfo = os.stat("/Users/lena/PycharmProjects/SC-chunk-offsets2/Chunks.dat")
print(statinfo.st_size)


# Use seek to offset the current point of the file
with open("/Users/lena/PycharmProjects/SC-chunk-offsets2/Chunks.dat", 'rb') as f:
    print("eys")
    f.seek(786444)
    a = f.read(12)
    print(a)
