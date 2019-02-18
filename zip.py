# -*- coding: utf-8 -*-
import zipfile
import os


# 读取被压缩的文件夹
def read_zipfile():
    azip = zipfile.ZipFile('C:\\Users\\laoch\\Desktop\\weibo.zip', mode='r')
    # 返回所有文件夹和文件
    print(azip.namelist())
    # 返回该zip的文件名
    print(azip.filename)


# 生成新的压缩文件
def write_zipfile():
    # 新建压缩包，放文件进去,若压缩包已经存在，将覆盖。可选择用a模式，追加
    azip = zipfile.ZipFile('C:\\Users\\laoch\\Desktop\\weibo.zip', 'w')
    for current_path, subfolders, filesname in os.walk('C:\\Users\\laoch\\Desktop\\weibo'):
        # print(current_path, subfolders, filesname)
        #  filesname是一个列表，我们需要里面的每个文件名和当前路径组合
        for file in filesname:
            if '.json' in file:
                # 将当前路径与当前路径下的文件名组合，就是当前文件的绝对路径
                azip.write(os.path.join(current_path, file))
    # 关闭资源
    azip.close()



if __name__ == "__main__":
    write_zipfile()