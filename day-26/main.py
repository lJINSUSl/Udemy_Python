# numbers = [1,2,3]
#
# new_list = [n+1 for n in numbers]
#
# print(new_list)
#
# name = 'Angela'
#
# new_list1 = [letter for letter in name]
# print(new_list1)
#
# my_range = range(1,5)
# new_list2 = [num*2 for num in my_range]
# print(new_list2)
#
# names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
# new_list3 = [item for item in names if len(item)<=4]
# print(new_list3)
# new_list4 = [item.upper() for item in names if len(item)>5]
# print(new_list4)
#
import random

names = ["A","B","C","D","E","F"]
students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)
print(students_scores.items())
passed_students = {student:score for (student,score) in students_scores.items() if score > 60}
print(passed_students)