print("*********Matric Results Summary*********")

print("*********Please Enter your Details Below*********")

name=input("Enter Your Full Name")
print("Enter your Date of Birth")
yearob=int(input("Enter your birth year (for ex: 1997):"))
monthob=input("Enter your Month of Birth(for ex: jan-dec)")
dob=input("Enter your Dob:(for ex: 1-31)")
print("*********Enter your Each Subjects marks details below*********")

M=int(input("Enter your Maths marks (out of 100):"))
U=int(input("Enter your Urdu marks (out of 100):"))
E=int(input("Enter your Eng marks (out of 100):"))
C=int(input("Enter your computer marks (out of 100):"))
p=int(input("Enter your Physics marks (out of 100):"))
age=2025-yearob
obtained=M+U+C+E+p
per=(obtained/500)*100

if per>=80:
    Grade="A+"
elif per>=70:
    Grade="A"
elif per>=60:
    Grade="B"
elif per>=50:
    Grade="C"
else:
    Grade="Fail"
    
    
print("Dear",name,"Age",age,"Your Matric examination for Result are here in which obtained marks are",obtained,"and the percentage is ",per,"And Grade is ",Grade)



#Decisions in Python
#if-else

''' # Arithmetic Operator
+ 
-
/
*
%
** | POW(base,value)
//
'''
'''
Relational / Comparison Operators

== #ye isi ke barabar hai
> #bara hai
< #chota hai
>= #bara hai or barabar hai
<= #chota hai or barabar hai
!= #barabar nh hai


Logical operator

and
or
not
'''




























