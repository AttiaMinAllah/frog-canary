import re

def alphanumeric_sort(input_string):
    # Extract numbers as multi-digit integers
    numbers = re.findall(r'\d+', input_string)
    # Remove numbers from input string
    non_numbers = re.sub(r'\d+', '', input_string)

    # Separate characters into lowercase, uppercase, and others
    lowercase = sorted([char for char in non_numbers if char.islower()])
    uppercase = sorted([char for char in non_numbers if char.isupper()])
    others = sorted([char for char in non_numbers if not char.isalnum()])

    # Convert numbers to integers and sort
    sorted_numbers = sorted(numbers, key=int)

    # Combine all sorted elements
    result = ''.join(sorted_numbers) + ''.join(lowercase) + ''.join(uppercase) + ''.join(others)
    return result

if __name__ == "__main__":
    input_string = input("Enter a string to sort: ")
    print("Sorted Output ->", alphanumeric_sort(input_string))
