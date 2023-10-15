import os
import shutil
from threading import Thread as th


print("P R G R A M M I N G   B Y  T A R E Q  K H .......")
print("-------------------------------------------------\n\n")
cwd = os.getcwd()  

files = os.listdir(cwd)

def organizePython():
	for file in files:
		if file != "org.py":
			if file.endswith(".py"):
				if "python" not in files :
					os.mkdir("python")
				pathFile = cwd + "\\" + file
				pathFileNew = cwd + "\\" + "python" +"\\" + file
				shutil.copy2(pathFile,pathFileNew)
				os.remove(pathFile)
	print("Python have been transferred successfully !!")

def organizeImage():
	for file in files:
		if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".ico") or file.endswith(".gif") :
			if "Image" not in files :
				os.mkdir("Image")
			pathFileImg = cwd + "\\" + file
			pathFileImgNew = cwd + "\\" + "Image" +"\\" + file
			shutil.copy2(pathFileImg,pathFileImgNew)
			os.remove(pathFileImg)
	print("Images have been transferred successfully !!")

def organizeDoc():
	for file in files :
		if file.endswith("docx") or file.endswith("xlsx") or file.endswith(".pptx") or file.endswith("doc") or file.endswith("txt") or file.endswith(".pdf") : 
			if "Document" not in files :
				os.mkdir("Document")
			pathFileDoc = cwd + "\\" + file
			pathFileDocNew = cwd + "\\" + "Document" + "\\" + file
			shutil.copy2(pathFileDoc,pathFileDocNew)
			os.remove(pathFileDoc)
	print("Documents have been transferred successfully !!")

def organizeVideo():
	for file in files :
		if file.endswith(".MP4") or file.endswith(".MOV") or file.endswith(".WMV") or file.endswith(".AVI") or file.endswith(".FLV"):
			if "Videos" not in files :
				os.mkdir("Videos")
			pathFileVideo = cwd + "\\" + file
			pathFileVideoNew = cwd + "\\" + "Videos" + "\\" + file
			shutil.copy2(pathFileVideo,pathFileVideoNew)
			os.remove(pathFileVideo)
	print("Videos have been transferred successfully !!")

def organizeProgram():
	for file in files:
		if file != "organize.exe":
			if file.endswith(".exe"):
				if "Program" not in files:
					os.mkdir("Program")
			pathFileProgram = cwd + "\\" + file
			pathFileProgramNew = cwd + "\\" + "Program" + "\\" + file
			shutil.copy2(pathFileProgram,pathFileProgramNew)
			os.remove(pathFileProgram)


threadPython = th(target=organizePython)
threadImage = th(target=organizeImage)
threadDocument = th(target=organizeDoc)
threadViedo = th(target=organizeVideo)
threadProgram = th(target=organizeProgram)
threadViedo.start()
threadProgram.start()
threadDocument.start()
threadImage.start()
threadPython.start()

input()
