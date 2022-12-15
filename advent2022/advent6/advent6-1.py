sequence = []
with open("./data.txt", "r") as data:
    for char in data.readline(4):
        sequence.append(char)
    
    if len(set(sequence)) == 4:
        print("4")
        exit

    print(sequence)
    for i, char in enumerate(data.readline()):
        sequence.pop(0)
        sequence.append(char)
        if len(set(sequence)) == 4:
            print(sequence)
            print(i+5)
            break
