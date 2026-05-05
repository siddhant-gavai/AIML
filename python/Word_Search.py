line = 1
data = True
with open("sample.txt", "r") as f:
    while data:
        data = f.readline()

        if "Python" in data:
            print(f"Python word exists in the line {line}")
            break    

        line = line + 1 