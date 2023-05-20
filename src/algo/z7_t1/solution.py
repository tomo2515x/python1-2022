
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
    #todo: your solution hered
    splited = word.split()
    output = ""
    for x in range(len(splited)):
         output = splited[x-1] + splited[x]
    return output

