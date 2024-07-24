# MODULE 2

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

our_list = get_sequence()
print(f"Entered list: {our_list}")

our_list.sort()
print(f"Sorted list: {our_list}")

duplicate_indexes = []
for i in range(len(our_list)):
    if our_list[i] == our_list[i-1] and i != 0:
        duplicate_indexes.append(i-1)
        duplicate_indexes.append(i)

result_list = []
for j in range(len(our_list)):
    if j not in duplicate_indexes:
        result_list.append(our_list[j])


print(f"Resulted unique elements: {result_list}")