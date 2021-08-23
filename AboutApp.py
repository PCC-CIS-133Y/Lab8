import os
import pygubu

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "about.ui")


class AboutApp:

    # This class implements a simple display of some about text.
    # It can either be run as a stand-alone app (run AboutApp.py directly)
    # or within a tabbed notebook (run main.py and select the About... tab).

    def __init__(self, master):

        # Boilerplate from pygubu-designer. Renamed builder and mainwindow to use
        # name mangling.
        self.__builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.__mainwindow = builder.get_object('top_frame', master)
        builder.connect_callbacks(self)

    def get_top_frame(self):
        # Return the top frame for the app so that it can be displayed in a tabbed notebook.
        return self.__mainwindow

    def run(self):
        self.__mainwindow.mainloop()


if __name__ == '__main__':
    import tkinter as tk

    root = tk.Tk()
    app = AboutApp(root)
    app.run()

