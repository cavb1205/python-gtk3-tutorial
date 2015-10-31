#!/usr/bin/env python3

from gi.repository import Gtk

class Frame(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(200, 200)
        self.set_border_width(5)
        self.connect("destroy", Gtk.main_quit)

        label = Gtk.Label("Label in a Frame")

        frame = Gtk.Frame(label="Frame")
        frame.add(label)
        self.add(frame)

window = Frame()
window.show_all()

Gtk.main()
