def sort(word, start=0, end=None):
    if not end:
        end = len(word)
    if (end - start) > 1:
        middle = (start + end) // 2
        sort(word, start, middle)
        sort(word, middle, end)
        merge(word, start, middle, end)

def merge(word, start, middle, end):
    left_part = word[start:middle]
    right_part = word[middle:end]

    left_index, right_index = 0, 0

    for main_index in range(start, end):
        if left_index >= len(left_part):
            word[main_index] = right_part[right_index]
            right_index = right_index + 1
        elif right_index >= len(right_part):
            word[main_index] = left_part[left_index]
            left_index = left_index + 1
        elif left_part[left_index] < right_part[right_index]:
            word[main_index] = left_part[left_index]
            left_index = left_index + 1
        else:
            word[main_index] = right_part[right_index]
            right_index = right_index + 1

def is_anagram(first_string, second_string):

    if not first_string and not second_string:
        return first_string, second_string, False
    
    first_lowered = list(first_string.lower())
    second_lowered = list(second_string.lower())


    sort(first_lowered)
    sort(second_lowered)

    first_joined = "".join(first_lowered)
    second_joined = "".join(second_lowered)

    return first_joined, second_joined, first_joined == second_joined
