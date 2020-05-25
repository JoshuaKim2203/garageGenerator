import requests
sesh = requests.session()
import tkinter as tk


class garage():
    def __init__(self, master):
        self.master = master
    def changeGarage(self, event):
        if event.keysym == "Return":
            self.text = ("Garages Copied to your account!")
            tk.Label(self.master, text = self.text).grid(row=4)
            self.username = self.e1.get()
            self.password = self.e2.get()
            self.garageSpaces = int(self.e3.get())
            if(self.garageSpaces > 30):
                self.garageSpaces = 30
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            log = sesh.post("https://www.nitrotype.com/api/login", data = {"username": self.username, "password": self.password})
            print(log.text)
            garageString = "garage%5B0%5D=17&"
            uhash = sesh.cookies["ntuserrem"]
            for i in range(1, (self.garageSpaces * 30)-1, 1):
                garageString = garageString + "garage%5B"  + str(i) + "%5D=&"
            garageString = garageString + "uhash=" + uhash
            changeGarage = sesh.post("https://www.nitrotype.com/api/cars-arrange", data = garageString, headers = headers)
            print(changeGarage.text)
    def run_program(self):
        tk.Label(self.master, text="Username").grid(row=0)
        tk.Label(self.master, text="Password").grid(row=1)
        tk.Label(self.master, text="Spaces").grid(row=2)
        self.text = "Press ENTER to generate garages!"
        tk.Label(self.master, text = self.text).grid(row=3)
        
        self.e1 = tk.Entry(self.master)
        self.e2 = tk.Entry(self.master)
        self.e3 = tk.Entry(self.master)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)

        self.master.bind("<KeyPress-Return>",self.changeGarage)
        self.master.mainloop()


master = tk.Tk()
gen = garage(master)
gen.run_program()
