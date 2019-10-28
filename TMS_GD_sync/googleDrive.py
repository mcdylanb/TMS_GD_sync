from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os


gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

#creates object getting parameter of gauth for GoogleDrive
drive = GoogleDrive(gauth)

#File Drive creates object
file_drive = drive.CreateFile()  
#file uses content from parameter to copy
file_drive.SetContentFile('test.xls') 
# File comes out as HTML codes
file_drive.Upload() #file gets upload 

