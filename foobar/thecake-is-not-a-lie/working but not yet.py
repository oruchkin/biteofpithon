#s = "abcabcabcabcabc"
# s = "abababab"
#s = "MNONMMNMNNM"
#s = "abababab"

#s = "DEFGHHHG"
s = "abcabca"

alphabet1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # 26


def solution(s):
    alphabet2 = "abcdefghijklmnopqrstuvwxyz"

    sequence = ""
    for i in range(0, (len(s)-2)):
        cycle = 0

        first_letter = s.lower()[cycle]
        second_letter = s.lower()[cycle + 1]
        third_letter = s.lower()[cycle + 2]
        fourth_letter = s.lower()[cycle + 3]
        fifth_letter = s.lower()[cycle + 4]

        print(first_letter, second_letter,
              third_letter, fourth_letter, fifth_letter)

        sequence = sequence + first_letter
        letter_number = alphabet2.find(first_letter)

        cycle += 1

        if second_letter == alphabet2[letter_number + 1]:
            sequence += second_letter
        else:
            break

        if third_letter == alphabet2[letter_number + 2]:
            sequence += third_letter
        else:
            break

        if fourth_letter == alphabet2[letter_number + 3]:
            sequence += fourth_letter
        else:
            break

        if fifth_letter == alphabet2[letter_number + 4]:
            sequence += fifth_letter
        else:
            break


    print(f"последовалтельность {sequence}")

    result = s.count(sequence)
    print(result)


solution("abcascbaabccba")
