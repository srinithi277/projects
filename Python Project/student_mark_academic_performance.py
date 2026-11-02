name=input("enter your name : ")
n=int(input("enter no of subject : "))
total=0
for i in range(1,n+1):
    mark=float(input(f'enter mark for subject {i} : '))
    total+=mark
percentage= total/n
if percentage >=90:
    grade="A+"
    performance="out standing"
elif percentage >=80:
    grade="A"
    performance="excellent"
elif percentage >=70:
    grade="A"
    performance="very good"
elif percentage >=60:
    grade="C"
    performance="good"
elif percentage >=50:
    grade="D"
    performance="average"
else:
    grade="F"
    performance="need improvement"
print("\n----academic performance----")
print("student name : ",name)
print("total mark : ",total)
print("percentage : ",round(percentage,2),"%")
print("grade : ",grade)
print("performance : ",performance)