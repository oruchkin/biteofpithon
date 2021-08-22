s = "abcabcabcabc"
s = "abababab"

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # 26



times_counter = 0
letter_counter =0



for i in range(0, (len(s)-2)):
    if s[letter_counter]+s[letter_counter+1]+s[letter_counter+2] == "abc":
        times_counter += 1
    letter_counter +=1
    
print(times_counter)



#old
def solution(s):
    # Your code here

    times_counter = 0
    letter_counter = 0
    for i in range(0, (len(s)-2)):
        if s[letter_counter]+s[letter_counter+1]+s[letter_counter+2] == "abc":
            times_counter += 1
        letter_counter += 1
    return times_counter
