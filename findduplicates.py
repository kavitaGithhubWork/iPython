def findduplicate(dupl):
    seen = set()
    dup = set()
    for item in dupl:
        if item in seen:
            dup.add(item)
        else:
            seen.add(item)

    return list(dup)


print(findduplicate('mummy'))