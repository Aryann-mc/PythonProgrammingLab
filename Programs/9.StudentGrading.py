#Student grading system using combination of lists and dictionaries
student_mark=[]
student_name=input("Enter student name: ")
student_id=int(input("Enter student ID: "))
No_of_subs=5
for i in range(No_of_subs):
    subject_mark=int(input("Enter subject mark of subject"+str(i+1)+": " ))
    student_mark.append(subject_mark)
totallen=len(student_mark)
totalmarks=sum(student_mark)
average=totalmarks/No_of_subs
if(average<50):
    grade="F"
elif(average>=50 and average<=60):
    grade="B"
elif(average>=70 and average<=80):
    grade="A"
elif(average>80):
    grade="Excellent"
else:
    grade="Not enough marks"
#data displayed as dictionary
student_data= {}
student_data["name"]=student_name
student_data["student_id"]=student_id
student_data["subject_marks"]=student_mark
student_data["Avg"]=average
student_data["grade"]=grade

#The output as a dictionary
print("The data is:")
print(student_data)


