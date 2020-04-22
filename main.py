from tkinter import Tk, Button, Frame, Label, StringVar
from time import sleep

def startTimer():
    global start, hour, minute, second
    start = True
    
    while start:
        timeVar.set(str(hour)+":"+str(minute)+":"+str(second))
        time_label.update()
        sleep(1)
        second += 1
        
        if second >= 60:
            minute += 1
            second = 0

        if minute >= 60:
            hour += 1
            minute = 0


def stopTimer():
    global start
    start = False


def resetTimer():
    global start, hour, minute, second
    start = False
    hour, minute, second = 0, 0, 0
    timeVar.set("0:0:0")
    time_label.update()


start = True
i = 0
hour, minute, second = 0, 0, 0

root = Tk()
root.title("Stopwatch")
root.maxsize(300, 250)
root.minsize(300, 250)


timeVar = StringVar()
timeVar.set("0:0:0")

time_label = Label(root,
                   textvariable=timeVar,
                   pady=10,
                   font="arial 45")

time_label.pack()

start_button = Button(root,
                      text='Start',
                      pady=10,
                      padx=10,
                      command=startTimer)

start_button.pack()

stop_button = Button(root,
                      text='Stop',
                      pady=10,
                      padx=10,
                      command=stopTimer)

stop_button.pack()

reset_button = Button(root,
                      text='Reset',
                      pady=8,
                      padx=8,
                      command=resetTimer)

reset_button.pack()

root.mainloop()



