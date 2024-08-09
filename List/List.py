students = [
    {"name": "Victor", "house": "Nairobi", "patronous": "Otter"},
    {"name": "Ragnar", "house": "Norway", "patronous": "Stag"},
    {"name": "Rollo", "house": "Norway", "patronous": "Jack Russell"},
    {"name": "Jon", "house": "Winterfell", "patronous": None}
]
for student in students:
    print(student["name"], student["house"], student["patronous"], sep=", ")