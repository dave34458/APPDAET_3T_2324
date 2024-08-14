ulam_file = open("ulam.txt", "w")  # open a file for writing
ulam_file.write("Chicken Nuggets\n")  # write a line of text to a file
ulam_file.close()  # close the file

ulam_file_reading = open("ulam.txt")  # open the file for reading
ulam_file_contents = ulam_file_reading.read()  # read the contents, and assign to a variable
ulam_file_reading.close()  # close the file
print(ulam_file_contents)  # print the variable where the text is stored