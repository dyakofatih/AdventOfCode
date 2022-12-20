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

# Sort the Elves by calorie count in descending order
elves = sorted(calories.items(), key=lambda x: x[1], reverse=True)

# Get the top three Elves
top_elves = elves[:3]

# Calculate the total number of calories carried by the top three Elves
total_calories = sum([calorie_count for _, calorie_count in top_elves])

# Print the result
print(
    f"The top three Elves are carrying a total of {total_calories} calories.")
