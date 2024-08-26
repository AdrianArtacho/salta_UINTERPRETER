import random

def main(my_list, default=''):
    # If default is an empty string, remove a random element
    if default == '':
        index_to_remove = random.randint(0, len(my_list) - 1)
    else:
        # Otherwise, remove the element at the index specified by default
        index_to_remove = int(default) - 1  # Convert to 0-based index
    
    # Remove the element from the list
    modified_list = my_list[:index_to_remove] + my_list[index_to_remove+1:]
    return modified_list

if __name__ == "__main__":       
    # Example usage:
    my_list = [1, 2, 3, 4, 5]
    print(main(my_list, default=2))  # Removes the second element
    print(main(my_list, default=''))  # Removes a random element
