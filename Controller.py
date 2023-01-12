import numpy as np
from PIL import Image
import openai, requests, webbrowser, os

import View

openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # API key goes here


def create_basic_img(user_input):
    response = openai.Image.create(
        prompt=f"{user_input}",
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']

    # launch a new browser window
    webbrowser.open_new_tab(image_url)
    return str(image_url)


def show_image():
    url = create_basic_img(str(View.input_field.get()))
    save_image(url, "image")


def save_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
            im = Image.open(filename)
            im.save("IMGs/"+filename + ".png")
        formatted_img = Image.open("IMGs/" + filename + '.png')
        formatted_img.save("IMGs/formatted_img.png")
    else:
        print(f"Failed to retrieve image from {url}")


def generate_mask(image_path, threshold):
    image = Image.open(image_path)
    image = image.convert("L")  # convert to grayscale
    mask = np.array(image)
    mask[mask < threshold] = 0
    mask[mask >= threshold] = 255
    # save mask as png
    mask = Image.fromarray(mask)
    mask.save("IMGs/mask.png")
    edit_img()


def edit_img():
    response = openai.Image.create_edit(
        image=open("IMGs/image.png", "rb"),
        mask=open("IMGs/mask.png", "rb"),
        prompt=f"{View.input_field.get()},{View.input_field2.get()}",
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    webbrowser.open_new_tab(image_url)


def reset():
    View.input_field.delete(0, 'end')
    View.input_field2.delete(0, 'end')
    View.threshold_entry.delete(0, 'end')
    View.threshold_entry.insert(0, "150")
    if os.path.exists("IMGs/image.png"):
        os.remove("IMGs/image.png")
    if os.path.exists("IMGs/mask.png"):
        os.remove("IMGs/mask.png")
    if os.path.exists("IMGs/formatted_img.png"):
        os.remove("IMGs/formatted_img.png")
    if os.path.exists("IMGs/image"):
        os.remove("IMGs/image")
