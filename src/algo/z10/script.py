import string
import random
def encode(s:str):
    encoded = []
    for character in range(len(s)):
        letters = list(string.ascii_lowercase)
        letters.remove(s[character])
        # print(letters)
        encoded.append(s[character] + ''.join(random.choice(letters) for i in range(random.randint(1,9))) + s[character])
    
    return ''.join(encoded)

a = encode("aa")
print(a)

print("------------")

def decode(s:str):
    predicted = s[0]
    predicted_ct = 0
    decoded_string = []
    for letter_in in range(len(s)):
        if s[letter_in] == predicted:
            predicted_ct += 1
        
        if predicted_ct == 2:
            predicted_ct = 0
            decoded_string.append(predicted)
            if letter_in+1 < len(s):
                predicted = s[letter_in+1]
    
    return ''.join(decoded_string)

print(decode(a))