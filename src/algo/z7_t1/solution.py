
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
    syllist = []

    for syllable in range(len(word)):

        if syllable+1 < len(word):
            syllist.append(word[syllable]+word[syllable+1])
    
    return syllist
    



