import os
newline = os.linesep
dirPath = r"./"
result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
print(result)
ile = len(result)
for x in range(0,ile):
    argu = result[x]
    argu2 = argu.replace("com", "xyz")
    argu3 = argu.replace("txt", "a")
    argu4 = argu.replace("xyz", "com")
    print("Analyzing: " + argu)
    if argu == argu2:
        print(argu + ": not a COM file")
    elif argu == argu4:
        file = open(argu, "r")
        lines1 = file.readlines()
        file = open(argu2, "r")
        lines2 = file.readlines()
        if lines1[8] == lines2[5]:
            print(argu + " same as " + argu2)
            info = open ("Test.txt", "a")
            info.write(argu + " same as " + argu2 + "\n")
        else:
            print(argu + " different than " + argu2)

