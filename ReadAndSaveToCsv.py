#读取文件夹下的文件名并保存为CSV From: https://www.jianshu.com/p/393f116b0d68
import os
import csv
import re
root_path = 'F:\\BaiduNetdiskDownload\\mini_Imagenet\\dataset\\train'

#
# # 将所有目录下的文件信息放到列表中
def get_Write_file_infos(path):
    # 文件信息列表
    file_infos_list = []
    # 遍历并写入文件信息
    for root, dirnames, filenames in os.walk(path):

        for filename in filenames:
            file_infos = {}
            dirname = root
            print(root)
            dirname = re.findall(r'[^\\ /:*?"<>|\r\n]+$',dirname)
            # 正则表达式来截取文件夹名称
            # 正则表达式还得学习
            filename1 = filename.split('.jpg')[0]
            file_infos["file"] = filename1
            file_infos["species"] = dirname
            
            # 将数据追加字典到列表中
            file_infos_list.append(file_infos)

   return file_infos_list

# 写入csv文件
def write_csv(file_infos_list):
    with open('1.csv', 'a+', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=['file', 'species'])
        csv_writer.writeheader()
        for each in file_infos_list:
            csv_writer.writerow(each)

# 主函数
def main():
    # 调用获取文件信息的函数
    file_infos_list = get_Write_file_infos(root_path)
    # 执行写入程序
    write_csv(file_infos_list)

# # 主程序入口
if __name__ == '__main__':

    main()
