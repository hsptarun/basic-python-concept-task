def find_anagrams(word, candidates):
    target = word.lower()
    tsort = sorted(target)
    result = []
    for candidate in candidates:
        clower = candidate.lower()
        if clower == target:
            continue
        if sorted(clower) == tsort:
            result.append(candidate)
    return result
        
    pass
