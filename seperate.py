import subprocess
import os
import tkinter as tk
from tkinter import filedialog
#get filename and path
root=tk.Tk()
root.withdraw()
ffmpegpath=os.getcwd()+'/ffmpeg/bin/ffmpeg.exe'
pathname=filedialog.askdirectory()
filename=filedialog.askopenfilename()
#get frames
subprocess.Popen(ffmpegpath +' -i'+ ' ' + filename+ ' ' +'-qscale:v 1 -qmin 1 -qmax 1 -vsync 0 ' + pathname +'/frame%08d.png', shell=True)

