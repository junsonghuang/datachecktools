import PySimpleGUI as sg

def window1():
    layout = [[sg.Text('这是界面1')],
              [sg.Button('返回')]]

    window = sg.Window('界面1', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == '返回':
            break

    window.close()

def window2():
    layout = [[sg.Text('这是界面2')],
              [sg.Button('返回')]]

    window = sg.Window('界面2', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == '返回':
            break

    window.close()

main_menu_def = [['文件', ['界面1', '界面2']],
                ['帮助', ['关于']]]

main_menu_layout = [[sg.Menu(main_menu_def)]]

main_window_layout = [[sg.Text('这是主界面')],
                      [sg.Button('退出')]]

window = sg.Window('主界面', main_window_layout + main_menu_layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == '退出':
        break
    elif event == '界面1':
        window.hide()
        window1()
        window.un_hide()
    elif event == '界面2':
        window.hide()
        window2()
        window.un_hide()
    elif event == '关于':
        sg.popup('这是一个示例程序')

window.close()