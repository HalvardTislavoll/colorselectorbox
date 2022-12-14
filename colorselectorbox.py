#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#    Nov 09, 2020 08:02:52 PM CET  platform: Linux

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import colorselectorbox_support
import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)
    colorselectorbox_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    colorselectorbox_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("111x112+954+383")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(0,  0)
        top.title("New Toplevel")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(x=5, y=5, height=105, width=105)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")

        self.lbl_bottom_color = tk.Label(self.Frame1)
        self.lbl_bottom_color.place(x=41, y=41, height=60, width=60)
        self.lbl_bottom_color.configure(activebackground="#f9f9f9")
        self.lbl_bottom_color.configure(background="LightSkyBlue1")
        self.lbl_bottom_color.configure(borderwidth="2")
        self.lbl_bottom_color.configure(relief="raised")
        self.lbl_bottom_color.bind('<ButtonRelease-1>',lambda e:colorselectorbox_support.on_lbl_bottom_color(e))

        self.lbl_top_color = tk.Label(self.Frame1)
        self.lbl_top_color.place(x=0, y=0, height=60, width=60)
        self.lbl_top_color.configure(activebackground="#f9f9f9")
        self.lbl_top_color.configure(background="cornflowerblue")
        self.lbl_top_color.configure(borderwidth="2")
        self.lbl_top_color.configure(relief="raised")
        self.lbl_top_color.bind('<ButtonRelease-1>',lambda e:colorselectorbox_support.on_lbl_top_color(e))

        self.btn_black_white = tk.Button(self.Frame1)
        self.btn_black_white.place(x=1, y=61, height=41, width=41)
        self.btn_black_white.configure(activebackground="#f9f9f9")
        photo_location = os.path.join(prog_location,"./asset/graphics/system_icon/kvitt_svart.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.btn_black_white.configure(image=_img0)
        self.btn_black_white.bind('<ButtonRelease-1>',lambda e:colorselectorbox_support.on_btn_black_white(e))

        self.btn_change_color = tk.Button(self.Frame1)
        self.btn_change_color.place(x=60, y=2, height=41, width=41)
        self.btn_change_color.configure(activebackground="#f9f9f9")
        self.btn_change_color.configure(command=colorselectorbox_support.on_btn_change_color)
        photo_location = os.path.join(prog_location,"./asset/graphics/system_icon/snu_farge.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.btn_change_color.configure(image=_img1)
        self.btn_change_color.configure(text='''Button''')

if __name__ == '__main__':
    vp_start_gui()





