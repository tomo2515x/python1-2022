"""
Semantic versioning
https://devopedia.org/images/article/279/7179.1593248779.png

{Major}.{Minor}.{Patch}

np.

'1.3.6' oznacza major=1, minor=3, path=6


"""


def get_latest(versions: list[str]) -> str:
    v = []
    for i in versions:
        v.append("".join(i.split(".")))
    return versions[v.index(max(v))]



def next_version(version: str, level: int) -> str:
    v = version.split(".")

    if level == 0:
        return str(int(v[0])+1)+".0.0"
    elif level == 1:
        return str(v[0])+"."+str(int(v[1])+1)+".0"
    elif level == 2:
        return str(v[0])+"."+str(v[1])+"."+str(int(v[2])+1)
    else:
        print("out of range")
    return False

