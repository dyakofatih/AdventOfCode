# Open the input file
with open("data.txt", "r") as f:
    # Initialize an empty dictionary to store the Elves and their calorie counts
    calories = {}

    # Initialize a variable to store the current Elf's index
    current_elf = 0

    # Iterate over the lines in the file
    for line in f:
        # If the line is empty, start a new Elf
        if not line.strip():
            current_elf += 1
            continue

        # If the current Elf is not yet in the dictionary, add it
        if current_elf not in calories:
            calories[current_elf] = 0

        # Convert the calorie count to an integer and add it to the current Elf's total
        calories[current_elf] += int(line.strip())

# Find the Elf with the most calories
max_calories = 0
max_elf = 0
for elf, calorie_count in calories.items():
    if calorie_count > max_calories:
        max_calories = calorie_count
        max_elf = elf

# Print the result using the Elf's index
print(f"Elf {max_elf + 1} is carrying the most calories ({max_calories}).")
