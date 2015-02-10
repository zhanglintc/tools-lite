#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
                   _ooOoo_ 
                  o8888888o 
                  88" . "88 
                  (| -_- |) 
                  O\  =  /O 
               ____/`---'\____ 
             .'  \\|     |//  `. 
            /  \\|||  :  |||//  \ 
           /  _||||| -:- |||||-  \ 
           |   | \\\  -  /// |   | 
           | \_|  ''\---/''  |   | 
           \  .-\__  `-`  ___/-. / 
         ___`. .'  /--.--\  `. . __ 
      ."" '<  `.___\_<|>_/___.'  >'"". 
     | | :  `- \`.;`\ _ /`;.`/ - ` : | | 
     \  \ `-.   \_ __\ /__ _/   .-` /  / 
======`-.____`-.___\_____/___.-`____.-'====== 
                   `=---=' 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
         佛祖保佑    iii    永无BUG 
"""

from __future__ import print_function
import ctypes
import re

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE= -11
STD_ERROR_HANDLE = -12

FOREGROUND_BLACK = 0x0
FOREGROUND_BLUE = 0x01 # text color contains blue.
FOREGROUND_GREEN= 0x02 # text color contains green.
FOREGROUND_RED = 0x04 # text color contains red.
FOREGROUND_INTENSITY = 0x08 # text color is intensified.

BACKGROUND_BLUE = 0x10 # background color contains blue.
BACKGROUND_GREEN= 0x20 # background color contains green.
BACKGROUND_RED = 0x40 # background color contains red.
BACKGROUND_INTENSITY = 0x80 # background color is intensified.

class Color:
    """
    See http://msdn.microsoft.com/library/default.asp?url=/library/en-us/winprog/winprog/windows_api_reference.asp
    for information on Windows APIs. - www.sharejs.com
    """

    std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    
    def set_cmd_color(self, color, handle=std_out_handle):
        """
        (color) -> bit
        Example: set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE | FOREGROUND_INTENSITY)
        """

        bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
        return bool
    
    def reset_color(self):
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)
    
    def print_red_text(self, print_text):
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_INTENSITY)
        print(print_text, end = '')
        self.reset_color()
        
    def print_green_text(self, print_text):
        self.set_cmd_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
        print(print_text, end = '')
        self.reset_color()
    
    def print_blue_text(self, print_text): 
        self.set_cmd_color(FOREGROUND_BLUE | FOREGROUND_INTENSITY)
        print(print_text, end = '')
        self.reset_color()
          
    def print_red_text_with_blue_bg(self, print_text):
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_INTENSITY| BACKGROUND_BLUE | BACKGROUND_INTENSITY)
        print(print_text, end = '')
        self.reset_color()

def cprint(s, c = None):
    if not s:
        return

    if not c:
        c = Color()

    mc = re.search('(.*?)(\[.*?\])(.*)', s, re.DOTALL)
    if not mc:
        print(s, end = '')

    else:
        print(mc.group(1), end = '')

        command = mc.group(2)

        command = command.replace('[', '')
        command = command.replace(']', '')
        command = command.replace(' ', '')

        to_p  = command.split(',')[0]
        color = command.split(',')[1]

        if color == 'red':
            c.print_red_text(to_p)

        cprint(mc.group(3), c)

if __name__ == "__main__":
    # clr = Color()
    # clr.print_red_text('red')
    # clr.print_green_text('green')
    # clr.print_blue_text('blue')
    # clr.print_red_text_with_blue_bg('background')
    cprint("this is: [red, red]")

    try:
        input()
    except:
        pass
    
# code from: http://www.sharejs.com/codes/python/8665

