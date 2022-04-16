import cv2 as cv
import numpy as np

from matplotlib import pyplot as plt


def draw_matches(matches, key1, key2, image1, image2):
    output = cv.drawMatches(img1=image1,
                            keypoints1=key1,
                            img2=image2,
                            keypoints2=key2,
                            matches1to2=matches[:15],
                            outImg=None,
                            flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    plt.figure(figsize=(20, 20))
    plt.imshow(output)
    plt.show()


def brisk_descriptor(img1, img2):
    # Convert the training image to gray scale
    image1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    image2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    # Create a Surf Matcher object
    brisk = cv.xfeatures2d.SURF_create()
    key1, desc1 = brisk.detectAndCompute(image1, None)
    key2, desc2 = brisk.detectAndCompute(image2, None)
    print('Number of key_points detected on distorted image:', len(key2), "\n")
    return key1, desc1, key2, desc2


def brute_force_matcher(desc1, desc2):
    # Create a Brute Force Matcher object
    BFMatcher = cv.BFMatcher(normType=cv.NORM_L1, crossCheck=True)
    # Perform the matching between the Surf descriptors of the training image and the test image
    matches = BFMatcher.match(queryDescriptors=desc1, trainDescriptors=desc2)
    # The matches with shorter distance are the ones we want
    matches = sorted(matches, key=lambda x: x.distance)
    return matches


def own_matcher(desc1, desc2):
    matches = []
    for i, k1 in enumerate(desc1):
        for j, k2 in enumerate(desc2):
            matches.append(cv.DMatch(_distance=np.linalg.norm(k1 - k2), _imgIdx=0, _queryIdx=i, _trainIdx=j))
    matches = sorted(matches, key=lambda x: x.distance)
    return matches


images = [{"train": 'images/train.png', "test": 'images/test.png'},
          {"train": 'images/train1.png', "test": 'images/test1.png'}]
for img in images:
    original_image = cv.cvtColor(cv.imread(img["train"]), cv.COLOR_BGR2RGB)
    distorted_image = cv.cvtColor(cv.imread(img["test"]), cv.COLOR_BGR2RGB)
    key1, desc1, key2, desc2 = brisk_descriptor(original_image, distorted_image)
    matches1 = brute_force_matcher(desc1, desc2)
    draw_matches(matches1, key1, key2, original_image, distorted_image)
    matches2 = own_matcher(desc1, desc2)
    draw_matches(matches2, key1, key2, original_image, distorted_image)
