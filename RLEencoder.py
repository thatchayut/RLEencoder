input_string = input(" Enter your input string : ")

# split string to characters in order to check adjacent character easier
input_characters = list(input_string)

# define array used to collect RLE
RLE = []

# iterate through input characters and count
# define boolean used to track whether adjacent character is the same
check_same_character = False
number_of_input_charaters = len(input_characters)

for character_index in range(0, number_of_input_charaters):
    if (character_index == 0):
        character_occurrence = []
        character_counter = 1
        character_occurrence.append(str(input_characters[character_index]))
        character_occurrence.append(character_counter)
        RLE.append(character_occurrence)
    else:
        number_of_RLE_element = len(RLE)
        previous_character_in_RLE = RLE[number_of_RLE_element - 1][0]
        current_character = input_characters[character_index]

        if (previous_character_in_RLE == current_character):
            RLE[number_of_RLE_element - 1][1] += 1
            check_same_character = True
        else: 
            check_same_character = False

        if (check_same_character is False):
            character_occurrence = []
            character_counter = 1
            character_occurrence.append(str(input_characters[character_index]))
            character_occurrence.append(character_counter)
            RLE.append(character_occurrence)
    # print(RLE)
print(" RLE result : ")

for RLE_index in range(0, len(RLE)):
    RLE_character = RLE[RLE_index][0]
    RLE_character_occurrence = RLE[RLE_index][1]

    print(RLE_character, end = " ")
    print(RLE_character_occurrence, end = " ")
print()



    