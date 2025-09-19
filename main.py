empty={}
student={'name':"Alice",'age':"12",'grade':"9",'subject':"Math",}
#access element
print(f"Name:{student['name']}")
#appemd/add elements
empty['Parent_Name']="Bob"
print(empty)
student['gender']="Female"
print(f"Gender:{student['gender']}")
student.pop('subject')
print(student)
student.clear()
print(student)