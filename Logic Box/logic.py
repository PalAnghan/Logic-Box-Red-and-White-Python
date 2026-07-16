# Welcome Message Print 
print("Welcome to the Pattern and Number Analyzer!")

while True:
    print("\nSelect an Option :")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    
    choice_num = int(input("Enter Your Choice: "))
        
    match choice_num:
        case 1:
            n = int(input("Enter the number of rows for the pattern: "))
            for i in range(1, n + 1):
                for j in range(i):
                    print("*", end=" ")
                print()
                
        case 2:
            start_num = int(input("Enter the start of range: "))
            end_num = int(input("Enter the end of range: "))
            total_sum = 0
            
            for i in range(start_num, end_num + 1):
                if i % 2 == 0:
                    print(f"Number {i} is Even")
                else:
                    print(f"Number {i} is Odd")
                total_sum += i
            print(f"Sum of all numbers from {start_num} to {end_num} is: {total_sum}")
            
        case 3:
            print("Exiting the program. Goodbye!")
            break
            
        case _:
            print("Invalid choice. Please select 1, 2, or 3.")
