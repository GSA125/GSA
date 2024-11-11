import json

def load_data(filename):
    students = {}
    with open (filename, "r") as file:
        reader = json.load(file)
        for student_id, student_info in reader.items():
            student = student_info[0]
            name = student['name']
            grade = student['grade']
            group = student['group']
            students[student_id] = [name, grade, group]
            
    return students
            
def main():
    filename='accdients.csv'
    yes = load_data(filename)
    
    print ()
    print ("Student display list")
    print ()
    
    for item in yes:
        print(f"Number ID:{item}")
        print(f"Name: {yes[item][0]}")
        print(f"Grade: {yes[item][1]}")
        print(f"Group: {yes[item][2]}")
        print()
    
    
main()
    