"""
Python Image Manipulation Empty Template by Kylie Ying (modified from MIT 6.865)

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

from image import Image # 'image' is from another file not included in this Githyb repository
import numpy as np

def brighten(image, factor):
    # when we brighten, we just want to make each channel higher by some amount 
    # factor is a value > 0, how much you want to brighten the image by (< 1 = darken, > 1 = brighten)
    # pass

    # we need to iterate through each pixel, which carries 3-d info: x position, y position, and color (RGB channels)
    # to that, we first need to see how big the image is ...

    x_pixels, y_pixels, num_channels = image.array.shape  # note: we would be invoking self.array for the stored image
    # need to make a new image so that we don't mutate the one we're passing in
    # ??? Why would that happen in the first place? Maybe we do that just as a matter of good practice?
    new_im = Image(x_pixels=x_pixels,y_pixels=y_pixels,num_channels=num_channels)
        # to be perfectly clear--now we just mutate the new image, not the old one. 

    # here's the non-vectorized way to do this: a 3D for-loop each pixel at its x, its y, and its color:
    # for x in range(x_pixels):
    #   for y in range (y_pixels):
    #      for c in range(num_channels):
                # at index x,y,c in the image new array, we're going to "mirror" the first image, times "factor"
                # to adjust for brightness:
                new_im.array[x,y,c] = image.array[x,y,c] * factor
                # after all this, we return the new image:

    # vectorized version (in which you WON'T have to iterate through a for loop of every pixel)
    new_im.array = image.array * factor
    return new_im

def adjust_contrast(image, factor, mid=0.5): # in practice, this makes the difference from a user-define midpoint greater.
    # adjust the contrast by increasing the difference from the user-defined midpoint by factor amount
    # to put new values in without modifying the image (the reasoning is a bit confusing here)
    x_pixels, y_pixels, num_channels = image.array.shape 
    new_im = Image(x_pixels=x_pixels,y_pixels=y_pixels,num_channels=num_channels)

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_im.array[x,y,c] = (image.array[x,y,c] - mid) * factor + mid
                # basically from an arbitary midpoint, you're making points lighter or darker
                # the midpoint creates a distance and the factor just makes it bigger (maybe?)
                # don't understand why you add the midpoint back in (??)
    return new_im

    # the vectorized version would look like this:
    # new_im.array = (image.array - mid) * factor + mid

def blur(image, kernel_size):
    # kernel size is the number of pixels to take into account when applying the blur
    # (ie kernel_size = 3 would be neighbors to the left/right, top/bottom, and diagonals)
    # kernel size should always be an *odd* number
    pass

def apply_kernel(image, kernel):
    # the kernel should be a 2D array that represents the kernel we'll use!
    # for the sake of simiplicity of this implementation, let's assume that the kernel is SQUARE
    # for example the sobel x kernel (detecting horizontal edges) is as follows:
    # [1 0 -1]
    # [2 0 -2]
    # [1 0 -1]
    pass

def combine_images(image1, image2):
    # let's combine two images using the squared sum of squares: value = sqrt(value_1**2, value_2**2)
    # size of image1 and image2 MUST be the same
    pass
    
if __name__ == '__main__':
    lake = Image(filename='lake.png')
    city = Image(filename='city.png')

    # what if we want to make changes to specific parts of the image?
    # brightened_im = adjust_brightness(lake,1.7)
    # brightened_im.write_image("brightened.png")

    # or you could darken it:
    darkened_im = adjust_brightness(lake, 0.3)
    darkened_im.write_image('darkened.jpg')