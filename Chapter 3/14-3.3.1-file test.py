# file = open("data2.txt", "w")
# file.write("Sample file writing\n")
# file.write("This is line 2\n")
# file.close()

# text_lines = [
#     "Chapter 3\n",
#     "Sample text data file\n",
#     "This is the third line of text\n",
#     "The fourth line looks like this\n",
#     "Edit the file with any text editor\n"
# ]
# file = open("data.txt", "w")
# file.writelines(text_lines)
# file.close()

###
# 如果改变内容多次调用，会发现w操作是把原文件内容删除后完全重写
###




# 读取数据可以使用file.read(n)，其中n是读取的字符数目
# file = open("data.txt", "r")
# char = file.read(20)
# print(char)

# 也可以不写n直接读取整个文件
# file = open("data.txt", "r")
# all_data = file.read()
# print(all_data)

# 也可以使用file.readline(n)读取整行，n是行数，不填就是1行
# file = open("data.txt", "r")
# one_line = file.readline()
# print(one_line)

# 还可用file.readlines()直接读取所有的行
# 这个函数不是使用文本数据填充接受数据的变量，而是创建一个列表，每一行都是列表中的一项
# 打印列表数据的话，并不是文件中的样子，而是带换行字符'\n'的样子
# file = open("data.txt", "r")
# all_data = file.readlines()
# print(all_data)

# 对于file.readlines()方法，可以通过循环print来还原文本样式
# file = open("data.txt", "r")
# all_data = file.readlines()
# print("Lines: ", len(all_data))
# for line in all_data:
#     print(line.strip())     # 通过line.strip()方法删去行末的换行字符



