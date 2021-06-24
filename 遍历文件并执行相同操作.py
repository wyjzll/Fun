# 遍历文件并执行相同操作 do someting in the same folder

def read_directory(directory_name):
    for filename in os.listdir(directory_name):
        print(filename)  # 仅仅是为了测试
        img = cv2.imread(directory_name + "/" + filename,cv2.IMREAD_GRAYSCALE)
      #填入相同操作代码，举个例子比如删除黑色图片
        if cv2.countNonZero(img) == 0:
            print("Image is black")
            os.remove(directory_name + "/" + filename)
# main
if __name__ == '__main__':
   # read
read_directory("F:\BaiduNetdiskDownload\mini_Imagenet\dataset\\train\\n04296562")
