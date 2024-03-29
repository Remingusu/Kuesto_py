from tkinter import *
from generateur import qcm_generator


def launch_generation():
    frame_etat = Frame(window, bg='#A2A2A2')
    Label(frame_etat, text=f"Nombre de copie: {nbr_qcm_content.get()}", font=('CAMBRIA', 8), bg='#A2A2A2').grid(row=0,
                                                                                                                column=0)
    Label(frame_etat, text=f"Nom du fichier: {name_content.get()}", font=('CAMBRIA', 8), bg='#A2A2A2').grid(row=1,
                                                                                                            column=0)
    Label(frame_etat, text=f"En cours...", font=('CAMBRIA', 8), bg='#A2A2A2').grid(row=2, column=0)
    frame_etat.grid(row=20, column=2, sticky=SE, ipadx=30, ipady=30)
    qcm_generator.generate(qcm_generator, nbr_qcm_content.get(), name_content.get())
    Label(frame_etat, text=f"Terminez !", font=('CAMBRIA', 8), bg='#A2A2A2').grid(row=3, column=0)
    frame_etat.grid(row=20, column=2, sticky=SE, ipadx=30, ipady=30)


window = Tk()
window.geometry('750x500')
window.minsize(1000, 500)
window.title("Générateur de QCM -- License CC-BY-NC-ND")
window.config(background='#A2A2A2')
window.grid_rowconfigure(20, weight=1)
window.grid_columnconfigure(3, weight=1)
Label(window, text="Générateur de QCM", font=('CLARENDON', 20), bg='#A2A2A2').grid(row=0, column=0, ipadx=15, ipady=20,
                                                                                   sticky=NW)
Label(window, text="by Leween MASSIN", font=('CALISTO MT', 5), bg='#A2A2A2').grid(row=20, column=0, sticky=SW)
Label(window,
      text="Pour commencer:\n- Mettre le script dans le même dossier que le fichier csv\n- Inserer le nom\n- Choisir le nombre de copie\n- Appuyer sur générer",
      font=('CONSOLAS', 10), bg='#A2A2A2').grid(row=0, column=1, ipady=15, sticky=N)
frame_nbr_qcm = Frame(window, bg='#A2A2A2')
nbr_qcm_content = IntVar()
Scale(frame_nbr_qcm, variable=nbr_qcm_content, bg='#74637B', from_=1, to_=40, width=35, length=200).pack()
Label(frame_nbr_qcm, text='Faites défiler le curseur pour\nchoisir le nombre de copie', font=('CONSOLAS', 10),
      bg='#A2A2A2').pack(side=BOTTOM)
frame_name_csv = Frame(window, bg='#A2A2A2')
name_content = StringVar()
Entry(frame_name_csv, textvariable=name_content, bg='#74637B').pack()
Label(frame_name_csv, text='Noter le nom du fichier, sans son extension.\nexemple.csv --> erreur\nexemple --> OK',
      font=('CONSOLAS', 10), bg='#A2A2A2').pack(side=BOTTOM)
gen_button = Button(window, text="Générer", font=('FUTURA', 15), bg='#7F6D87', command=launch_generation)
frame_nbr_qcm.grid(row=0, column=2, ipadx=15, sticky=NE)
frame_name_csv.grid(row=2, column=0, sticky=E, ipadx=15)
gen_button.grid(row=1, column=1)
window.mainloop()
