#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#    Nov 08, 2020 07:39:23 PM CET  platform: Linux   startup
#    Nov 09, 2020 12:50:05 PM CET  platform: Linux   finished
""".........filname : grayshadeselectorbox_support.py
............Purpose : choose shades of gray a la Gimp color picker box
..date last updated : Nov 09, 2020
.............Author : Halvard Tislavoll
.....released under : MIT License
.the current status : C  (Completed or Incomplete)"""
# ============================================================================ #
import sys
import share
import colorselectorbox
import colorselectorbox_support
from gray_shades import shades_dict
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


def set_Tk_var():
    global scale
    scale = tk.DoubleVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    #--------------
    w.lbl_color.configure(text="")   # removes label text
    root.after(10, lift)   # make sure that no other forms is covered this one
    # Check if this module runs alone
    try:
        if not share.solo:
            current_label_level()  
    except:
        print("This is a module that can only be called from other modules.")
        destroy_window()

def current_label_level():
    """Function that find out if label gray shade applies to foreground or background"""
    level = share.level
    if level=='top':
        w.Scale1.set(float(share.top_idx))   # set the Scale widgets init value
        apply_value(share.top_idx)
    elif level=='bottom':
        w.Scale1.set(float(share.bottom_idx))   # set the Scale widgets init value
        apply_value(share.bottom_idx)


def lift():
    """Function that lifts the form at the front of the screen"""
    root.attributes("-topmost", True)


def apply_value(idx):
    """Function that update labels with current color from shades dict"""
    w.lbl_red.configure(text=shades_dict[idx][2])          # R
    w.lbl_green.configure(text=shades_dict[idx][3])        # G
    w.lbl_blue.configure(text=shades_dict[idx][4])         # B
    w.lbl_hex.configure(text=shades_dict[idx][1])          # Hex
    w.lbl_python_color.configure(text=shades_dict[idx][0]) # Hex
    w.lbl_color.configure(background=shades_dict[idx][1])  # color      

def on_scale(*args):
    """Function that uses scale and changes the index value for shades_dict"""
    val=scale.get()
    st = share.level   # which of the top or bottom label color are treated
    if st=='top':
        share.top_idx = int(val)
        apply_value(share.top_idx)   # update labels with current color from dict
    elif st=='bottom':
        share.bottom_idx = int(val)
        apply_value(share.bottom_idx)   # update labels with current color from dict

def on_btn_cansel():
    """Function that terminate this form"""
    destroy_window()

def on_btn_ok():
    """Function that returns grayscale values for foreground and background."""
    # set share.color
    l = share.level
    if l=='top':
        share.rem_top_black_white = shades_dict[share.top_idx][1]       
    elif l=='bottom':
        share.rem_bottom_black_white = shades_dict[share.bottom_idx][1]
    root.withdraw()
    colorselectorbox_support.show_me()

def destroy_window():
    """Function which closes the window."""
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import grayshadeselectorbox
    grayshadeselectorbox.vp_start_gui()
