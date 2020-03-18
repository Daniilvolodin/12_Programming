keep_going=""
while keep_going=="":
    author=input("Author: ")
    if author == "":
        print("Author: Anonymous")
    else:
        print("Author: {}".format(author))
        author_store=author