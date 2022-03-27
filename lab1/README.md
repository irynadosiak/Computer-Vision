# Histogram left shift

### Launch:
Install the following libraries:
- numpy
- matplotlib

Run the program with the python preprocessing.py command.

### Resilt comparison:
RGB (red, green, blue) is an additive color model that describes a method of color synthesis in which red, green, and blue light are superimposed together by mixing into different colors.
The image consists of three images (one for each channel), where each image can store discrete pixels with normal brightness intensities from 0 to 255.
The higher the intensity, the brighter the image. That is why the operation of shifting the histogram to the left - the illumination of the image. Because according to the formula, we increase the pixel intensity by k units.
The results show that images with a high content of black colors are brighter. For images with high and low levels of detail, the detail remains the same. However, if you apply the offset to the left to a bright image, the filter may play a blurring role.
