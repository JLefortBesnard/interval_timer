### Interval timer for training session.

Download the file timer.py as well as the three .wav files.
On your terminal with the current location where the 4 downloaded files are, activate python3 and type "run timer.py".
Then, follow the steps:
 1. Choose the number of repetition,
 2. Then the duration of each repetition (in sec),
 3. And finally how much time (in sec) before the end of the repetition you want a warning (if this is set to zero, there won't be any warning)
 
For a user interface, download "timer_ui.py" and type "run timer_ui.py" within your terminal with Python3 activated

Dependency: VLC media (with CVLC)

You can change the sounds I used and download some there for example: http://www.wavsource.com/sfx/sfx.htm

Carefull though, if the sounds are shorter or longer than the ones I used, it might affect the accuracy of the timer.
Make sure to compensate following these steps:

 1. Time the duration of the sound:

copy-paste the 4 following lines on python (changing the namesound.wav to your file)

now = time.time()

subprocess.call(['cvlc', 'namesound.wav','--play-and-exit', 'vlc://quit'])

duration = time.time() - now

print("total duration = {} seconds".format(duration))

 2. Compensate by changing the number where it is needed:

eg. boxing_bell.wav has a duration of 1.72 sec so I compensated typing 
time.sleep(almost-1.72)

eg. fanfare.wav has a duration of 1.6 sec so I compensated typing 
time.sleep(warning-1.72)





