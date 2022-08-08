from tkinter import *

window = Tk()

window.title("XYZ Creator")

window.geometry('500x70')

lbl = Label(window, text="This is a program that extracts xyz files from the last point of Gaussian log files")
lbl2 = Label(window,text="Make sure the folder contains ONLY log files and this program before running it.")
lbl3 = Label(window,text="Created by Michał Pocheć, PtysioCreations 2022")
lbl.grid(column=1, row=0)
lbl2.grid(column=1, row=1)

def clicked():
    import os
    newline = os.linesep
    dirPath = r"./"
    result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
    ile = len(result)
    print(ile)
    location = "./"
    key = "Center     Atomic      Atomic             Coordinates (Angstroms)"
    key2 = "symmetry adapted cartesian basis functions of"
    zrob = 0
    for y in range(0, ile):
        number = 0
        argu = result[y]
        argu2 = argu.replace("log", "xyz")
        file = open(result[y], "r")
        lines = file.readlines()
        print(argu)
        app = []
        app2 = []
        xyz = ["\n", "\n"]
        for number, line in enumerate(lines, 0):
            if key in line:
                app.append(number)
        print(app)
        for number, line in enumerate(lines, 0):
            if key2 in line:
                app2.append(number)
        print(app2)
        final1 = app[-1]
        final2 = app2[-1]
        start = int(final1) + 3
        finish = int(final2) - 3
        print(final1)
        print(final2)
        print(start)
        print(finish)
        for x in range(start, finish):
            str1 = lines[x]
            strp2 = str1[30:70]
            strp = str1[17]
            if strp == "6":
                strp = "C"
            elif strp == "1":
                strp = "H"
            elif strp == "7":
                strp = "N"
            elif strp == "8":
                strp = "O"
            elif strp == "5":
                strp = "Br"
                strp2 = str1[31:70]
            else:
                print("ERROR")
            strf = strp + strp2 + "\n"
            xyz.append(strf)
        print(xyz)
        zrob += 1
        LOGFILE = open(argu2, "a")
        LOGFILE.writelines(xyz)
        LOGFILE2 = open("LOGFILE.txt", "a")
        LOGFILE2.write(str(zrob) + " out of " + str(ile) + ": Succesful creation of " + argu2 + " from " + argu + "\n")
        print(zrob)

btn = Button(window, text="Run", command=clicked)

btn.grid(column=2, row=1)
lbl3.grid(column=1, row=3)
window.mainloop()



