
"""
Słowa sklejamy z sylab w następujący sposób:

słowo:

"abac"

... trzeba złożyć z 2-literowych "sylab"
ab←→ba -> aba
aba←→ac -> abac

(czyli dołączana sylaba 2-literowa ma mieć taką pierwszą literę, jak ostatnia litera słowa do którego jest dołączana)

Zadanie -- mamy dostępny zbiór sylab, oraz pewne słowo `word`; pytanie -- czy przy użyciu tych sylab
(każdą można użyć dowolną liczbę razy, również 0) można utworzyć dane słowo.

"""

def split_to_syllables(word: str) -> list[str]:
    syllist = []

    for syllable in range(len(word)):

        if syllable+1 < len(word):
            syllist.append(word[syllable]+word[syllable+1])
    
    return syllist

def construct_word(syllables: set[str], word: str) -> bool:
    syllist = []
    for syllable in range(len(word)):
        
        if syllable+1 < len(word):
            syllist.append(word[syllable]+word[syllable+1])

    if set(syllist) & syllables == set(syllist):
        return True
    return False


print(construct_word({"aa"}, "aaaaaaaa"))