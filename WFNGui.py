from tkinter import *

window = Tk()

window.title("COM creator for WFN")

window.geometry('600x150')

lbl = Label(window, text="This is a program that creates com files for wfn acquisition using xyz files")
lbl2 = Label(window,text="Make sure the folder contains ONLY xyz files and this program before running it.")
lbl6 = Label(window,text="xyz files NEED to have two line before the matrix and one after.")
lbl3 = Label(window,text="Created by Michał Pocheć, PtysioCreations 2022")
lbl4 = Label(window,text="Specify functional:")
lbl5 = Label(window,text="Specify basis set:")
txt = Entry(window,width=15)
txt2 = Entry(window,width=15)
lbl.grid(column=0, row=0)
lbl2.grid(column=0, row=1)
lbl6.grid(column=0, row=2)
lbl4.grid(column=0, row=3)
txt.grid(column=1, row=3)
lbl5.grid(column=0, row=4)
txt2.grid(column=1, row=4)
def clicked():
    import os
    newline = os.linesep
    dirPath = r"./"
    result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
    ile = len(result)
    zrob = 0
    funkc = txt.get()
    baza = txt2.get()
    print("You have chosen " + funkc + "/" + baza + "\n\n")
    LOGFILE = open("LOGFILE.txt", "a")
    LOGFILE.write("You have chosen " + funkc + "/" + baza + "\n\n")
    for x in range(0, ile):
        print(result[x])
        argu = result[x]
        argu2 = argu.replace("xyz", "log")
        argu3 = argu.replace("xyz", "wfn")
        argu4 = argu.replace("xyz", "com")
        file = open(result[x], "r")
        lines = file.readlines()
        lines[0] = "# " + funkc + "/" + baza + " sp scf=tight pop=hirshfeld out=wfn \n \n"
        lines[1] = argu2 + "\n" + "\n" + "0 1 \n"
        lines[-1] = lines[-1] + "\n" + argu3 + "\n\n\n"
        try:
            efekt = open(argu4, "x")
            efekt.writelines(lines)
            print("Succesful creation of " + argu4)
            zrob += 1
        except FileExistsError:
            ile -= 1
        LOGFILE = open("LOGFILE.txt", "a")
        LOGFILE.write(
            str(zrob) + " out of " + str(ile) + ": Succesful creation of " + argu4 + " from " + result[x] + "\n")
        print(str(zrob) + " out of " + str(ile))


btn = Button(window, text="Run", command=clicked)

btn.grid(column=1, row=5)
lbl3.grid(column=0, row=6)
window.mainloop()



