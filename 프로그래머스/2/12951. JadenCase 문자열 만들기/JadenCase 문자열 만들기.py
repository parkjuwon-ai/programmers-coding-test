def solution(s):
    lower_word = s.lower()
    split_word = lower_word.split(' ')
    capitalized_word = [w.capitalize() for w in split_word]
    answer=' '.join(capitalized_word)

    return answer