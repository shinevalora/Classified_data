#_*_coding:UTF-8_*_
#创建于2019/4/25:15:52

import os
import logging
from glob import glob
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)-8s: %(message)s")


def merge_data(file):
    base_name = os.path.basename(file)  # 文件名
    # print('base_name:',base_name)
    logging.debug(f"获取文件名: {base_name}")
    with open(file) as f:
        content = f.read().replace('\n', '')
        content = f"\n>>{base_name[:-4]}\n{content}\n\n"
        # print('content:',content)

    _data.setdefault(base_name[8:15], "")  # 设置默认值，防止下一行代码出现KeyError错误
    # print('_data1:',_data)
    _data[base_name[8:15]] += content  # 向字典存入数据
    # print('_data2:',_data)
    logging.debug(f"数据存入 {base_name[0]} 标里")


if __name__ == '__main__':
    path1 = "./YX20190425-1_2019-04-25"  # 文件夹所在路径
    path2 = r"./data"  # 保存的文件路径的文件夹
    _data = {}  # 用来存放文件内容
    os.makedirs(path2, exist_ok=True)  # 创建保存文件的路径文件夹

    # 1. 找到文件
    file_list = glob(f"{path1}/*.seq")
    logging.info(f"找到文件{len(file_list)} 个")
    logging.debug(f"具体内容：{file_list} 个")

    # 2. 分类合并
    [merge_data(file) for file in file_list]

    # 3. 保存到文件
    for k, v in _data.items():
        # print(k)
        _path = os.path.join(path2, f"{k}.txt")
        # print('_path:',_path)
        with open(_path, "w") as f:
            f.write(v)
        logging.debug(f" {k} 标的数据 已保存到 {_path}")

    logging.info(f"合并后的 {len(_data)} 组数据， 已经全部保存到 {path2} 文件夹中，")




