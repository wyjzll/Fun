# 版权声明：本文为CSDN博主「北木.」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_43283397/article/details/104253462
# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————
import os
def listdir(path, list_name):  # 传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        else:
            list_name.append(file_path)
 
list_name=[]
path='D:/PythonProject/data/'   #文件夹路径
listdir(path,list_name)
print(list_name)
 
with open('./list.txt','w') as f:     #要存入的txt
    write=''
    for i in list_name:
        write=write+str(i)+'\n'
    f.write(write)
