from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Setup")

mainframe = ttk.Frame(root, padding="12 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

patient = StringVar()
patientValues = ["patient 1", "patient 2"]

ttk.Label(mainframe, text="Patient").grid(column=2, row=1, sticky=(W, E))
feet_entry = ttk.Combobox(mainframe, width=7, textvariable=patient, values=patientValues)
feet_entry.grid(column=2, row=2, sticky=(W, E))


utilisateur = StringVar()
utilisateurValues = ["user 1", "user 2"]

ttk.Label(mainframe, text="Utilisateur").grid(column=2, row=4, sticky=(W, E))
feet_entry = ttk.Combobox(mainframe, width=7, textvariable=utilisateur, values=utilisateurValues)
feet_entry.grid(column=2, row=5, sticky=(W, E))

maladie = StringVar()
maladieValues = ["maladie 1", "maladie2"]

ttk.Label(mainframe, text="Maladie").grid(column=2, row=7, sticky=(W, E))
feet_entry = ttk.Combobox(mainframe, width=7, textvariable=maladie, values=maladieValues)
feet_entry.grid(column=2, row=8, sticky=(W, E))


#ttk.Label(mainframe, textvariable=maladie).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Demarrer").grid(column=3, row=12, sticky=W)

root.mainloop()

