
students_data = [
    {'id': 1, 'name': 'Alice', 'class': '5A', 'subject': 'Math'},
    {'id': 2, 'name': 'Bob', 'class': '5B', 'subject': 'Science'},
    {'id': 3, 'name': 'Alice', 'class': '5A', 'subject': 'Math'},  
    {'id': 4, 'name': 'Dave', 'class': '5C', 'subject': 'English'},
    {'id': 5, 'name': 'Eve', 'class': '5A', 'subject': 'Math'},
    {'id': 2, 'name': 'Bob', 'class': '5B', 'subject': 'Science'}, 
]

students_dict = {}
for student in students_data:
    key = (student['id'], student['name'], student['class'], student['subject'])
    students_dict[key] = student 