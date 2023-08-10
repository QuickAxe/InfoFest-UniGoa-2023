import tkinter as tk
from tkinter import ttk
import tkinterDnD  # Importing the tkinterDnD module

# You have to use the tkinterDnD.Tk object for super easy initialization,
# and to be able to use the main window as a dnd widget
def return_the_text(s):
    root = tkinterDnD.Tk()
    root.geometry('300x200+1000+300')  
    root.title("Drag and Drop Your Text File")

    stringvar = tk.StringVar()
    stringvar.set('Drop here or drag from here!')


    def drop(event):
        # This function is called, when stuff is dropped into a widget
        stringvar.set(event.data)
        try:
            print(1)
            s.set(open(event.data).read())
            print(1)
            root.exit()
            print(1)
            # exit(0)
        except:
            print(2)
            root.destroy()
            print(2)
            return_the_text(s)
            print(2)
            # exit(0)

    def drag_command(event):
        # This function is called at the start of the drag,
        # it returns the drag type, the content type, and the actual content
        return (tkinterDnD.COPY, "DND_Text", "Some nice dropped text!")


    # Without DnD hook you need to register the widget for every purpose,
    # and bind it to the function you want to call
    label_1 = tk.Label(root, textvar=stringvar, relief="solid")
    label_1.pack(fill="both", expand=True, padx=10, pady=10)

    label_1.register_drop_target("*")
    label_1.bind("<<Drop>>", drop)

    label_1.register_drag_source("*")
    label_1.bind("<<DragInitCmd>>", drag_command)


    # With DnD hook you just pass the command to the proper argument,
    # and tkinterDnD will take care of the rest
    # NOTE: You need a ttk widget to use these arguments
    label_2 = ttk.Label(root, ondrop=drop, ondragstart=drag_command,
                        textvar=stringvar, padding=50, relief="solid")
    label_2.pack(fill="both", expand=True, padx=10, pady=10)
    root.mainloop()
