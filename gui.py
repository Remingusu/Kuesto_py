from tkinter import *


class MainGUI:
    def __init__(self):
        window = Tk()
        window.geometry("700x500")
        window.minsize(500, 300)
        window.title("Kuesto -- License CC-BY-NC-ND")


class SecondGUI:
    def __init__(self):
        window = Tk()
        window.geometry("500x700")
        window.minsize(300, 500)
        window.title("Kuesto")
