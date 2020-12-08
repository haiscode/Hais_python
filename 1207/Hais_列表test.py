list  = ["周浩","刘爽","彭龙"]
# print(list[1])


list[1] = "张三"

print(list[1])


list.insert(1,"李四")



# 迭代遍历
for name in list:
    print("你的名字：%s" %name)



# 比较
def max(a , b):
    if a>b:
        print("a大")
    else:
        print("b大")


max(list[0],list[1])
