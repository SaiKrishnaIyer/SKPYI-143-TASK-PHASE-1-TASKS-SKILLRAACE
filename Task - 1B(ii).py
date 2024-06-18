def remove_common_letters(name1, name2):
    list1 = list(name1)
    list2 = list(name2)
    
    for letter in list1[:]:
        if letter in list2:
            list1.remove(letter)
            list2.remove(letter)
    
    return ''.join(list1), ''.join(list2)

def flames_game(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    name1, name2 = remove_common_letters(name1, name2)
    
    combined_length = len(name1 + name2)
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    
    while len(flames) > 1:
        split_index = combined_length % len(flames) - 1
        
        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]
    
    return flames[0]

# Example usage
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

relationship = flames_game(name1, name2)
print(f"The relationship between {name1} and {name2} is: {relationship}")
