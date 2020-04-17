import time
import os
import subprocess

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

choice0 = input("how many intervals?")
choice1 = input("time for an interval?")
choice2 = input("time warning before?")

now = time.time()
interval_timer(int(choice0), int(choice1), int(choice2))
duration = time.time() - now
print("total duration = {} seconds".format(duration))
subprocess.call(['cvlc', 'applause.wav','--play-and-exit', 'vlc://quit'])
