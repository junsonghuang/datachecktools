# @Creater ：huangjunsong
# @File : Data_operation.py
# @Software : PyCharm

import PySimpleGUI as psg
import json
import pandas as pd
import matplotlib.pyplot as plt


# 禁用警告
pd.options.mode.chained_assignment = None


# 获取文件的所有列
def get_filelist(list):
    with open('config\\PDlist.json', 'r', encoding='utf-8') as file:
        jsondata = json.load(file)
    print(f"这里是文件所有的列：{jsondata[f'{list}'].keys()}")


# 生成json配置文件
def creat_json_profile(df,list):
    # 获取文件的所有列
    cloumns_list = df.columns.tolist()
    # 将列写入字典
    cloumns_dict = {}
    for iter in cloumns_list:
        cloumns_dict.update({iter:iter})
    cloumns_dict = {f"{list}":cloumns_dict}

    # 将字典写入json
    with open('config\\PDlist.json','w',encoding='utf-8') as file:
        cloumns_dict = json.dumps(cloumns_dict,ensure_ascii=False,indent=4)
        file.write(cloumns_dict)
        print(file)

# 数据去重
def Deduplication(df,subsetmult = []):
    isFlag = True
    while isFlag:
        print("""
        -----数据去重-----
        请选择去重的方式
        1、按所有字段合并作为唯一值去重
        2、按指定一列或多列去重
        """)
        user_input = input("请输入操作步骤: ")
        if user_input == '1':
            df_duplicates = df.drop_duplicates(keep='first')
            isFlag = False
        elif user_input == '2':
            get_filelist('lsit1')
            user_input_params = input("请输入去重的唯一值列组合，用英文逗号(,)隔开：")
            # 设置指定列
            subsetmult += user_input_params.split(",")
            # print(subsetmult)
            df_duplicates = df.drop_duplicates(subset=subsetmult, keep='first')
            isFlag = False
        else:
            print('选择的步骤有误,请重新输入')
    print(f'去重之后的数据：\n{df_duplicates}')
    df_duplicates.to_csv('test\\new_data_duplicates.csv', index=False, encoding='GBK')
    print('去重后的数据保存在以下路径 : test\\new_data_duplicates.csv')


# 合并唯一值
def add_unique(df):
    # 用户输入组合列
    get_filelist('list1')
    user_input_params = input("请输入唯一值列组合，用英文逗号(,)隔开：")
    alllist = user_input_params.split(",")
    # 合并唯一主键
    df_new_col = df.assign(unique_value = df[f'{alllist[0]}'])
    for iter in alllist[1:]:
        # print(1)
        # print(df_new_col)
        df_new_col['unique_value'] = df_new_col['unique_value'] + df_new_col[f'{iter}']
    print(f'合并唯一值之后的数据：{df_new_col}')
    df_new_col.to_csv('test\\new_data_unique.csv', index=False, encoding='GBK')
    print('合并唯一值后的数据保存在以下路径 : test\\new_data_unique.csv')


# 图标展示数据
def icon_display(df):
    font_name = 'KaiTi'
    get_filelist('list1')
    user_input_params = input("请输入图标统计X轴列名和Y轴列名，用英文逗号(,)隔开：")
    list = user_input_params.split(",")
    plt.bar(df[f'{list[0]}'],df[f'{list[1]}'])
    user_input = input("请输入图表的标题 : ")
    plt.title(f'{user_input}',fontname = font_name)
    plt.xlabel(f'{list[0]}',fontname = font_name)
    plt.ylabel(f'{list[1]}',fontname = font_name)
    plt.show()


# 核对两个报表的某些列
def match_check(df_original,df_reference):
    get_filelist('list1')
    user_input_unique = input("请输入需要对比的两张表的唯一值 : ")
    unique = user_input_unique
    # 根据某一列进行连接（例如，根据ID列）
    df_merged = pd.merge(df_original, df_reference, on=unique, how='left')
    # 匹配核对
    isFlag = True
    while isFlag:
        print(f"连接两张表后的字段值：f{df_merged.columns}")
        user_input_params = input("请输入需要核对的列，用英文逗号(,)隔开（例如需要表1的 账号 列核对表2的 acct 列时输入：账号,acct）：")
        alllist = user_input_params.split(",")
        # 创建一个新的列来存储匹配结果
        df_merged[f'比对_{alllist[0]}列和{alllist[1]}列'] = df_merged[f'{alllist[0]}'] == df_merged[f'{alllist[1]}']
        # 打印匹配结果
        print(f'核对后的数据：\n{df_merged}')
        print("""
        是否继续核对:
        0、退出
        1、继续核对
        """)
        user_input = input("请出入操作步骤: ")
        if user_input == '0':
            break
        elif user_input == '1':
            continue
        else:
            print("输入的操作步骤有误~~~请重新输入!")
    df_merged.to_csv('test\\merged.csv', index=False, encoding='GBK')
    print('合并唯一值后的数据保存在以下路径 : test\\merged.csv')


if __name__ == "__main__":
    # 读取需要处理的数据
    df1 = pd.read_csv('test\\test1.csv',index_col=False,encoding='GBK')
    df2 = pd.read_csv('test\\test2.csv',index_col=False,encoding='GBK')

    # 根据导入的文件生成json配置文件
    creat_json_profile(df1,'list1')

    # 开始选择操作步骤
    isFlag = True
    while isFlag:
        print("""
        数据读取成功，请选择操作方式:
        0、退出
        1、去重
        2、合并唯一值
        3、图像展示
        4、数据核对
        """)
        user_input = input("请出入操作步骤: ")
        # 退出
        if user_input == '0':
            isFlag = False
        # 去重
        elif user_input == '1':
            Deduplication(df1)
        # 合并唯一值
        elif user_input == '2':
            add_unique(df1)
        # 图像展示
        elif user_input == '3':
            icon_display(df1)
        # 数据核对
        elif user_input == '4':
            match_check(df1,df2)
        else:
            print("输入的操作步骤有误~~~请重新输入!")




