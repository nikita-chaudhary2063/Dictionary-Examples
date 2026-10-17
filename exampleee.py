'''Find all subjects with marks above a target
print only subjects with marks above 80.'''
scores = {
    "Python": 75,
    "Java": 90,
    "Math": 45,
    "English": 82
}
count=0
for subject,mark in scores.items():
    if mark>80:
        count+=1
print(count)

'''Find the subject with the lowest marks using min()'''
lowest=min(scores.values())
print(lowest)

'''Find the total number of subjects'''
count=0
for subject in scores.keys():
    count+=1
print(count)

'''Handle an empty dictionary
if we calculate the average: This causes a ZeroDivisionError because len(scores) is 0, and we cannot divide by zero.
How do we prevent the error?
Check whether the dictionary contains any subjects before calculating the average.'''

scores = {}

if len(scores) > 0:
    average = sum(scores.values()) / len(scores)
    print("Average:", average)
else:
    print("No marks available.")

'''Use .get() to safely access dictionary values'''
student = {
    "name": "Nikita",
    "marks": 85
}

print(student.get("marks")) #it gives value if find keys if not it throws keyerror
print(student.get("age")) #it gives none if it doesn't find keys

'''Clear an entire dictionary with .clear()'''
student = {
    "name": "Nikita",
    "marks": 95,
    "age": 20
}

student.clear()

print(student)

'''Copying a dictionary with .copy()'''
student = {"name": "Nikita", "marks": 85}

new_student = student.copy()
new_student["marks"] = 100

print(student["marks"])      # 85
print(new_student["marks"])  # 100//

'''The difference between .copy() and assignment'''
student = {"name": "Nikita", "marks": 85}

new_student = student
new_student["marks"] = 100

print(student["marks"]) #print 100 coz it used assignment not copy

'''Get all dictionary keys as a list'''
student = {"name": "Nikita", "marks": 85, "age": 20}
keys = list(student.keys())
print(keys)

'''Get the values as a list'''
student = {"name": "Nikita", "marks": 85}
values = list(student.values())
print(values)

'''Get values and keys together as a list'''
student = {"name": "Nikita", "marks": 85}
print(list(student.items()))

'''Loop through a dictionary using .items()'''
student = {"name": "Nikita", "marks": 85}
for key, value in student.items():
    print(key, value)

'''Print only selected dictionary values'''
scores = {
    "Python": 85,
    "Math": 35,
    "English": 75
}
for subject, mark in scores.items():
    if mark >= 40:
        print(subject, mark)

'''Store in list'''
scores = {
    "Python": 85,
    "Math": 30,
    "English": 65,
    "Java": 25,
    "Science": 50
}
passed_subjects = []
for subject, mark in scores.items():
    if mark >= 40:
        passed_subjects.append(subject)
print(passed_subjects)

'''Finding subjects within a mark range'''
scores = {
    "Python": 85,
    "Math": 65,
    "English": 40,
    "Java": 25,
    "Science": 79
}
subjects = []
for subject, mark in scores.items():
    if mark >= 40 and mark <= 79:
        subjects.append(subject)
print(subjects)

'''Finding subjects using or'''
scores = {
    "Python": 35,
    "Math": 60,
    "English": 90,
    "Java": 80,
    "Science": 25
}
subjects = []
for subject, mark in scores.items():
    if mark < 40 or mark > 80:
        subjects.append(subject)
print(subjects)

'''Use not with dictionary: It reserves condition true becomes false and vice-versa.'''
scores = {
    "Python": 80,
    "Math": 30,
    "English": 65
}
for subject, mark in scores.items():
    if not mark >= 40:
        print(subject)

'''Updating marks in dictionary using loop
It changes original dictionary.It doesn't create a spearate one.'''
scores = {
    "Python": 60,
    "Math": 70,
    "English": 80
}
for subject, mark in scores.items():
    scores[subject] = mark + 5
print(scores)

'''updating only specific dictionary values'''
scores = {
    "Python": 35,
    "Math": 50,
    "English": 25
}
for subject, mark in scores.items():
    if mark < 40:
        scores[subject] = mark + 10
print(scores)

'''Finding subjects with second highest mark without sort()'''
scores = {
    "Python": 50,
    "Math": 90,
    "English": 70,
    "Java": 80
}
highest = max(scores.values())
second_highest = 0
for mark in scores.values():
    if mark < highest and mark > second_highest:
        second_highest = mark
print(second_highest)
