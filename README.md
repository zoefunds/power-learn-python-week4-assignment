# power-learn-python-week4-assignment
1. The program defines a process_file() function that handles the main logic.
  
2. Error Handling:
    a. FileNotFoundError: Handles cases where the input file doesn't exist
    b. PermissionError: Handles cases where the program doesn't have permission to access the file
    c. IOError: Handles general input/output errors
    d. Exception: Catches any other unexpected errors

3. File Operations:
    a. Uses with statements for proper file handling (automatically closes files)
    b. Reads content from the input file
    c. Modifies the content (in this case, converts to uppercase)
    d. Creates a new filename by adding 'modified_' prefix
    e. Writes the modified content to the new file

To use this program:
1. Save it as file_processor.py
2. Run it from the command line using python file_processor.py
3. When prompted, enter the name of a file you want to process
4. The program will create a new file with "modified_" prefix containing the uppercase version of the original content

The program will handle various error scenarios:
a. If the file doesn't exist
b. If there are permission issues
c. If there are other I/O errors
d. If any unexpected errors occur
