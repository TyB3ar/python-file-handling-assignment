'''  
Objective: The goal of this assignment is to deepen your understanding of the OS module in Python.

Task 1: Directory Inspector:

Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the user for the directory path and then display the contents.

Code Example:
    import os

    def list_directory_contents(path):
        # List and print all files and subdirectories in the given path
Expected Outcome: The script should correctly list all files and subdirectories in the specified directory. Handle exceptions for invalid paths or inaccessible directories.
'''


import os

try: 
    
    def list_directory_contents(path):
        print("Main Directory: ") 
        entry_lst = os.listdir(path)  
        
        for i in os.scandir(path):
            if i.is_dir():
                sub_lst = os.listdir(i) 
                for entry in sub_lst:
                    print(f"   Sub Directory Files: ")
                    print("    " + entry)    
            elif i.is_file():
                file_lst = [i]
                for entry in file_lst:
                    print(f"File Name: {entry}")
                    
    while True:
        print("Please enter the directory path you wish to view, else enter 'exit'. ")
        user_dir = input("Directory Path: ") 
        if os.path.exists(user_dir):
           list_directory_contents(user_dir) 
           break
        elif user_dir.lower() == 'exit':
            break
        else: 
            print("Error, pathway not found.") 
            
except PermissionError:
    print("Error, permission not granted.") 
except FileNotFoundError:
    print("Error, file not found.")
except Exception as e:
    print(f"Error: {e}")
        