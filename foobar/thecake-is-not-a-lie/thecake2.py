#s = "abcabcabcabcabc"
# s = "abababab"
#s = "MNONMMNMNNM"
#s = "abababab"

#s = "DEFGHHHG"
s = "abcabcabcabc"

alphabet1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # 26
alphabet2= "abcdefghijklmnopqrstuvwxyz"



for i in range(0, (len(s)-2)):
    cycle = 0
    sequence = ""

    first_letter = s.lower()[cycle]
    second_letter = s.lower()[cycle + 1]
    third_letter = s.lower()[cycle + 2]
    #print(f"3rd leter {third_letter}")
    fourth_letter = s.lower()[cycle + 3]
    #print(f"4 leter {fourth_letter}")

    #print(f"first letter: {first_letter}")
    
    sequence = sequence + first_letter
    letter_number = alphabet2.find(first_letter)
    #print(f"letter number: {letter_number}")    
    cycle += 1

    if second_letter == alphabet2[letter_number + 1]:
        sequence += second_letter
        if third_letter == alphabet2[letter_number + 2]:
            sequence += third_letter
            if fourth_letter == alphabet2[letter_number + 3]:
                sequence += fourth_letter

# #second var
#     if second_letter == alphabet2[letter_number + 1]:
#         sequence += second_letter
#         if third_letter == alphabet2[letter_number + 2]:
#             sequence += third_letter
#             if fourth_letter == alphabet2[letter_number + 3]:
#                 sequence += fourth_letter
#             else:
#                 break



#print(f"последовалтельность {sequence}")

times_counter = 0
letter_counter = 0

length_sequence = len(sequence)

result = s.count(sequence)
print(result)


