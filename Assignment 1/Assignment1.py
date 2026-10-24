students = [
    {"name": "Lara",  "age": 23, "track": "AI",   "hours_studied": 40, "scores": [85, 90, 78]},
    {"name": "Omar",  "age": 31, "track": "Data", "hours_studied": 12, "scores": [60, 55, 70]},
    {"name": "Rim",   "age": 27, "track": "AI",   "hours_studied": 55, "scores": [95, 88, 92]},
    {"name": "Karim", "age": 19, "track": "Web",  "hours_studied": 8,  "scores": [50, 65, 40]},
    {"name": "Nour",  "age": 25, "track": "AI",   "hours_studied": 30, "scores": [75, 80, 85]},
    {"name": "Sami",  "age": 35, "track": "Data", "hours_studied": 48, "scores": [88, 91, 79]},
]

#Part 1:
#1-
print(students[0]["name"])  # first student's name
print(students[-1]["name"])  # last student's name

#2-
for x in students:
    if x["name"] == "Rim":
        print(x["scores"])  # Rim's scores

#3-
for x in students:
    print(f"{x['name']} is {x['age']} years old and studies {x['track']}.") #loop through the list of students and print their name, age, and track

#Part 2:
#4-
ai_students = []  # create an empty list to store AI students
for student in students:
    if student["track"] == "AI":
        ai_students.append(student)  # create a new list of students who are in the AI track
print(f"AI Students: {len(ai_students)}")  # print the new list of AI students

#5-
ai_students_1 = [x for x in students if x["track"] == "AI"]  # create a new list of students who are in the AI track using list comprehension
print(f"AI Students: {len(ai_students_1)}")  # print the new list of AI students
print(ai_students == ai_students_1)

#6-
hardworking_students = [x["name"] for x in students if x["hours_studied"] > 30]  # create a new list of students who have studied more than 30 hours using list comprehension
print(hardworking_students)  # print the new list of hardworking students

#7-
filtered_students=[x for x in students if x["age"]>24 and x["track"]=="AI"]
print(filtered_students)

#Part 3
#8-
total_age= 0
for x in students:
    total_age += x["age"]
average_age= total_age/ len(students)
print(f"Average age: {average_age}")

#9-
total_hours = 0
for x in students:
    total_hours += x["hours_studied"]
print(f"Total Hours Studied : {total_hours}")

#10- 
top_student = students[0]

for x in students:
    if x["hours_studied"] > top_student["hours_studied"]:
        top_student = x

print(f"Most hours studied: {top_student['name']} ({top_student['hours_studied']} hours)")

#11-
for x in students:
    avg_score = sum(x["scores"]) / len(x["scores"])
    print(f"{x['name']}: {round(avg_score, 1)}")

#Part 4-
#12-
transformed_students = [
    {
        "name": x["name"],
        "average_score": round(sum(x["scores"]) / len(x["scores"]), 1)
    }
    for x in students
]
print(transformed_students)

#13-
track_counts = {}
for x in students:
    track = x["track"]
    if track in track_counts:
        track_counts[track] += 1
    else:
        track_counts[track] = 1

print(track_counts)

#14-
unique_tracks = {x["track"] for x in students}

print(unique_tracks)

# Why set? 
# A set automatically removes duplicates and ensures every track appears only once.

#Part 5
#15-
def filter_by_track(students_list, track_name):
    return [x for x in students_list if x["track"] == track_name]

print("AI Track:", filter_by_track(students, "AI"))
print("Data Track:", filter_by_track(students, "Data"))

#16-
def average_score(x):
    return sum(x["scores"]) / len(x["scores"])
print(round(average_score(students[0]),1))

#17-
def top_student(students_list):
    best_student = students_list[0]
    for x in students_list:
        if average_score(x) > average_score(best_student):
            best_student = x
    return best_student["name"]

print("Top Student:", top_student(students))

#18-
def summary(students_list):
    tot_students = len(students_list)
    avg_age = sum(x["age"] for x in students_list) / tot_students
    uniq_tracks = {x["track"] for x in students_list}
    
    return {
        "total_students": tot_students,
        "average_age": round(avg_age, 1),
        "tracks": uniq_tracks
    }

print("Summary:", summary(students))

#Bonus
#19-
def report(students, min_hours):
    result = [
        {
            "name": student["name"],
            "average_score": round(average_score(student), 1)
        }
        for student in students
        if student["hours_studied"] >= min_hours
    ]

    result.sort(key=lambda student: student["average_score"], reverse=True)

    return result
print(report(students, 30))