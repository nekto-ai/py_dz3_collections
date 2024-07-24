# MODULE 1

def get_total_elements():
    total_elements = input("Enter the total number of elements in the sequence: ")
    if total_elements.isnumeric():
        return int(total_elements)
    else:
        print("Invalid input. Please enter a valid number.")
        return get_total_elements()
    
local_elements = []
for i in range(get_total_elements()):
    element = input(f"Enter element {i+1}: ")
    local_elements.append(float(element))

# sort our list
local_elements.sort()


print(f"Sorted list:{local_elements}")