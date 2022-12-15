sequence = []
with open("./data.txt", "r") as data:
    for char in data.readline(14):
        sequence.append(char)
    
    if len(set(sequence)) == 14:
        print("14")
        exit

    print(sequence)
    for i, char in enumerate(data.readline()):
        sequence.pop(0)
        sequence.append(char)
        if len(set(sequence)) == 14:
            print(sequence)
            print(i+15)
            break
