from PIL import Image 
import webcolors as wb
from random import shuffle
import os
from time import sleep 


def createImgRandomColor(width, height,number,folderName="Result"):
    # getting current working directory
    current_directory = os.getcwd()
    path = os.path.join(current_directory, folderName)

    # creating a new folder for storing the results
    try : 
        os.mkdir(path)
    except:
        pass

    # creating list of colour names    
    col = wb.css3_hex_to_names.values()
    color_name = []
    for name in col:
        color_name.append(name)

    # shuffle the color names
    shuffle(color_name)
    print("\n\n---Generating {} image(s) with dimensions {}px x {}px---\n\n".format(number,width,height))

    #sleep(3)

    for i in range(number):
        im=Image.new("RGB",(width,height),color_name[i])
        im.save("{}//Img{:03d}.jpg".format(folderName,i+1))
        print("\tImage {:03} Done!".format(i+1))
    sleep(2)

    print("""\n\nImages will be available at "{}"\n
---------Task-Completed---------\n\n""".format(path))

#driver code

if __name__ == "__main__":
    print("\n\n-----Image Generator w/ Random Solid Colours-----\n\n")
    sleep(2)
    w=int(input("Enter the Width of the image (in pixels) : "))
    h=int(input("Enter the Height of the image (in pixels) : "))
    n=int(input("\nHow many Images do you want? : "))
    answer = input("""\nDo you want to Rename the output folder?\n(By Default it'll be "Result") \n\n(Y/N) : """)
    while True:
        if answer.upper() == "Y":
            fname=input("\nEnter the Folder name: ")
            createImgRandomColor(w, h, n, fname)
            break
        elif answer.upper() == "N":
            createImgRandomColor(w, h, n)
            break
        else:
            answer=input("\n\nInvalid Choice!\nRe-enter a valid Choice (Y/N) :")

        
    
