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
student_score=[85, 92, 91,70]


print(student_name)
print(student_score)

print('first student', student_name[0]) # form start
print('last student', student_name[-1]) #from last
print(' student', student_name[0:3]) # form 0 the index to 3 
print('every second student', student_name[::2]) #  "skip","skip","cmon","lmon


#add to end
student_name.append('demon')
print("\n after adding demon", student_name)


#add to position
student_name.insert(1,"mmon") #insert in index 1
print("\n after adding demon", student_name)

#add to remove
student_name.remove("demon")  #removes last element
print("\n after adding demon", student_name)



#  List comprehension (1 line)
passing = [score for score in student_score if score > 80]

print(passing)  # [85, 92, 91]


#Tuples are similar to list but cannot be changed after creation

student_record =("meeka ", 20, 85, "cs")
print("student Record tuples", student_record)


#accesing tuples element

print ("name: ", student_record[0])
print ("Age: ", student_record[1])

#tuples unpacking
name,age ,score, department = student_record
print("\n Unpacked:", name , "is", age ,"years old, scored", "in", department)


#sets 
#set are the unordered collection of unique  items 
#sets automatically removes duplication

course_A= {"HILO", "PILO", "MEELIO", 'CHEELO'}
course_B={'billo',"khillo", "nillo","killo"}

print ("course a ", course_A)
print("course b: " ,course_B)


#set operations
# 1. Union all elements from both sets
print("\nUnion:", course_A | course_B)

# 2. Intersection common elements only
print("Intersection:", course_A & course_B)

# 3. Difference in A but not in B
print("Difference A-B:", course_A - course_B)

# 4. Symmetric Difference in either but not both
print("Symmetric Difference:", course_A ^ course_B)

# 5. Check if element exists
print("HILO in course_A:", "HILO" in course_A)


#remove duplicates from list using set
score_with_duplicates =[85,58,85,90,90,70]
unique_scores = list(set(score_with_duplicates)) #typecasting 
print("\nOriginal scores: ",score_with_duplicates )
print("unique scores: ", unique_scores)






