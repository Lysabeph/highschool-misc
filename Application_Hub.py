#!/usr/bin/python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango
import io
import os
import sys
import subprocess
import fcntl


class Application_Menu(Gtk.Window):
    
    os.chdir(os.environ['HOME'])
    applications_dir = "/usr/share/applications/"
    applications_list = os.listdir(applications_dir)
    non_gui_applications = []
    for app in applications_list:
        if os.path.isdir(applications_dir + app):
            non_gui_applications.append(app)
    for app in non_gui_applications:
        applications_list.remove(app)
    non_gui_applications = []
    for app in applications_list:
        with open(applications_dir + app, "r", encoding="utf8") as file:
            app_info = file.readlines()
        for item in app_info:
            if "NoDisplay=true" in item:
                non_gui_applications.append(app)
                break
    for app in non_gui_applications:
        applications_list.remove(app)
    for app in applications_list:
       applications_list [applications_list.index(app)] = app.split(".")[0]
    applications_list.sort()
    

    def __init__(self):
        Gtk.Window.__init__(self, title="Application Selector")
        self.connect("destroy", Gtk.main_quit)
        #self.set_size_request(160, 120)
        self.move(0, 0)
        self.set_border_width(10)
        self.set_resizable(False)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(vbox)
        
        hbox = Gtk.Box(spacing=5)
        vbox.pack_start(hbox, True, True, 0)

        label = Gtk.Label("Please select/enter a command.")
        hbox.pack_start(label, True, True, 0)

        close_button = Gtk.Button(label="Exit")
        close_button.connect("clicked", self.close)
        hbox.pack_start(close_button, True, True, 0)

        self.application_list = Gtk.ListStore(int, str)
        for item in enumerate(self.applications_list):
            self.application_list.append(item)

        self.combo_box = Gtk.ComboBox.new_with_model_and_entry(self.application_list)
        self.combo_box.get_child().set_placeholder_text("Enter a command.")
        self.combo_box.get_child().connect("activate", self.on_button_click)
        self.combo_box.set_entry_text_column(1)
        vbox.pack_start(self.combo_box, False, False, 0)

        button = Gtk.Button(label="Enter")
        button.connect("clicked", self.on_button_click)
        vbox.pack_start(button, True, True, 0)

        self.scroll = Gtk.ScrolledWindow()
        self.scroll.set_size_request(-1, 500)
        self.text_view = Gtk.TextView()
        self.text_buffer = self.text_view.get_buffer()
        self.text_view.set_editable(False)
        self.text_view.set_size_request(-1, 500)
        self.text_view.modify_font(Pango.FontDescription("monospace 8"))
        self.scroll.add(self.text_view)
        self.expander = Gtk.Expander()
        #self.expander.set_size_request(-1, 500)
        self.expander.add(self.scroll)
        vbox.pack_start(self.expander, True, True, 0)


    def on_button_click(self, button):
        command = self.combo_box.get_child().get_text()
        if command[:5] == "sudo ":
            if command[5:] in self.applications_list:
                command += " &"
            print("Executing command: " + command)
            self.combo_box.get_child().set_text("")
            #result = subprocess.check_output("gksudo " + command, universal_newlines=True, shell=True)
            #end_iter = self.text_buffer.get_end_iter()
            #self.text_buffer.insert(end_iter, result)
            os.system("gksudo" + command)
        elif command == "exit":
            self.close(None)
        else:
            if command in self.applications_list:
                command += " &"
            print("Executing command: " + command)
            self.combo_box.get_child().set_text("")
            #result = subprocess.check_output(command, universal_newlines=True, shell=True)
            #end_iter = self.text_buffer.get_end_iter()
            #self.text_buffer.insert(end_iter, result)
            os.system(command)


    def close(self, button):
        sys.exit(0)


window = Application_Menu()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
