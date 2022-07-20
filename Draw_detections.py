import cv2, os

class ImageDetails:
    def __init__(self, name="", x_center=0, y_center=0, width=0, height=0):# Initialize the class parameters
        self.name = name
        self.x_center = int(float(x_center)) 
        self.y_center = int(float(y_center))
        self.width = int(float(width))
        self.height = int(float(height))
    
# Load data from resources\Q2_Draw_task_labels.tsv line by line and save it to a list of ImageDetails objects
def load_data(file_name: str):
    list_of_objects = []
    dir_validation(file_name)
    with open(file_name) as file:
        for line in file: # Read the file line by line
            splited_line = [word.strip() for word in line.split("\t")] # Split the line by tabs
            if splited_line[0].endswith(".png"): # Check if the file is a png 
                list_of_objects.append(ImageDetails(*splited_line)) # Append the ImageDetails object to the list
    return list_of_objects



# Create a directory for the images named "Images_draw_output"
def creat_new_directory(file_name: str):
    cwd = os.getcwd() # Get the current working directory
    final_dir =  os.path.join(cwd, file_name) # Create a new name directory with "Images_draw_output"
    if not os.path.exists(final_dir): # Check if the directory exists
        os.makedirs(final_dir) # Create the directory
        print("Directory created")
    else:
        print("Directory already exists")
    return final_dir

# Draw a rectangle on the image
def draw_rectangle(image_dir: str, final_dir: str, image: ImageDetails):
    final_dir = os.path.join(final_dir, image.name)
    image_dir = os.path.join(image_dir, image.name)
    
    if os.path.exists(final_dir):
        # read the image
        img = cv2.imread(final_dir)
        # draw a rectangle around the object
        cv2.rectangle(img, (image.x_center, image.y_center), (image.x_center + image.width, image.y_center + image.height), (0, 255, 0), 2)
        # save the image
        cv2.imwrite(final_dir, img)
    else:
        # read the image
        img = cv2.imread(image_dir)
        # draw a rectangle around the object
        cv2.rectangle(img, (image.x_center, image.y_center), (image.x_center + image.width, image.y_center + image.height), (0, 255, 0), 2)
        # save the image
        cv2.imwrite(final_dir, img)
         
    print("Image saved")
    
# Check if the directory exists
def dir_validation(dir: str):
    if not os.path.exists(dir):
        print(f"{dir} does not exist\nPlease check the path and run again")
        exit(1)

def main():
    list_of_objects = load_data("Predictions.tsv") # Load the data from the file to list of ImageDetails objects
    image_dir = "Draw_task_images" # The directory of the images - can be changed
    dir_validation(image_dir)
    final_dir = creat_new_directory("Images_draw_output") # Create a directory for the images named "Images_draw_output"
    for image in list_of_objects:# For each image in the list
        draw_rectangle(image_dir, final_dir, image) # Draw a rectangle on givven coordinates

if __name__ == "__main__":
    main()


