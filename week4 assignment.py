# Create a dummy file for the program to read
with open('sample.txt', 'w') as file:
    file.write("Hello, this is the first line.\n")
    file.write("The second line has more text.\n")
    file.write("And the third line concludes the file.")

# The main program logic without a function
input_filename = 'sample.txt'
output_filename = 'modified_sample.txt'

try:
    # Read the content of the input file
    with open(input_filename, 'r') as infile:
        content = infile.read()

    # Modify the content (e.g., convert to uppercase)
    modified_content = content.upper()

    # Write the modified content to the output file
    with open(output_filename, 'w') as outfile:
        outfile.write(modified_content)

    print(f"Successfully modified '{input_filename}' and saved to '{output_filename}'.")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' was not found.")
except IOError as e:
    print(f"An I/O error occurred: {e}")