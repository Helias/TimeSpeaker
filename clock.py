#!/usr/bin/env python

import gtk
import appindicator
import os
import time
import sys

dir_path = os.path.dirname(os.path.abspath(__file__)) + "/"

t=0

class Clock:
    def __init__(self):
        self.ind = appindicator.Indicator("clock-app",
                                           dir_path + "clock.png",
                                           appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status(appindicator.STATUS_ACTIVE)
	self.ind.set_attention_icon(dir_path  + "clock_red.png")
        self.menu_setup()
        self.ind.set_menu(self.menu)

    def menu_setup(self):
        self.menu = gtk.Menu()

        self.active_item = gtk.MenuItem("Say Time")
        self.active_item.connect("activate", self.saytime)
        self.active_item.show()
        self.menu.append(self.active_item)

        self.check_item = gtk.CheckMenuItem("Active")
	self.check_item.set_active(True)
        self.check_item.show()
        self.menu.append(self.check_item)

        self.quit_item = gtk.MenuItem("Quit")
        self.quit_item.connect("activate", self.quit)
        self.quit_item.show()
        self.menu.append(self.quit_item)


    def main(self):
        gtk.timeout_add(1000, self.check_time)
	gtk.main()

    def saytime(self, widget):
	self.ind.set_status(appindicator.STATUS_ATTENTION)
	if ("15" in time.strftime("%M")) or ("30" in time.strftime("%M")) or ("45" in time.strftime("%M")):
		if ("10" in time.strftime("%H")) or ("20" in time.strftime("%H")):
			os.system("echo sono le %s e %s | espeak -v it"% (time.strftime("%H"), time.strftime("%M")))
		elif (time.strftime("%H") == "0") or (time.strftime("%H") == "00"):
			os.system("echo e\' mezzanotte e %s | espeak -v it"% time.strftime("%M"))
		else:
			os.system("echo sono le %s e %s | espeak -v it"% (time.strftime("%H").replace("0", ""), time.strftime("%M")))
	else:
		os.system("echo sono le %s e %s | espeak -v it"% (time.strftime("%H"), time.strftime("%M")))

	if ("00" in time.strftime("%M")):
		if ("10" in time.strftime("%H")) or ("20" in time.strftime("%H")):
			os.system("echo sono le ore %s | espeak -v it"% time.strftime("%H"))
		elif (time.strftime("%H") == "0") or (time.strftime("%H") == "00"):
			os.system("echo e\' mezzanotte | espeak -v it")
		else:
			os.system("echo sono le ore %s | espeak -v it"% time.strftime("%H").replace("0", ""))
	self.ind.set_status(appindicator.STATUS_ACTIVE)

    def quit(self, widget):
        exit(0)

    def check_time(self):
	global t
	if ("16" in time.strftime("%M")) and t == 1:
		t = 0
	elif ("31" in time.strftime("%M")) and t == 1:
		t = 0
	elif ("46" in time.strftime("%M")) and t == 1:
		t = 0
	elif ("01" in time.strftime("%M")) and t == 1:
		t = 0

	if self.check_item.get_active():
		if (("15" in time.strftime("%M")) or ("30" in time.strftime("%M")) or ("45" in time.strftime("%M"))) and t == 0:
			self.ind.set_status(appindicator.STATUS_ATTENTION)
			t = 1
			if ("10" in time.strftime("%H")) or ("20" in time.strftime("%H")):
				os.system("echo sono le %s e %s | espeak -v it"% (time.strftime("%H"), time.strftime("%M")))
			elif (time.strftime("%H") == "0") or (time.strftime("%H") == "00"):
				os.system("echo e\' mezzanotte e %s | espeak -v it"% time.strftime("%M"))
			else:
				os.system("echo sono le %s e %s | espeak -v it"% (time.strftime("%H").replace("0", ""), time.strftime("%M")))

		if ("00" in time.strftime("%M")) and t == 0:
			self.ind.set_status(appindicator.STATUS_ATTENTION)
			t = 1
			if ("10" in time.strftime("%H")) or ("20" in time.strftime("%H")):
				os.system("echo sono le ore %s | espeak -v it"% time.strftime("%H"))
			elif (time.strftime("%H") == "0") or (time.strftime("%H") == "00"):
				os.system("echo e\' mezzanotte | espeak -v it")
			else:
				os.system("echo sono le ore %s | espeak -v it"% time.strftime("%H").replace("0", ""))
	self.ind.set_status(appindicator.STATUS_ACTIVE)
	return True


if __name__ == "__main__":
    Clock().main()
