#QwikLabs exxercise question
# Code to apply operations on all the images 
# present in a folder one by one 
# operations such as rotating, resizing, 
from PIL import Image 
from PIL import ImageFilter 
import os 


def main(): 

       
        # path of the folder containing the raw images 
        inPath ="images"

        # path of the folder that will contain the modified image 
        outPath ="/opt/icons"

        for imagePath in os.listdir(inPath): 
                # imagePath contains name of the image 
                inputPath = os.path.join(inPath, imagePath) 

                # inputPath contains the full directory name 
                img = Image.open(inputPath) 

                fullOutPath = os.path.join(outPath, imagePath) 
                # fullOutPath contains the path of the output 
                # image that needs to be generated 
                img.rotate(90).resize((128, 128), Image.ANTIALIAS).convert('RGB').save(fullOutPath, format = "jpeg") 
                
# Driver Function 
if __name__ == '__main__': 
        main() 
