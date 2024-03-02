# @Creater ：huangjunsong
# @Time : 2024/2/25 15:48
# @File : menu.py
# @Software : PyCharm

import PySimpleGUI as sg
import Data_operation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 去重功能界面
def window_deduplication(df):
    layout = [
        [sg.Text('请选择去重的方式',font=('楷体', 13))],
        [sg.Text(f"这是这里所有的列:{Data_operation.get_filelist('list1')}",key='-get_filelist-')],
        [sg.Radio('按所有字段合并作为唯一值去重','dption_group',enable_events=True,default = True,key='dption_radio_1'),
         sg.Radio('按指定一列或多列去重','dption_group',enable_events=True,key='dption_radio_2')],
        [sg.Text('请输入去重的唯一值列组合：')],
        [sg.Listbox(Data_operation.get_filelist('list1'),select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE,
                    key='listbox1',size = (50,10),visible=False)],
        [sg.Button('去重'),sg.Button('返回主界面')]
    ]
    window = sg.Window('去重',layout,size=(600,400),grab_anywhere=True,resizable=True)
    while True:
        event,values = window.read()
        print(event,values)
        if event == sg.WIN_CLOSED or event == '返回主界面':
            break
        if event == 'dption_radio_2':
            window['listbox1'].update(visible=True)
        elif event == 'dption_radio_1':
            window['listbox1'].update(visible=False)
        if event == '去重':
            if values['dption_radio_1']:
                filelocal = Data_operation.Deduplication(df,user_input='1')
                window['-get_filelist-'].update(f'你选择了按所有字段去重！！\n{filelocal}。')
            elif values['dption_radio_2']:
                window['-get_filelist-'].update('你选择了按指定字段去重')
                filelocal = Data_operation.Deduplication(df,user_input='2',subsetmult=values['listbox1'])
                window['-get_filelist-'].update(f'你选择了按指定一列或多列去重！！\n{filelocal}。')
    window.close()
    return True

#合并唯一值功能界面
def window_add_unique(df):
    layout = [
        [sg.Text('请选择需要合并的字段：', font=('楷体', 13))],
        [sg.Text("核对后保存的文件路径",key='-get_filelist-')],
        [sg.Listbox(Data_operation.get_filelist('list1'), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE,
                    key='listbox1', size=(50, 10), visible=True)],
        [sg.Button('合并唯一值'),sg.Button('返回主界面')]
    ]
    window = sg.Window('合并唯一值',layout,size=(600,400),grab_anywhere=True,resizable=True)
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == '返回主界面':
            break
        if event == '合并唯一值':
            filelocal = Data_operation.add_unique(df,values['listbox1'])
            window['-get_filelist-'].update(f'{filelocal}。')
    window.close()
    return True


#数据核对功能界面
def window_match_check(df):
    all_list = Data_operation.get_filelist('list1')
    layout = [
        [sg.Text('两表数据核对：', font=('楷体', 13))],
        [sg.Text("核对后保存的文件路径", key='-get_filelist-')],
        [sg.Text("请输入需要对比的两张表的唯一值："),
         sg.Combo(all_list, key='combo1', size=(30, 10), visible=True,default_value=all_list[0])],
        [sg.Button('选择唯一值')],
        [sg.Text('请选择两表需要比对的字段进行比对：', font=('楷体', 12),visible=False)],
        [sg.Text("表1",visible=False,key='biao1'),sg.Combo([], key='combo_check1', size=(30, 10), visible=False)],
        [sg.Text("表2",visible=False,key='biao2'),sg.Combo([], key='combo_check2', size=(30, 10), visible=False)],
        [sg.Button('核对',visible=False,key='checkbutton')],
        [sg.Button('返回主界面')]
    ]
    window = sg.Window('合并唯一值', layout, size=(600, 400), grab_anywhere=True, resizable=True)
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == '返回主界面':
            break
        if event == '选择唯一值':
            df_merged = Data_operation.connect_match(df[0],df[1],values['combo1'])
            checklist = list(df_merged.keys())
            window['combo_check1'].update(values=checklist,visible=True)
            window['combo_check2'].update(values=checklist,visible=True)
            window['biao1'].update(visible=True)
            window['biao2'].update(visible=True)
            window['checkbutton'].update(visible=True)
        elif event == 'checkbutton':
            window['checkbutton'].update('继续核对')
            alllist = [values['combo_check1'],values['combo_check2']]
            print(type(alllist))
            filelocal = Data_operation.match_check(df_merged,alllist)
            window['-get_filelist-'].update(f'{filelocal}。')
    window.close()
    return True


def window_draw(df):
    all_list = Data_operation.get_filelist('list1')
    layout = [
        [sg.Text('点击绘图按钮,开始绘制选中参数的图像！~：', font=('楷体', 13))],
        [sg.Text('请输入图形标题名称：'),sg.Input(key='title')],
        [sg.Text("请选择X轴坐标值："),sg.Combo(all_list, key='Xlabel', size=(30, 10))],
        [sg.Text("请选择Y轴坐标值："), sg.Combo(all_list, key='Ylabel', size=(30, 10))],
        [sg.Button('绘图',key='draw')],
        [sg.Canvas(size=(400,400), key='canvas1')]
    ]
    window = sg.Window('绘图', layout, size=(600, 400), grab_anywhere=True, resizable=True)
    canvas = None
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == '返回主界面':
            break
        if event == 'draw':
            fig = Data_operation.icon_display(df[0],axis_title=values['title'],axis_Xlabel=values['Xlabel']
                                              ,axis_Ylabel=values['Ylabel'])
            if canvas is not None:
                canvas.get_tk_widget().destroy()
            canvas = FigureCanvasTkAgg(fig, window['canvas1'].TKCanvas)
            canvas.draw()
            canvas.get_tk_widget().pack()

#主界面功能
def main_window(df):
    main_menu = [
        ['文件', '导入核对文件'],
        ['功能', ['去重', '合并唯一值','数据核对','绘图']],
    ]
    sg.theme('DefaultNoMoreNagging')
    layout = [[sg.Menu(main_menu)],
              [sg.Text('主界面，请选择 “功能” 菜单进行操作~@！', font=('楷体', 16), size=(80, 5), expand_x=True)]
            ]
    window =  sg.Window('主界面', layout, size=(600, 400), enable_close_attempted_event=True,
                     grab_anywhere=True,resizable=True)
    # 窗口监控
    while True:
        event,values = window.read()
        print(event)
        if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT and sg.popup_yes_no('请确认是否需要退出软件?',title='确认退出') == 'Yes':
            break
        elif event == '去重':
            window_deduplication(df[0])
            window.un_hide()
        elif event == '合并唯一值':
            window_add_unique(df[0])
            window.un_hide()
        elif event == '数据核对':
            window_match_check(df)
            window.un_hide()
        elif event == '绘图':
            window_draw(df)
            window.un_hide()
    return window


