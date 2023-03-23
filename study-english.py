import tkinter as tk
from PIL import Image, ImageTk
import googletrans
from googletrans import Translator
import os
import random

# Create a dictionary that maps image names to their English translations
image_names = {
    "1.jpg": "táo",
    "2.jpg": "chuối",
    "3.jpg": "sư tử",
    "4.jpg": "tàu lửa",
    "5.jpg": "hươu cao cổ",
    "6.jpg" : "mây",
    "7.jpg" : "ngôi nhà",
    "8.jpg" : "cây",
    "9.jpg" : "cửa",
    "10.jpg" : "gối ôm",
    "11.jpg" : "con kiến",
    "12.jpg" : "máy tính",
    "13.jpg" : "lớp học",
    "14.jpg" : "cá heo",
    "15.jpg" : "tờ lịch",
    "16.jpg" : "lạc đà",
    "17.jpg" : "con muỗi",
    "18.jpg" : "cái quạt",
    "19.jpg" : "máy giặt",
    "20.jpg" : "chim cánh cụt"
}

# Create a list of image names
images = list(image_names.keys())

# Initialize variables for the current image and its translation
current_image = ""
current_translation = ""

# Create a translator object for English to Vietnamese translation
translator = Translator()

# Create a function to load a random image and its translation
def load_image():
    global current_image, current_translation
    # Select a random image from the list
    current_image = random.choice(images)
    # Load the image using PIL
    image_path = os.path.join("images", current_image)
    image = Image.open(image_path)
    # Resize the image to fit the display box
    image = image.resize((300, 300), Image.ANTIALIAS)
    # Convert the image to a format that tkinter can display
    image_tk = ImageTk.PhotoImage(image)
    # Update the image display box with the new image
    image_box.config(image=image_tk)
    image_box.image = image_tk
    # Get the English translation of the current image
    current_translation = image_names[current_image]

# Create a function to check the user's answer
def check_answer():
    # Get the user's answer from the input box
    user_answer = answer_box.get().strip()
    # Translate the current image's name from Vietnamese to English
    translated_name = translator.translate(current_translation, src='vi', dest='en').text
    # Compare the user's answer to the translated name
    if user_answer.lower() == translated_name.lower():
        # If the answer is correct, load a new image
        answer_box.delete(0, tk.END)
        load_image()

# Create a function to start the game
def start_game():
    # Load the first image
    load_image()
    # Clear the answer box
    answer_box.delete(0, tk.END)

# Create the main window and set its title
window = tk.Tk()
window.title("Study English With Nhat")

# Set the background image
bg_image = Image.open("background.jpg")
bg_image = bg_image.resize((800, 600), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(window, image=bg_photo)
bg_label.image = bg_photo
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label for the image display box
image_label = tk.Label(window, text="Image:", font=("Arial", 14), bg="#F7DC6F")
image_label.pack()

# Create a box to display the current image
image_box = tk.Label(window, bg="#F9E79F")
image_box.pack()


# Create a label for the answer input box
answer_label = tk.Label(window, text="What is this in English?")
answer_label.pack()

# Create an input box for the user's answer
answer_box = tk.Entry(window)
answer_box.pack()

# Create a button to check the user's answer
check_button = tk.Button(window, text="Check Answer", command=check_answer)
check_button.pack()

result_label = tk.Label(window, text="Click Start to play game")
result_label.pack()

# Create a box to display the result of the user's answer
result_box = tk.Label(window)
result_box.pack()

# Create a button to start the game
start_button = tk.Button(window, text="Start Game", command=start_game)
start_button.pack()

# Start the GUI event loop
window.mainloop()
