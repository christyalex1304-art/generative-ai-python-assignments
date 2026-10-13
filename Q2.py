# Student Marks Analysis

marks = [78, 35, 92, 40, 61]

marks_tuple = tuple(marks)

print("List of marks:", marks)
print("Tuple of marks:", marks_tuple)

print("List data type:", type(marks))
print("Tuple data type:", type(marks_tuple))

print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))

passed_count = (
    (marks[0] >= 40)
    + (marks[1] >= 40)
    + (marks[2] >= 40)
    + (marks[3] >= 40)
    + (marks[4] >= 40)
)

print("Students scoring at least 40:", passed_count)

valid_marks = (
    0 <= marks[0] <= 100
    and 0 <= marks[1] <= 100
    and 0 <= marks[2] <= 100
    and 0 <= marks[3] <= 100
    and 0 <= marks[4] <= 100
)

print("Are all marks valid?", valid_marks)

marks[0] = 80

print("List after changing the first mark:", marks)

# A tuple cannot be changed.
# Uncomment the next line and run it separately to see the error.
# marks_tuple[0] = 80
```
