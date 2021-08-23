import os
import pygubu

import tkinter as tk
import tkinter.messagebox as mb

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "grams_to_ounces.ui")


class GramsToOuncesApp:
    GRAMS_PER_OUNCE = 28.3495

    # This class implements a simple calculator to convert grams to ounces.
    # It can either be run as a stand-alone app (run GramsToOuncesApp.py directly)
    # or within a tabbed notebook (run main.py and select the Grams to Ounces tab).

    def __init__(self, master):

        # Boilerplate to build the tkinter interface based on grams_to_ounces.ui
        self.__builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.__mainwindow = builder.get_object('top_frame', master)
        builder.connect_callbacks(self)

        # Save these two UI elements as properties so that we can access them when
        # the user clicks on the calculate button.
        self.__grams_entry = builder.get_object('grams_entry', master)
        self.__ounces_entry_variable = builder.get_variable('ounces_entry_variable')

    def calculate(self):
        # Convert grams to ounces. If there's an error, display an error message.
        try:
            grams = float(self.__grams_entry.get())
            ounces = grams / self.GRAMS_PER_OUNCE
            self.__ounces_entry_variable.set("{:.2f} ounces".format(ounces))
        except ValueError:
            mb.showerror(title="Error Calculating Ounces!", message="Grams must be a decimal number. Please try again.")

    def get_top_frame(self):
        # Return the top frame for the app so that it can be displayed in a tabbed notebook.
        return self.__mainwindow

    def run(self):
        self.__mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = GramsToOuncesApp(root)
    app.run()

