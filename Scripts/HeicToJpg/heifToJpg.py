"""

"""
from PIL import Image
import pillow_heif
import os

def convertHEICFolder(path):
    # Check Filepath exists
    print("\n  Searching for path", path)
    if not os.path.exists(path):
        raise ValueError("Input folder does not exist")
    
    print("\n  Folder was found: {}".format(path))

    # Extract HEIC files
    my_files = []
    for f in os.listdir(path):
        copy = f.lower()
        if copy.endswith(".heic"):
            my_files.append(f)

    print("\n  Files Found:")
    for f in my_files:
        print(f, end="  |  ")

    

    

    
    
    
    # folder = path
    # files = [f for f in os.listdir(folder) if f.endswith(".heic")]
    # # if not os.path.exists():
    #  # Read in the HEIC file
    # my_file = pillow_heif.read_heif(r"C:\Users\Ryan\Pictures\Photos\Motorbike\IMG_1130.HEIC")  

    # # Extract data from the file obj to the PIL Image obj
    # image = Image.frombytes(
    #     my_file.mode,
    #     my_file.size,
    #     my_file.data,
    #     "raw"
    # )

    # # Choose where to save the converted format to
    # image.save("./test.png", format="png")
    

if __name__ == "__main__":
    convertHEICFolder(r"C:\Users\Ryan\Pictures\Photos\Motorbike")
