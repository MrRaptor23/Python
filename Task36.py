def change_marks(marks: list[int]) -> list[int]:
    """Рекурсивная замена макисмальных оценок минимальными"""

    max_mark = max(marks)
    min_mark = min(marks)
    marks[marks.index(max_mark)] = min_mark

    if max_mark not in marks:
        return marks
    return change_marks(marks)


print(change_marks([1, 2, 3, 1, 1, 3, 4, 4, 5, 4]))

a = [1, 2, 3, 1, 1, 3, 4, 5, 5, 5]
print(a.index(5))

a[a.index(5)] = 1000
print(a)