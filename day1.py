name = "emon"
age = 25
gpa = 12.22
print("My name is {} and I am {} years old.".format(name, age))


print("My name is {0} and I am {1} years old.".format(name, age))



print (f"typee:{type(age)}")
print (f"typee:{type(name)}")
print (f"typee:{type(gpa)}")


name,age,gpa ="dhwie", 12, 12.22
print("My name is {0} and I am {1} years old.".format(name, age))


#swapping

x,y = 1,2
print("before swapping ",x,y)
x,y=y,x
print("after swapping ",x,y)

#list
student_info =["emon", 33, 88.0 ]
name, age, score =student_info
print("unpacked:", name, age, score)

name1, *others = student_info
print("name:",name1)
print("name:",others)


#list operations

student_name= ["anamika","emon","cmon","lmon"]
student_score=[12,13,14]


print(student_name)
print(student_score)

print('first student', student_name[0]) # form start
print('last student', student_name[-1]) #from last
print(' student', student_name[0:3]) # form 0 the index to 3 
print('every second student', student_name[::2]) #  "skip","skip","cmon","lmon


#add to end
student_name.append('demon')
print("\n after adding demon", student_name)


#add to end
student_name.insert[1,"mmon"]  #insert in index 1
print("\n after adding demon", student_name)

#add to end
student_name.remove["demon"]  #removes last element
print("\n after adding demon", student_name)


#list comprehension 
#multiple command 

# passing_scores = [scores   (if scvore>80)]






