import sqlite3
from PIL import Image, ImageTk
import os
import tkinter as tk

from show import record1
#from record import record1

# Function to display image details
def show_image_details(item_id):
    # Retrieve the selected item from the database
    cursor.execute('SELECT name, path FROM your_table WHERE id = ?', (item_id,))
    name, image_path = cursor.fetchone()

    # Create a new window to display the image details
    details_window = tk.Toplevel()
    
    details_window.title('Records')

    # Load and display the image
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(details_window, image=photo)
    image_label.image = photo
    image_label.pack()

    # Display the image name
    name_label = tk.Label(details_window, text=f"Image Name: {name}")
    name_label.pack()
# Function to update the table based on search query
def search_images():
    query = search_entry.get()
    # # Delete the database file if it exists
    # if os.path.exists('criminal_database.db'):
    #     os.remove('criminal_database.db')
    conn = sqlite3.connect('criminal_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, path FROM your_table WHERE name LIKE ?', ('%'+query+'%',))
    rows = cursor.fetchall()

    # Clear the table
    for widget in table_frame.winfo_children():
        widget.destroy()

    # Keep track of the current row index
    row_index = 0

    # Display the search results
    for row in rows:
        item_id, name, image_path = row

     
        # Display the image name
        name_label = tk.Label(table_frame, text=name,font=("Castellar", 25,"bold"),bg="white", fg="red")
        name_label.grid(row=row_index, column=0, padx=30, pady=25)

        # Load and display the image
        image_path = os.path.join(folder, f"{name}.png")
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
       
        image_label = tk.Label(table_frame, image=photo)
        image_label.image = photo
        image_label.grid(row=row_index, column=1, padx=80, pady=25)

        # # Show image details when the "More Details" button is clicked
        # more_details_button = tk.Button(table_frame, text='More Details',  font= ("times new roman",20, "bold"),bg="white", fg="blue",
        #                                 command=lambda name=name: record1(name))
        # more_details_button.grid(row=row_index, column=2, padx=80, pady=25)
       # Show image details when the "More Details" button is clicked
        more_details_image = Image.open("C:\\hackathon\\Machine Learning\\Face Recgnition\\Resources\\more.png")
        more_details_image_resized = more_details_image.resize((250, 80))
        more_details_photo = ImageTk.PhotoImage(more_details_image_resized)
    
        more_details_button = tk.Button(table_frame, image=more_details_photo, bd=0,
                                    command=lambda name=name: record1(name))
        more_details_button.photo = more_details_photo
        more_details_button.grid(row=row_index, column=2)

        # Increment the row index
        row_index += 1

# Create the main GUI window
root = tk.Tk()
root.title('Database')
root.geometry("1450x620")
# root.configure(bg="#2edaff")
root.configure(bg="white")
tk.Label(root, text=" Record", font=("times new roman", 30,"bold"),bg="white", fg="#050A80").pack()
#         #    font = (18, 'Castellar'))


# Create a frame for the search functionality
search_frame = tk.Frame(root)
search_frame.pack(pady=10)

# Create a search entry and button
search_entry = tk.Entry(search_frame, width=50,font= ("Castellar",12, "bold"),bg="white", fg="black")
search_entry.pack(side='left', padx=5)
search_button = tk.Button(search_frame, text='Search', font= ("Castellar",14, "bold"),bg="white", fg="black", command=search_images)
search_button.pack(side='left')


# Create a frame to hold the table
frame = tk.Frame(root)
frame.pack(fill='both', expand=True)
frame.configure(bg="white")
# Create a canvas for scrolling
canvas = tk.Canvas(frame)
canvas.pack(side='left', fill='both', expand=True)
canvas.configure(bg="white")
# Create a scrollbar
scrollbar = tk.Scrollbar(frame, orient='vertical', command=canvas.yview)
scrollbar.pack(side='right', fill='y')

# Configure the canvas
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

# Create a frame inside the canvas to hold the table
table_frame = tk.Frame(canvas)
table_frame.configure(bg="white")
canvas.create_window((0, 0), window=table_frame, anchor='nw')
if os.path.exists('criminal_database.db'):
        os.remove('criminal_database.db')
# Create a database connection
conn = sqlite3.connect('criminal_database.db')
cursor = conn.cursor()

# Create the table if it does not exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS your_table (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        path TEXT
    )
''')

# Define the folder containing the images
folder = './Images'

# Keep track of the current row index
row_index = 0
N_label = tk.Label(table_frame, text="Name",font=("Castellar", 25,"bold"), fg="#050A80",bg="white")
N_label.grid(row=row_index, column=0, padx=25, pady=25)
I_label = tk.Label(table_frame, text="Photo",font=("Castellar", 25,"bold"), fg="#050A80",bg="white")
I_label.grid(row=row_index, column=1, padx=30, pady=25)
M_label = tk.Label(table_frame, text="Check More Information",font=("Castellar", 25,"bold"), fg="#050A80",bg="white")
M_label.grid(row=row_index, column=2, padx=30, pady=25)
row_index += 1



# Iterate over the image files in the folder
for filename in os.listdir(folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Process image files
        image_path = os.path.join(folder, filename)
        image = Image.open(image_path)

        # Get the image name without the file format
        name = os.path.splitext(filename)[0]

        # # Insert image details into the database
        cursor.execute('INSERT INTO your_table (name) VALUES (?)', (name,))

        # Display the image name
        name_label = tk.Label(table_frame, text=name,font=("Castellar", 20,"bold"),bg="white", fg="#050A80")
        name_label.grid(row=row_index, column=0, padx=30, pady=25)

        # Display the image
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(table_frame, image=photo)
        image_label.image = photo
        image_label.grid(row=row_index, column=1, padx=80, pady=25)

        # button = tk.Button(frame, text='More Details', font= ("times new roman",20, "bold"),bg="white", fg="blue",
        #                    command=lambda item_id=cursor.lastrowid: show_image_details(item_id))
       
        # more_details_button = tk.Button(table_frame, text='More Details',  font= ("times new roman",20, "bold"),bg="white", fg="blue",
        #                                 command=lambda name=name: record1(name))
       
        # more_details_button.grid(row=row_index, column=2, padx=80, pady=25)
        more_details_image = Image.open("C:\\hackathon\\Machine Learning\\Face Recgnition\\Resources\\more.png")
        more_details_image_resized = more_details_image.resize((250, 80))
        more_details_photo = ImageTk.PhotoImage(more_details_image_resized)
    
        more_details_button = tk.Button(table_frame, image=more_details_photo, bd=0,
                                    command=lambda name=name: record1(name))
        more_details_button.photo = more_details_photo
        more_details_button.grid(row=row_index, column=2)

        # Increment the row index
        row_index += 1
       

        # # Show image details when clicked
        # image_label.bind('<Button-1>', lambda event, item_id=cursor.lastrowid: show_image_details(item_id))
        

        # Increment the row index
        row_index += 1
       
# Commit the changes and close the connection
conn.commit()
conn.close()

# Add the table frame to the canvas
table_frame.update_idletasks()  # Update the table frame
canvas.config(scrollregion=canvas.bbox('all'))

# Configure scrolling
canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrollbar.set)
# Load the logo image and resize it
logo_image = Image.open("C:\\hackathon\\Machine Learning\\Face Recgnition\\Resources\\rec.png")
logo_image_resized = logo_image.resize((100, 100))  # Resize the image to 100x100 pixels
logo_photo = ImageTk.PhotoImage(logo_image_resized)

# Create the logo and place it at the top left corner
logo_label = tk.Label(root, image=logo_photo, bd=0)
logo_label.photo = logo_photo
logo_label.place(x=40,y=10)
def on_exit():
    root.destroy()

# Load the exit button image and resize it
exit_image = Image.open("C:\\hackathon\\Machine Learning\\Face Recgnition\\Resources\\back.png")
exit_image_resized = exit_image.resize((80, 80))  # Resize the image to 30x30 pixels
exit_photo = ImageTk.PhotoImage(exit_image_resized)

# Create the exit button and place it at the top right corner
exit_button = tk.Button(root, image=exit_photo, bd=0, command=on_exit)
exit_button.photo = exit_photo
exit_button.place(x=root.winfo_width() - 150, y=10)


# Start the main event loop
root.mainloop()

