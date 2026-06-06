# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()
#
# with open("my_file.txt") as f:
#     print(f.read())

with open("my_file.txt", mode="a") as f:
    f.write("\nDDDDDDDDD")

with open("my_file.txt") as f:
    print(f.read())

with open("my_file_1.txt", mode="a") as f:
    f.write("test")