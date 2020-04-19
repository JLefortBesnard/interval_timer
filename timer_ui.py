from tkinter import *
import time
import os
import subprocess

#start the root
ui = Tk()


# set the parameters for the root/window
ui.title("Kick-Ass Interval Timer")
ui.geometry("250x190")
ui.configure(background="blue")

# Defining all sub-routines:
def interval_timer(nb, interval, warning):
    # interval and warning should be in seconds
    # warning lets you know that the interval is almost over
    now = time.time()
    for i in range(0, nb):
        if warning > 0:
            almost = interval - warning
            time.sleep(almost-1.72)
            subprocess.call(['cvlc', 'boxing_bell.wav','--play-and-exit', 'vlc://quit'])
            time.sleep(warning-1.6)
            subprocess.call(['cvlc', 'fanfare.wav','--play-and-exit', 'vlc://quit'])
        else:
            time.sleep(interval-1.73)
            subprocess.call(['cvlc', 'boxing_bell.wav','--play-and-exit', 'vlc://quit'])
        duration = time.time() - now
        print("so far: {} sec".format(duration))

def start_timer():
    nb_turn = turn.get()
    lap_time = lap.get()
    warning = warn.get()
    now = time.time()
    interval_timer(int(nb_turn), int(lap_time), int(warning))
    duration = time.time() - now
    print("total duration = {} seconds".format(duration))
    subprocess.call(['cvlc', 'applause.wav','--play-and-exit', 'vlc://quit'])

def stop_timer():
    ui.destroy()



# Add entry box + its label
Label(ui, text="Turn?", bg="blue", font="arial 18 bold", fg="yellow").grid(row=1, column=0, sticky=W+E+N+S, padx=5, pady=5)
Label(ui, text="Time?", bg="blue", font="arial 18 bold", fg="yellow").grid(row=2, column=0, sticky=W+E+N+S, padx=5, pady=5)
Label(ui, text="Warning?", bg="blue", font="arial 18 bold", fg="yellow").grid(row=3, column=0, sticky=W+E+N+S, padx=5, pady=5)
turn = Entry(ui, bg='white', width=5)
turn.grid(row=1, column=1, sticky=W+E+N+S, padx=5, pady=5)
lap = Entry(ui, bg='white', width=5)
lap.grid(row=2, column=1, sticky=W+E+N+S, padx=5, pady=5)
warn = Entry(ui, bg='white', width=5)
warn.grid(row=3, column=1, sticky=W+E+N+S, padx=5, pady=5)

# create the needed button to enter inputs
Button(ui, text="Start", width=5, font="arial 18 bold", bg="green", fg="yellow", command=start_timer).grid(row=4, column=0, sticky=W, padx=5, pady=5)
Button(ui, text="Stop", width=5, font="arial 18 bold", bg="red", fg="yellow", command=stop_timer).grid(row=4, column=1, sticky=W, padx=5, pady=5)


#Kickstart the loop
ui.mainloop()
