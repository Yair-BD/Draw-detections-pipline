## Draw-detections-pipline

# File format:

* **Columns**
     - Name
     - X_center
     - Y_center
     - Width
     - Height
    
Every line contains the image name and the coordinates of a detected object’s bounding box.
 
 # The Pipeline action:

1. Loads the detection file.
2. Draw the objects for every image.
3. Save the output in folder 'Images_draw_output'.
