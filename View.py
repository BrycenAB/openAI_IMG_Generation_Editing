import tkinter as tk

import Controller

root = tk.Tk()
root.title("Image Viewer")
root.config(bg="Black")
root.geometry("500x300")

label2 = tk.Label(root, width=75, bg="black", fg="green", text="Enter a prompt:")
label2.pack()
input_field = tk.Entry(root, width=75, font=("Arial", 8), justify="center", bg="black", fg="green", border=1, )
input_field.pack()
show_button = tk.Button(root, text="Generate Image", bg="black", fg="green", activebackground="green",
                        activeforeground="black", command=lambda: Controller.show_image())
show_button.pack()


input_field2 = tk.Entry(root, width=75, font=("Arial", 8), justify="center", bg="black", fg="green")
input_field2.pack()
edit_button = tk.Button(root, text="Edit Image", bg="black", fg="green", border=1,activebackground="green",
                        activeforeground="black",
                        command=lambda: Controller.generate_mask("IMGs/image.png", int(threshold_entry.get())))
edit_button.pack()
threshold_entry = tk.Entry(root, width=25, font=("Arial", 8), justify="center",
                           bg="black", fg="green")
threshold_entry.insert(0, "150")
threshold_entry.pack()
label = tk.Label(text="Threshold for greyscale conversion (0-255)", bg="black", fg="green")
label.pack()

reset_button = tk.Button(root, text="Reset", bg="black", fg="green", activebackground="green", activeforeground="black",
                         command=lambda: Controller.reset())
reset_button.pack()
