import random
import tkinter as tk

root = tk.Tk()
root.resizable(False,False)
root.attributes("-fullscreen", False)
root.overrideredirect(0)
root.geometry("600x200+600+200")
root.title("Game")

europenames = ["Albania","Alemania","Andorra","Armenia","Austria",
    "Azerbaiyán","Bélgica","Bielorrusia","Bosnia y Herzegovina",
    "Bulgaria","Chipre","Ciudad del vaticano","Croacia","Dinamarca","Eslovaquia",
    "Eslovenia","España","Estonia","Finlandia","Francia","Georgia",
    "Grecia","Hungría","Irlanda","Islandia","Italia","Kosovo","Letonia",
    "Liechtenstein","Luxemburgo","Macedonia del Norte","Malta","Moldavia","Mónaco",
    "Montenegro","Noruega","Holanda/P. Bajos","Polonia","Portugal","Reino Unido",
    "Rep. Checa","Rumania","San Marino","Serbia","Suecia","Suiza","Ucrania"]

asianames = ["Afganistán","Arabia Saudita","Bangladés","Baréin","Birmania","Brunéi",
             "Bután","Camboya","Catar","China","Cor. Norte","Cor. Sur","Em. Árabes Unidos",
             "Filipinas","India","Indonesia","Irak","Israel","Japón","Jordania",
             "Kazajistán","Kiriguistán","Kuwait","Laos","Líbano","Malasia","Maldivas",
             "Maldivas","Mongolia","Nepal","Omán","Pakistán","Palestina","Qatar",
             "Rusia","Singapur","Siria","Sri Lanka","Tayikistán","Tailandia",
             "Timor Oriental","Turmekistán","Turquía","Uzbekistán","Vietnam",
             "Yemen"]

africanames = ["Angola","Argelia","Benín","Botsuana","Burkina Faso","Burundi",
               "Cabo Verde","Camerún","Chad","Comoras","Congo","Costa de Marfil",
               "Egipto","Eritrea","Eswatini/Suazilandia","Etiopía","Gabón","Gambia",
               "Ghana","Guinea","Guinea-Bissau","Guinea Ecuatorial","Kenia","Lesoto",
               "Liberia","Libia","Madagascar","Malaui","Malí","Marruecos","Mauricio",
               "Mauritania","Mozambique","Namibia","Níger","Nigeria","Rep. Centroafricana",
               "Ruanda","Santo Tomé y Príncipe","Senegal","Seychelles","Sierra Leona","Somalia",
               "Sudáfrica","Sudán","Sudán del Sur","Tanzania","Togo","Túnez","Uganda","Yibuti","Zambia",
               "Zimbabue"]

americanames = ["Canadá","Estados Unidos","México","Belice","Costa Rica",
                "El Salvador","Guatemala","Honduras","Nicaragua","Panamá",
                "Antigua y Barbuda","Bahamas","Cuba","Dominica","Granada",
                "Haití","Jamaica","Puerto Rico","Rep. Dominicana",
                "San Cristóbal y Nieves","Santa Lucía","San Vicente y las Granadinas",
                "Trinidad y Tobago","Argentina","Bolivia","Brasil","Chile","Colombia","Ecuador","Guyana",
                "Paraguay","Perú","Surinam","Uruguay","Venezuela"]

oceanianames = ["Australia","Fiyi","Islas Marshall","Islas Salomón","Kiribati","Micronesia",
                "Nauru","Nueva Zelanda","Palaos","Papúa Nueva Guinea","Samoa",
                "Tonga","Tuvalu","Vanuatu","Guam","Islas Cocos","Islas Cook",
                "Islas Marianas del Norte","Islas Pitcairn","Nueva Caledonia",
                "Niue","Polinesia Francesa","Samoa Americana","Tokelau","Wallis y Futuna"]

allnames = europenames + africanames + asianames + americanames + oceanianames

score = 0
whilepregs = 0

def NextQuestion():
    global country, whilepregs, score
    if whilepregs >= 10:
        root.destroy()
        root2 = tk.Tk()
        root2.resizable(False,False)
        root2.attributes("-fullscreen", False)
        root2.overrideredirect(0)
        root2.title(string="Results")
        root2.geometry("400x200+600+200")
        tk.Label(root2, text=f"Puntuación: {score}/10", font="Arial 20", pady=40).pack()
        def StartAgain():
            root2.destroy()
            import main
        def Close():
            root2.destroy()
        returnBtn = tk.Button(root2, text="Volver", height=4,width=12, command=StartAgain)
        closeBtn = tk.Button(root2, text="Cerrar", height=4,width=12, command=Close)

        returnBtn.place(x=10,y=120)
        closeBtn.place(x=290,y=120)
    else:
        whilepregs += 1
        country = random.choice(allnames)
        label.config(text=country)

def BtnClick(continent):
    global score, country
    global europenames, americanames, oceanianames, africanames, asianames
    if continent == "Europa" and country in europenames:
        score += 1
        europenames.remove(country)
    elif continent == "América" and country in americanames:
        score += 1
        americanames.remove(country)
    elif continent == "Oceanía" and country in oceanianames:
        score += 1
        oceanianames.remove(country)
    elif continent == "África" and country in africanames:
        score += 1
        africanames.remove(country)
    elif continent == "Asia" and country in asianames:
        score += 1
        asianames.remove(country)
    print(f"Puntuación: {score}, Pregunta: {whilepregs}")
    NextQuestion()

label = tk.Label(root, text="", font="Arial 20", pady=40)
label.pack()

euBtn = tk.Button(root, text="Europa", height=4, width=12, command=lambda: BtnClick("Europa"))
amBtn = tk.Button(root, text="América", height=4, width=12, command=lambda: BtnClick("América"))
ocBtn = tk.Button(root, text="Oceanía", height=4, width=12, command=lambda: BtnClick("Oceanía"))
afBtn = tk.Button(root, text="África", height=4, width=12, command=lambda: BtnClick("África"))
asBtn = tk.Button(root, text="Asia", height=4, width=12, command=lambda: BtnClick("Asia"))

euBtn.place(x=5, y=125)
amBtn.place(x=130, y=125)
ocBtn.place(x=255, y=125)
afBtn.place(x=380, y=125)
asBtn.place(x=500, y=125)

NextQuestion()
root.mainloop()