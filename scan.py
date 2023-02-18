import os  # from native modules
import pytesseract  # from pytesseract
import cv2  # from Opencv
import io  # from native modules
from PIL import Image, ImageFile  # from Pillow
import platform  # from native modules

ImageFile.LOAD_TRUNCATED_IMAGES = True

# Global variables
strPDF, textScanned, textScanned, inputTeEx, dirName = "", "", "", "", [
    "images", "output_txt"]


# def gInUs():
#     # Global var
#     global strPDF
#     global inputTeEx
#     if platform.system() == "Windows":
#         # Print input
#         print("[.] Add the tesseract.exe local path")
#         inputTeEx = input()
#         # Print input
#         print("[!] Add the PDF file local path:")
#         inputUser = input()
#     # Print an alert if input is not valid, if not, call to fun reDoc
#     if(inputUser == "" or len(inputUser.split("\\")) == 1):
#         print("[X] Please enter a valid PATH to a file")

def reImg():
    # Global var
    global dirName
    global inputTeEx
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-ocr\\tesseract.exe"
    content = os.listdir('inputs')
    print("content:", content)
    for i in range(len(content)):
        # Reading each image in images
        image = cv2.imread(f'inputs/{content[i]}')
        # Scan text from image
        print(f"[.] Scan text from {content[i]}")
        text = pytesseract.image_to_string(image, lang='eng')
        # Concate text scanned in a string
        # print
        print("[!] Finished scan text")
        # Showing img input
        # cv2.imshow('Image', image)
        # # 0.5 milisecond
        cv2.waitKey(1000)
        fileTxt = open(f"outputs/{content[i]}txtResult.txt", "w")
        fileTxt.write(text)
        print("[!] File Writted")


reImg()
