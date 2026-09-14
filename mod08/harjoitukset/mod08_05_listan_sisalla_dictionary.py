#hedelmä = {'Omena', 'Appelsiini', 'Vesimeloni'}
#Onko Omena listassa?
#print('Omena' in hedelmä)

students = [
    {'name':'Ella','age':14,'grade':'9'},
    {'name':'Leo','age':13,'grade':'8'},
    {'name':'Aino','age':11,'grade':'10'}
]

# print(type(students[0]))

print(f'{students[2]['name']}n arvosana on {students[2]['grade']}')

for student in students:
    print(f'{student['name']}{student['grade']}')