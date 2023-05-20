
"""
Słowa sklejamy z sylab w następujący sposób:

słowo:

"abac"

... trzeba złożyć z 2-literowych "sylab"
ab←→ba -> aba
aba←→ac -> abac

(czyli dołączana sylaba 2-literowa ma mieć taką pierwszą literę, jak ostatnia litera słowa do którego jest dołączana)

"""



def split_to_syllables(word: str) -> list[str]:
<<<<<<< Updated upstream
    #todo: your solution hered
    splited = word.split()
    output = ""
    for x in range(len(splited)):
         output = splited[x-1] + splited[x]
    return output

=======
    
    syllist = []

    for syllable in range(len(word)):
        print(syllable)
        
        if syllable+1 < len(word):
            syllist.append(word[syllable]+word[syllable+1])
    
    return(syllist)
    

print(split_to_syllables("aabb"))
>>>>>>> Stashed changes
