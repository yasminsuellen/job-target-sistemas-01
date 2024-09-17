def check_letter_a(string):
    # Counts the number of occurrences of 'a' and 'A' in the string
    count_a = string.lower().count('a')

    # Checks if the letter 'a' is present and displays the quantity
    if count_a > 0:
        return f"The letter 'a' appears {count_a} time(s) in the string."
    else:
        return "The letter 'a' was not found in the string."


# Requests user input
user_input = input("Enter a string: ")

# Display the result
print(check_letter_a(user_input))