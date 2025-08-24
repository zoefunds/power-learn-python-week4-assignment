# power-learn-python-week4-assignment
1. The program defines a process_file() function that handles the main logic.
  
2. Error Handling:
    <ul>
      <li>FileNotFoundError: Handles cases where the input file doesn't exist</li>
    <li>PermissionError: Handles cases where the program doesn't have permission to access the file</li>
    <li>IOError: Handles general input/output errors</li>
    <li>Exception: Catches any other unexpected errors</li>
    </ul>

3. File Operations:
   <ul>
    <li>Uses with statements for proper file handling (automatically closes files)</li>
    <li>Reads content from the input file</li>
    <li>Modifies the content (in this case, converts to uppercase)</li>
    <li>Creates a new filename by adding 'modified_' prefix</li>
    <li>Writes the modified content to the new file</li>
    </ul>

4. To use this program:
<ul>
  <li>Save it as file_processor.py</li>
  <li>Run it from the command line using python file_processor.py</li>
  <li>When prompted, enter the name of a file you want to process</li>
  <li>The program will create a new file with "modified_" prefix containing the uppercase version of the original content</li>
</ul>
