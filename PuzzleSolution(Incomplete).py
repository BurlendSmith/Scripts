# You should now see 5 folders, each with a lot of random .txt files.
# Find number: ###-###-#### 
# Iterate through each file, open it, and search for a telephone number.

# Open a diractory
# Check if items in directory are folders
# If they are, open them and iterate through each txt file to search for a number
# if number found print, 'I found a number: (number)'

import os
import re


path = "C:\\Users\\blsmi\\Desktop\\𝑬𝑹'𝑻𝑯𝑵𝑮\\𝑪𝒐𝒅𝒊𝒏𝒈👨🏾‍💻\\PythonBootcamp\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise\\extracted_content"

for folder , sub_folders , files in os.walk(path):
    
    print("Currently looking at folder: "+ folder)
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold )
    
    print('\n')
    
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+f)
        for o in open():
        	for match in re.search(r'\d{3}-\d{3}-\d{4}',f):
        		print(match.group())

    print('\n')
    



