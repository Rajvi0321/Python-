# Finding type of a file.

# Taking file name as an input from user
File_name = input("Enter the File name : ")

# checking for file type using if-else ladder
if ".py" in File_name:
    print("Python File.")
elif ".txt" in File_name:
    print("Text File.")
elif ".pdf" in File_name:
    print("PDF File.")
elif ".docx" in File_name:
    print("Document File.")
elif ".ppt" in File_name:
    print("PPT File.")
else:
    print("Unknown File Type.")