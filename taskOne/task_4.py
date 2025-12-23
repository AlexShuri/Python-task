n = int(input())
students = {}
for _ in range(n):
    line = input().split()
    name = line[0]
    marks = list(map(float, line[1:]))
    students[name] = marks

student_name = input()

result = 0
len_student = len(students.setdefault(student_name, []))
list_student = students.setdefault(student_name, [])
for i in list_student:
    result += i

print(f"{(result / len_student):.2f}")