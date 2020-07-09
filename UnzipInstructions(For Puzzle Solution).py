import zipfile
import os
import shutil

for files in os.listdir("C:\\Users\\blsmi\\Desktop\\𝑬𝑹'𝑻𝑯𝑵𝑮\\𝑪𝒐𝒅𝒊𝒏𝒈👨🏾‍💻\\PythonBootcamp\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise"):
  comp_file = zipfile.is_zipfile('unzip_me_for_instructions.zip')
  if comp_file:
  	comp_file = zipfile.ZipFile('unzip_me_for_instructions.zip', 'r')
  	zip_obj.extractall('extracted_content(1)')
  	
