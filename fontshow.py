#!/usr/bin/env python3
import urwid as u

text = [
"""A B C D E F G H I J K L M
N O P Q R S T U V W X Y Z

a b c d e f g h i j k l m
n o p q r s t u v w x y z

0 1 2 3 4 5 6 7 8 9

# $ % & ' (
) * + , - . /
: ; < = > ? @
[ \ ] ^ _ ` ~


""",
("0","██"), ("8","▖")," ", ("1","██"), ("9","▖"), " ", ("2","██"), ("10","▖"), " ", ("3","██"), ("11","▖\n"),
("8","▝▀▘"), " ", ("9","▝▀▘"), " ", ("10","▝▀▘"), " ", ("11","▝▀▘\n\n"),
("4","██"), ("12","▖"), " ", ("5","██"), ("13","▖"), " ", ("6","██"), ("14","▖"), " ", ("7","██"), ("15","▖\n"),
("12","▝▀▘"), " ", ("13","▝▀▘"), " ", ("14","▝▀▘"), " ", ("15","▝▀▘")
]

palette = [
    ("0",  "black",         ""),
    ("1",  "dark red",      ""),
    ("2",  "dark green",    ""),
    ("3",  "brown",         ""),
    ("4",  "dark blue",     ""),
    ("5",  "dark magenta",  ""),
    ("6",  "dark cyan",     ""),
    ("7",  "light gray",    ""),
    ("8",  "dark gray",     ""),
    ("9",  "light red",     ""),
    ("10", "light green",   ""),
    ("11", "yellow",        ""),
    ("12", "light blue",    ""),
    ("13", "light magenta", ""),
    ("14", "light cyan",    ""),
    ("15", "white",         "")
 ]

textbox = u.Text(text, align="center")
loop = u.MainLoop(u.Filler(textbox), palette, unhandled_input=u.ExitMainLoop())
loop.run()