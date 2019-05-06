import os

local_folder = os.getcwd()
print(local_folder)

# 在当前文件夹创建一个名字为5的文件夹
folder = local_folder + "\\5"
file_all_path = folder + "\\abc.txt"

def createFile():
    # 创建一个可读文件
    file = open(file_all_path, "w+")  # w+ 可读可写可覆盖, r+ 可读可写不可覆盖
    print("the file name is: ", file.name)
    print("the file weather is closed: ", file.closed)
    print("the file access mode: ", file.mode)
    file.write("www.runoob.com!\nVery good sitee!\n")
    file.close()

    file = open(file_all_path, "r+")
    content = file.read(10)

    # 查找当前位置
    position = file.tell()
    print("the current position is", position)

    # 将指针再次重新定位到文件开头
    position = file.seek(0, 0)
    strs = file.read(10)
    print("the current str is ", strs)
    file.close()

if os.path.exists(folder):
    print("the folder is exists")
    createFile()
else:
    os.mkdir(folder)
    print("the folder created finished!")
    createFile()
