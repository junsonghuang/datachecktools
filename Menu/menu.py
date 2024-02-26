# @Creater ：huangjunsong
# @Time : 2024/2/25 15:48
# @File : menu.py
# @Software : PyCharm

import PySimpleGUI as sg
import Data_operation


# 去重功能界面
def window_deduplication():
    layout = [
        [sg.Text('去重：', font=('楷体', 20))],
        [sg.Button('返回主界面')],
    ]
    window = sg.Window('去重',layout,size=(600,400),grab_anywhere=True,resizable=True)
    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED or event == '返回主界面':
            break
    window.close()
    return True


def window_add_unique():
    layout = [
        [sg.Text('合并唯一值：', font=('楷体', 20))],
        [sg.Button('返回主界面')]
    ]
    window = sg.Window('合并唯一值',layout,size=(600,400),grab_anywhere=True,resizable=True)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '返回主界面':
            break
    window.close()
    return True



def main_window():
    main_menu = [
        ['文件', '导入核对文件'],
        ['功能', ['去重', '合并唯一值', '图像展示', '数据核对']],
    ]
    sg.theme('DefaultNoMoreNagging')
    layout = [[sg.Menu(main_menu)],
              [sg.Text('数据核对功能，请选择 “功能” 菜单进行操作~@！', font=('楷体', 16), size=(80, 5), expand_x=True)]
            ]
    return sg.Window('主界面', layout, size=(600, 400), enable_close_attempted_event=True,
                     grab_anywhere=True,resizable=True)


def memu_index():
    # 主窗口进入
    window = main_window()

    # 窗口监控
    while True:
        event,values = window.read()
        print(event)
        if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT and sg.popup_yes_no('请确认是否需要退出软件?',title='确认退出') == 'Yes':
            break
        elif event == '去重':
            window.hide()
            window_deduplication()
            window.un_hide()
        elif event == '合并唯一值':
            window.hide()
            window_add_unique()
            window.un_hide()
    return window
