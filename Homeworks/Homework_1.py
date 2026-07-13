#task1

var1 = type(1)
var2 = type(-1)
var3 = type(True)

print(var1, var2, var3)

#task2

var4 = float(False)
var5 = float(3)
var6 = list({"key": "value", "key1": "value", "key3": "value"})

print(var4, var5, var6)

#task3

group = {
    "name": "Python2023",
    "count": 35,
    "male": 22,
    "female": 13,
    "students": ["Student1", "Student2", "Student3", "Student4", "Student5"],
    "ages": [24, 33, 15, 45, 42]
}

print(group)

#task4

birth_year = int(input("Enter your birth year: "))
name = input("Enter your name: ")
surname = input("Enter your surname: ")
current_year = 2026

age = current_year - birth_year

print(f"მე {name} {surname} დავიბადე {birth_year} წელს, შესაბამისად ვარ {age} წლის")

#task5

Yes = 119
No = 82

percent_of_yes = round((Yes / (Yes + No)) * 100, 2)
percent_of_no = round((No / (Yes + No)) * 100, 2)

print(f"YES: {Yes} = {percent_of_yes}%")
print(f"NO: {No} = {percent_of_no}%")


#task6

seconds = 3670

hours = seconds // 3600
seconds_left = seconds % 3600
minutes = seconds_left // 60
seconds_final = seconds_left % 60

print(f"{hours} საათი {minutes} წუთი {seconds_final} წამი")

#task7

text = "Python"

print(text[0], text[-1])

#task8

math = 45
total = 60

percent_of_math_exam = round((math / total) * 100)

print(f"{percent_of_math_exam}%")

#task9

birth_year = 2000
current_year = 2025

print(f"მომავალ წელს შენ იქნები {current_year - birth_year + 1} წლის")

#task10

minutes = 350
hours = 350 // 60
minutes_left = 350 % 60

print(f"{hours} საათი და {minutes_left} წუთი")