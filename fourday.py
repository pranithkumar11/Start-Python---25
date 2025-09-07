# list and tuples
student = [89,77,100000,23,56,9000,7000000]
student = [str(x)for x in student]


student.sort(reverse=True)
student.sort()
print(student)
print(type(student))
print(len(student))
print(student[1])
student.append(45)
print(student)
student.pop(1)
print(student)
student.insert(1,67)
print(student)
