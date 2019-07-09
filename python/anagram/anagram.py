from collections import Counter


def detect_anagrams(word, candidates):
    if word.istitle():
        word = word.lower()
    word_counter = Counter(word)

    anagrams = []
    for candidate in candidates:
        tmp_candidate = candidate.lower() if candidate.istitle else candidate
        if word_counter == Counter(tmp_candidate):
            anagrams.append(candidate)

    return anagrams

