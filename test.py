from Tkinter import *
from turtle import *
import turtle


forward(100)
ts = turtle.getscreen()

ts.getcanvas().postscript(file="duck.eps") #.eps文件即postscript脚本