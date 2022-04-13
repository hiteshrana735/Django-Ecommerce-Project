import json
students = {
    "Akash" : {
        "name" : "Akash",
        "age" : 23,
        "present_today" : True,
        "subjects" : ["Hindi", "English", "Maths"]
    },

    "Ritik" : {
        "name" : "Ritik",
        "age" : 22,
        "present_today" : False,
        "subjects" : ["Hindi","English", "Maths"]
    },

    "Himanshu" : {
        "name" : "Himanshu",
        "age" : 24,
        "present_today" : True,
        "subjects" : ["Hindi", "English", "Chemistry"]
    }
}

# print(students["Akash"]['subjects'][0])

student_json = json.dumps(students)
print(student_json)