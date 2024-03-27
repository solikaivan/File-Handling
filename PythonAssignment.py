# File Creation
try:
    # Create a new text file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write at least three lines of text to the file
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("line 2: 45678\n")
    print("File 'my_file.txt' created successfully.")
except Exception as e:
    print("Error:", e)
finally:
    # Close the file if it's open
    file.close() if 'file' in locals() else None

# File Reading and Display
try:
    # Open "my_file.txt" in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Read and display the contents of the file
        print("Contents of 'my_file.txt':")
        for line in file:
            print(line.strip())  # Strip newline characters before printing
except Exception as e:
    print("Error:", e)

# File Appending
try:
    # Open "my_file.txt" in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the existing content
        file.write("Appending line 1\n")
        file.write("Appending line 2\n")
        file.write("Appending line 3\n")
    print("Additional lines appended to 'my_file.txt'.")
except Exception as e:
    print("Error:", e)
finally:
    # Close the file if it's open
    file.close() if 'file' in locals() else None
