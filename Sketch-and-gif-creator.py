import cv2
import tkinter as tk
from tkinter import filedialog
import os
import glob
from PIL import Image

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
filepath, filename = os.path.split(file_path)
new_file_name = filepath + '/' + os.path.splitext(filename)[0] + '_sketch.jpg'

img = cv2.imread(file_path)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted_gray_image = 255 - gray_image
blurred_img = cv2.GaussianBlur(inverted_gray_image, (21,21),0)
inverted_blurred_img = 255 - blurred_img
pencil_sketch_IMG = cv2.divide(gray_image, inverted_blurred_img, scale = 256.0)
cv2.imwrite(new_file_name, pencil_sketch_IMG)


fp_in = filepath + '/' + os.path.splitext(filename)[0] + '*.jpg'
fp_out = filepath + '/' + os.path.splitext(filename)[0] + '.gif'

img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=1000, loop=0)

os.remove(new_file_name)
