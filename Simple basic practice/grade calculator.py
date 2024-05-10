grades = [78, 56, 45, 88, 90, 23, 38, 66, 95]
A = []
B = []
C = []
D = []
E = []
F = []
total = 0
for grade in grades:
    if 100 >= grade >= 90:
        A.append(grade)
    elif 80 <= grade < 90:
        B.append(grade)
    elif 70 <= grade < 80:
        C.append(grade)
    elif 60 <= grade < 70:
        D.append(grade)
    elif 50 <= grade < 60:
        E.append(grade)
    else:
        F.append(grade)

print(f"Total grade: A ={len(A)}")
print(f"Total grade: B={len(B)}")
print(f"Total grade: C ={len(C)}")
print(f"Total grade: D ={len(D)}")
print(f"Total grade: E ={len(E)}")
print(f"Total grade: F ={len(F)}")

for grade in grades:
    total += grade
average = total / len(grades)
if average > 90:
    print("Average is : A")
elif 80 <= average < 90:
    print("Average is : B")
elif 70 <= average < 80:
    print("Average is : C")
elif 60 <= average < 70:
    print("Average is : D")
elif 50 <= average < 60:
    print("Average is : E")
else:
    print("Average is : F")

