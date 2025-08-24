def process_file():
    try:
        # Ask user for input filename
        input_filename = input("Enter the name of the file to read: ")
        
        # Try to open and read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            
            # Modify the content (in this example, we'll capitalize it)
            modified_content = content.upper()
            
            # Create output filename by adding 'modified_' prefix
            output_filename = f"modified_{input_filename}"
            
            # Write modified content to new file
            with open(output_filename, 'w') as output_file:
                output_file.write(modified_content)
                
            print(f"\nSuccess! Modified content has been written to {output_filename}")
            
    except FileNotFoundError:
        print(f"\nError: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"\nError: Permission denied to access the file '{input_filename}'.")
    except IOError as e:
        print(f"\nError: An I/O error occurred: {str(e)}")
    except Exception as e:
        print(f"\nError: An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    print("File Processing Program")
    print("----------------------")
    process_file()