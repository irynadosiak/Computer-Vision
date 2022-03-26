import os
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import image as img


def validate_input_number(input_number, lower_condition, upper_condition, message):
    while input_number > upper_condition or input_number < lower_condition:
        input_number = int(input(message))
    return input_number


class ImagePreprocessing:
    """ A class used to make image preprocessing """

    def __init__(self, image_name, k):
        self.image_name = image_name
        self.image = img.imread(f'images/{image_name}.jpg')
        self.k = k

    def _perform_left_shift(self) -> np.array:
        image = img.imread(f'images/{self.image_name}.jpg')
        for r in range(0, image.shape[0]):
            for g in range(0, image.shape[1]):
                for b in range(0, image.shape[2]):
                    image[r][g][b] = min([image[r][g][b] + self.k, 255])
        return image

    def _plot_result(self, preprocessed_image: np.array):
        original_image_label = 'Original image'
        illuminated_image_label = f"Illuminated image (k={self.k})"
        labels = [original_image_label, illuminated_image_label]
        images = [self.image, preprocessed_image]
        fig, axes = plt.subplots(ncols=len(images))
        for idx, ax in enumerate(axes):
            ax.imshow(images[idx])
            ax.set_title(labels[idx])
            ax.axis("off")
        plt.show()

    def show_illuminated_image(self):
        """ Show origin and illuminated image in a figure"""
        preprocessed_image = self._perform_left_shift()
        self._plot_result(preprocessed_image)


if __name__ == '__main__':
    existing_images = [os.path.splitext(f)[0] for f in os.listdir("images") if f.endswith('.jpg')]
    for number, image_name in enumerate(existing_images):
        print(f"{number + 1}. {image_name}")
    number = int(input("\nProvide a number of image name from the list above: "))
    incorrect_image_number_message = (f"!!! The image does not exist\n"
                                      f"Please provide a correct number of image name from the list above: ")
    validate_input_number(number, 1, len(existing_images) + 1, incorrect_image_number_message)
    image_name = existing_images[number - 1]
    k = int(input("Provide k: "))
    incorrect_k_message = ("!!! K must satisfy the condition 0 < k < 255\n"
                           "Please provide a correct number: ")
    validate_input_number(number, 0, 255, incorrect_k_message)
    image_preprocessing_obj = ImagePreprocessing(image_name, k)
    image_preprocessing_obj.show_illuminated_image()
