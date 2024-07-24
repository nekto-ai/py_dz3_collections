# MODULE 3


def get_sequence():
    sequence = input("Enter a sequence of whole numbers separated by comma or semicolon or slash: ")
    if sequence.find(",") > 0:
        separator = ","
    elif sequence.find(";") > 0:
        separator = ";"
    elif sequence.find("/") > 0:
        separator = "/"
    else:
        print("Invalid input. Please enter a sequence of whole numbers separated by comma or semicolon or slash.")
    return [int(num) for num in sequence.split(separator)]


list_one = get_sequence()
list_two = get_sequence()

print(f"List one: {list_one}")
print(f"List two: {list_two}")

for i in range(len(list_two)):
    while list_two[i] in list_one:
        list_one.remove(list_two[i])

print(f"Resulted unique elements: {list_one}")