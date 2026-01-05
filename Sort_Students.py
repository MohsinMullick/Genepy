
students = [(85, "Susan"), (6, "Joshua"), (37, "Jeanette")]
# Part 1: Sort by mark in descending order
def sort_by_mark(students):
    return sorted(students, key=lambda student: student[0], reverse=True)
# Part 2: Sort by name in ascending order
def sort_by_name(students):
    return sorted(students, key=lambda student: student[1])
# ------------------ Testing ------------------
print("Original list:")
print(students)
print("\nSorted by mark (descending):")
print(sort_by_mark(students))
print("\nSorted by name (ascending):")
print(sort_by_name(students))
