"""
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>

"""

import os
import tkinter as tk

def startdl():
    if e3 == "video":
        os.system("youtube-dl " + "-" + e1.get() + " " + e2.get())
    else:
        os.system("youtube-dl " + " --audio-format " + e3.get() + " -" + e1.get() + " " + e2.get())



##    os.system("youtube-dl " + "-" + e1.get() + " " + e2.get())
##    print("youtube-dl " + "-" + e1.get() + e2.get())
##    os.system("youtube-dl " + "--audio-format" + e3.get() + "-" + e1.get() + " " + e2.get())  


master = tk.Tk()
master.title("YouTube-DL Python GUI")
master.geometry("500x100")
tk.Label(master, 
         text="Extra Arguments").grid(row=0)
tk.Label(master,
         text="I personally recommend wxci").grid(row=0, column = 2)
tk.Label(master,
         text="Download Link").grid(row=1)
tk.Label(master,
         text="Audio Format").grid(row=2)
tk.Label(master,
         text="(enter \"video\" for video download)").grid(row=2, column = 2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)



tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Download', command=startdl).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()
