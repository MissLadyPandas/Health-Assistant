# Final Project - Katharine Brumback - Health Assistant
# This program is a health assistant that includes a BMI calculator and a text editor.
# The BMI calculator allows the user to enter their height and weight and calculates their BMI.
# It also keeps track of the user's average weight.
# The text editor allows the user to open and save text files.
# The user can switch between the two programs using the menu bar.

#/////////////////////////////////////////////////////////////////////////////////////////////////////

#Import libraries
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os
from PIL import Image, ImageTk

#Create BMI calculator frame
def create_bmi_calculator_frame(parent, root):

    #Set the image paths
    bmi_icon_path = "logos/health.png"  

    #List to store weights for calculating average weight
    weights = []

    #Create ImageTk.PhotoImage objects using the images
    bmi_image = Image.open(bmi_icon_path)
    bmi_image_resized = bmi_image.resize((int(bmi_image.width * 0.03), int(bmi_image.height * 0.03)), Image.ANTIALIAS)
    root.bmi_icon = ImageTk.PhotoImage(bmi_image_resized)

    #Function to calculate BMI
    def calculate_bmi():
        try:

            #Get user input for height and weight
            feet = int(height_feet_entry.get())
            inches = int(height_inches_entry.get())
            weight_pounds = float(weight_entry.get())

            # Add validation checks for negative values
            if feet < 0 or inches < 0 or weight_pounds < 0:
                messagebox.showerror("Invalid input", "Height and weight must be positive values.")
                return

            # Add validation checks for minimum height and weight
            if feet < 1:
                messagebox.showerror("Invalid input", "Height is too low.")
                return
            if weight_pounds <= 1:  
                messagebox.showerror("Invalid input", "Weight is too low.")
                return

            #Convert feet and inches to meters and pounds to kilograms
            height_meters = (feet * 0.3048) + (inches * 0.0254)
            weight_kg = weight_pounds * 0.453592

            #Calculate BMI and display it in the frame
            bmi = weight_kg / (height_meters ** 2)
            bmi_result_var.set(f"BMI: {bmi:.2f}")

            #Determine and set BMI classification in label
            if bmi < 18.5:
                classification = "Underweight"
            elif 18.5 <= bmi < 25:
                classification = "Normal"
            elif 25 <= bmi < 30:
                classification = "Overweight"
            else:
                classification = "Obese"
            bmi_classification_var.set(f"Classification: {classification}")

            #Update average weight list and display average weight
            weights.append(weight_pounds)
            average_weight = sum(weights) / len(weights)
            average_weight_var.set(f"Average Weight: {average_weight:.2f} lbs")

        #Show error message if user enters invalid input
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers for height and weight.")

    #Create ImageTk.PhotoImage objects using the images
    bmi_image = Image.open(bmi_icon_path)
    bmi_icon = ImageTk.PhotoImage(bmi_image)

    #Resize the bmi image
    bmi_image_resized = bmi_image.resize((int(bmi_image.width * 0.03), int(bmi_image.height * 0.03)), Image.ANTIALIAS)
    bmi_icon = ImageTk.PhotoImage(bmi_image_resized)

    #Create the BMI calculator frame. 
    frame = ttk.Frame(parent)

    #Create a label for height in feet and an entry widget to accept user input for height in feet
    ttk.Label(frame, text="Height (ft):").grid(row=0, column=0, sticky="w")
    height_feet_entry = ttk.Entry(frame)
    #Add the frame to the parent frame
    frame.pack(padx=10, pady=10)
    height_feet_entry.grid(row=0, column=1)

    #Create a label for height in inches and an entry widget to accept user input for height in inches
    ttk.Label(frame, text="Height (in):").grid(row=1, column=0, sticky="w")
    height_inches_entry = ttk.Entry(frame)
    height_inches_entry.grid(row=1, column=1)

    #Create the "Calculate BMI" button and bind the calculate_bmi function to be executed when the button is clicked
    ttk.Label(frame, text="Weight (lbs):").grid(row=2, column=0, sticky="w")
    weight_entry = ttk.Entry(frame)
    weight_entry.grid(row=2, column=1)

    #Create the "Calculate BMI" button and call the calculate_bmi function when it is clicked.
    ttk.Button(frame, text="Calculate BMI", command=calculate_bmi).grid(row=3, column=0, columnspan=2)

    #Create labels to display the calculated BMI result and corresponding classification
    bmi_result_var = tk.StringVar()
    bmi_classification_var = tk.StringVar()
    ttk.Label(frame, textvariable=bmi_result_var).grid(row=4, column=0, columnspan=2)
    ttk.Label(frame, textvariable=bmi_classification_var).grid(row=5, column=0, columnspan=2)

    #Create label to display average weight
    average_weight_var = tk.StringVar()
    ttk.Label(frame, textvariable=average_weight_var).grid(row=6, column=0, columnspan=2)

    #Create a frame to hold the BMI calculator widget menu bar
    frame.pack(padx=10, pady=10)

#Create text editor frame
def create_text_editor_frame(parent, root):

    #Set the image paths
    text_editor_icon_path = "logos/pages.png"

    #Create ImageTk.PhotoImage objects using the images
    text_editor_image = Image.open(text_editor_icon_path)
    text_editor_image_resized = text_editor_image.resize((int(text_editor_image.width * 0.03), int(text_editor_image.height * 0.03)), Image.ANTIALIAS)
    root.text_editor_icon = ImageTk.PhotoImage(text_editor_image_resized)

    #Function to create a new file
    def new_file():
        text.delete(1.0, tk.END)
        root.title("Untitled - Text Editor")

    #Function to open an existing file
    def open_file():
        file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            root.title(os.path.basename(file) + " - Text Editor")
            text.delete(1.0, tk.END)
            with open(file, "r") as file_handler:
                text.insert(tk.INSERT, file_handler.read())

    #Function to save the current file
    def save_file():
        file = filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                                            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            with open(file, "w") as file_handler:
                file_handler.write(text.get(1.0, tk.END))
            root.title(os.path.basename(file) + " - Text Editor")

    #Create ImageTk.PhotoImage objects using the images
    text_editor_image = Image.open(text_editor_icon_path)
    text_editor_icon = ImageTk.PhotoImage(text_editor_image)
    
    #Create a frqame to hold the text editor widget menu bar
    frame = ttk.Frame(parent)

    #Create a menu bar for the text editor
    menubar = tk.Menu(root)

    #Configure the main application window to display the menu bar
    root.config(menu=menubar)

    #Create a file menu within the menu bar
    file_menu = tk.Menu(menubar, tearoff=0)

    #Add the "File" menu to the menu bar and configure it to display the "New", "Open", "Save", and "Exit" menu items
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=new_file)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    #Create a text editor widget within the text editor frame
    text = tk.Text(frame, wrap=tk.WORD)

    #Pack the text widget to expand and fill the available space
    text.pack(expand=True, fill=tk.BOTH)

    #Pack the text editor frame to expand and fill the available space
    frame.pack(expand=True, fill=tk.BOTH)


#Main function to create and display the main application window
def main():

    #Create the main application window
    root = tk.Tk()

    #Set the title and size of the main window
    root.title("BMI Calculator & Text Editor")

    #Create a Notebook widget to hold both the BMI calculator and text editor frames
    notebook = ttk.Notebook(root)

    #Create the frames for the BMI calculator and add it to the notebook
    bmi_calculator_frame = ttk.Frame(notebook)
    create_bmi_calculator_frame(bmi_calculator_frame, root)
    notebook.add(bmi_calculator_frame, text="BMI Calculator", image=root.bmi_icon, compound=tk.LEFT)

    #Create the frames for the text editor and add it to the notebook
    text_editor_frame = ttk.Frame(notebook)
    create_text_editor_frame(text_editor_frame, root)
    notebook.add(text_editor_frame, text="Text Editor", image=root.text_editor_icon, compound=tk.LEFT)

    #Pack the notebook widget to expand and fill the main window
    notebook.pack(expand=True, fill=tk.BOTH)

    #Start the main event loop to handle user inputs
    root.mainloop()

    #Call the main function when the script is executed
if __name__ == "__main__":
    main()
