tup = (1,2,3,4,5,6)
print( type(tup))
print(tup[2:4])
print ()
print(tup[1])
tup1 =(1,)
print(type(tup1))
print(tup1)

list1 = [" Dupuguntla  pranith kumar"]
copy_list1 = list1.copy()
copy_list1.reverse()
if (copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")

marks = [10,0000,900000,890000]
print(marks.count(10000))
print(marks.count(900000))
print(marks.count(890000))


list = ["a","b","c","d","e"]
list.sort(reverse=True)
print(list)

info = {
    "name": "ace engineering collge",
    "age": 35,
    "is_adult": True,
    "marks": 94.6
}
print(info)
print("name")