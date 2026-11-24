# 1. DATA STORAGE

students = []              # main list = students

# 2. FUNCTION DEFINITIONS 
def add_student():
    """Logic to input data and append to the list."""
    name = input("\nEnter the name of student: ")
    
    try:    
        roll = int(input("Enter the roll number: "))
        marks = float(input("Enter the marks: "))
        if (marks > 100) or (marks < 0):
            print("\nError: Marks should be 0-100")
            return
        
        student = {"name": name, "roll": roll, "marks": marks}

        for n in students:
            if roll == n['roll']:
                print("this roll number already exists ")
                return
            
        students.append(student)
        print(f"Success: {name} added successfully")

    except ValueError:
        print("\nInvalid input. Please enter valid numbers for roll or marks.")

def view_all():
    """Logic to loop through the list and print records with design."""

    if not students:
        print("\n" + "="*30)
        print("      DATABASE EMPTY")
        print("="*30)
        return
    
    print("\n" + "="*30)
    print("      STUDENT RECORDS")
    print("="*30)

    for s in students:
        print(f"Name: {s['name']:<10} | Roll: {s['roll']:<4} | Marks: {s['marks']}")

    print("="*30)

def find_topper():
    """Logic to find the highest scorer."""

    if not students:
        print("\nNo students to evaluate.")
        return
    
    toppers = []
    max_marks = -1

    for s in students:
        if s['marks'] > max_marks:
            max_marks = s['marks']
            toppers = [s]
        elif s['marks'] == max_marks:
            toppers.append(s)
    
    print("\n" + "="*30)
    print("      TOPPER DETAILS")
    print("="*30)

    for topper in toppers:
        print(f"👑 {topper['name']} (Roll: {topper['roll']})")
        print(f"Score: {topper['marks']}/100")

    print("="*30)

def avg():
    """Logic to calculate average with design."""

    if not students:
        print("\nNo students to calculate.")
        return
    
    total_marks = 0
    
    for s in students:
        total_marks += s['marks']
        
    count = len(students)
    average = total_marks / count

    print("\n" + "="*30)
    print("      CLASS PERFORMANCE")
    print("="*30)
    print(f"Total students: {count}")
    print(f"Total marks   : {total_marks}")
    print(f"Overall average: {average:.2f}%")
    print("="*30)

# 3. MAIN EXECUTION BLOCK
def main():
    while True:
        print("\n--- SYSTEM MENU ---")
        print("1. Add student\n2. View students\n3. Find topper\n4. Calculate average\n5. Exit")
        
        choice = input("\nSelect Option: ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            view_all()
        elif choice == '3':
            find_topper()
        elif choice == '4':
            avg()
        elif choice == '5':
            print("\nGOODBYE!\n")
            break
        else:
            print("\nInvalid Choice")

# 4. ENTRY POINT
if __name__ == "__main__":
    main()