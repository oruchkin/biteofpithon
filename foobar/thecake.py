s = "abcabcabcabc"
s = "abababab"


times_counter = 0
letter_counter =0
for i in range(0, (len(s)-2)):
    if s[letter_counter]+s[letter_counter+1]+s[letter_counter+2] == "abc":
        times_counter += 1
    letter_counter +=1
    
print(times_counter)

