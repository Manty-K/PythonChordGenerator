from tkinter import *
from functools import partial
from progression_generator import *

def start_program():
    selected_note = 'C'
    my_text = "Choose a Note"
    note_list = ["A", "Bb", "B", 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
    scale = 0

    def set(name):
        global my_text
        selected_note = name
        my_text = generate_sequence(note=selected_note,scale=scale)
        progression.config(text=my_text)

    def NoteButton(name):
        return Button(master=all_notes, text=name, command=partial(set, name))

    def change_scale(index):

        global scale
        scale = index
        print(scale)

    top = Tk("top = Tkinter.Tk()")
    top.minsize(width=1000, height=500)
    top.maxsize(width=1000, height=500)
    all_notes = Frame()
    all_notes.pack()
    all_scale = Frame()
    major_radio = Radiobutton(all_scale,variable=scale,value = 0,command=partial(change_scale, 0))
    major_radio.grid(row=0,column=0)
    major_l = Label(master=all_scale,text="Major")
    major_l.grid(row=0,column=1)
    minor_radio = Radiobutton(all_scale,variable=scale,value = 1,command=partial(change_scale, 1))
    minor_radio.grid(row=0,column=2)
    minor_l = Label(master=all_scale, text="Minor")
    minor_l.grid(row=0,column=3)
    all_scale.pack()
    for idx, val in enumerate(note_list):
        myNote = NoteButton(val)
        myNote.grid(row=0, column=idx,padx=10, pady=20)

    # create a StringVar class
    my_string_var = StringVar()

    # set the text
    my_string_var.set("What should I learn")

    progression = Label(master=top, text =my_text)
    progression.config(font=("Courier", 44))
    progression.pack()
    top.mainloop()
