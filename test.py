import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

layout = [[sg.Canvas(size=(400,400), key='canvas')],
          [sg.Button('绘制图形'), sg.Button('关闭')]]

window = sg.Window('图形嵌入示例', layout)

def draw_plot():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 9, 16])
    canvas = FigureCanvasTkAgg(fig, window['canvas'].TKCanvas)
    canvas.draw()
    canvas.get_tk_widget().pack()

while True:
    event, _ = window.read()

    if event == sg.WINDOW_CLOSED or event == '关闭':
        break

    if event == '绘制图形':
        draw_plot()

window.close()