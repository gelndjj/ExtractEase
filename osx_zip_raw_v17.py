import os, zipfile, py7zr, rarfile, threading
import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.ttk import Progressbar, Style
from PIL import Image, ImageTk
from ttkthemes import ThemedTk

def on_folder_selected(event):
    global selected_folder_paths
    selected_folder_paths = []
    for selected_item in tree.selection():
        folder_path = tree.item(selected_item, 'values')[0]
        selected_folder_paths.append(folder_path)

def update_tree():
    node = tree.focus()
    if tree.parent(node):
        populate_tree(node)

def populate_tree(parent_node):
    path = tree.set(parent_node, "fullpath")
    tree.delete(*tree.get_children(parent_node))

    try:
        # List directories, excluding hidden ones (those starting with '.')
        for p in os.listdir(path):
            if p.startswith('.'):
                continue  # Skip hidden files and folders
            p_path = os.path.join(path, p)
            if os.path.isdir(p_path):
                node = tree.insert(parent_node, "end", text=p, values=[p_path])
                # Insert a dummy node if there are subdirectories
                if any(not subp.startswith('.') and os.path.isdir(os.path.join(p_path, subp)) for subp in os.listdir(p_path)):
                    tree.insert(node, "end")
    except PermissionError:
        pass  # Skip directories where permission is denied

def extract_files_in_folder(folder_path):
    if not folder_path:
        print("No folder selected for extraction")
        return [], []

    extension_folder_name = "Extracted_Files_" + specific_extension.get() if specific_extension.get() else "Extracted_Files"
    extract_folder = os.path.join(folder_path, extension_folder_name)
    os.makedirs(extract_folder, exist_ok=True)

    all_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    zip_7z_rar_files = [f for f in all_files if f.endswith(('.zip', '.7z', '.rar'))]
    total_files = len(zip_7z_rar_files)

    if total_files == 0:
        print("No zip, 7z, or rar files found in the selected folder.")
        return [], []

    good_files = []
    bad_files = []

    for file_name in zip_7z_rar_files:
        file_path = os.path.join(folder_path, file_name)
        try:
            if file_name.endswith('.zip'):
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_folder)
                good_files.append(file_path)
            elif file_name.endswith('.7z'):
                with py7zr.SevenZipFile(file_path, 'r') as archive:
                    archive.extractall(path=extract_folder)
                good_files.append(file_path)
            elif file_name.endswith('.rar'):
                with rarfile.RarFile(file_path, 'r') as archive:
                    archive.extractall(path=extract_folder)
                good_files.append(file_path)
        except Exception as e:
            print(f"Error extracting '{file_name}': {str(e)}")
            bad_files.append(file_path)

    return good_files, bad_files

def extract_zip_files():
    extraction_thread = threading.Thread(target=process_extraction)
    extraction_thread.start()

def extract_zip_files_browse():
    destination = filedialog.askdirectory(title="Select Destination Folder")
    if not destination:
        print("No destination folder selected")
        return
    extraction_thread = threading.Thread(target=lambda: process_extraction_browse(destination))
    extraction_thread.start()

def process_extraction_browse(destination):
    all_good_files = []
    all_bad_files = []

    total_folders = len(selected_folder_paths)
    for i, folder_path in enumerate(selected_folder_paths):
        good_files, bad_files = extract_files_in_folder_browse(folder_path, destination)
        all_good_files.extend(good_files)
        all_bad_files.extend(bad_files)

        # Update the progress bar based on the number of folders processed
        progress_percent = ((i + 1) / total_folders) * 100
        window.after(0, update_progress_bar, progress_percent)

    # Once all folders are processed, display the results
    window.after(0, display_error_window, all_good_files, all_bad_files)

def extract_files_in_folder_browse(folder_path, destination):
    if not folder_path:
        print("No folder selected for extraction")
        return [], []

    # Create a folder inside the destination to store extracted files
    extract_folder = os.path.join(destination, "Extracted_Files")
    os.makedirs(extract_folder, exist_ok=True)

    good_files = []
    bad_files = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(('.zip', '.7z', '.rar')):
            file_path = os.path.join(folder_path, file_name)
            try:
                # Process each supported file type
                if file_name.endswith('.zip'):
                    with zipfile.ZipFile(file_path, 'r') as zip_ref:
                        zip_ref.extractall(extract_folder)
                elif file_name.endswith('.7z'):
                    with py7zr.SevenZipFile(file_path, 'r') as archive:
                        archive.extractall(path=extract_folder)
                elif file_name.endswith('.rar'):
                    with rarfile.RarFile(file_path, 'r') as archive:
                        archive.extractall(path=extract_folder)
                good_files.append(file_path)
            except Exception as e:
                print(f"Error extracting '{file_name}': {str(e)}")
                bad_files.append(file_path)

    return good_files, bad_files

def update_progress_bar(progress_percent):
    progress_var.set(progress_percent)

def process_extraction():
    all_good_files = []
    all_bad_files = []

    total_folders = len(selected_folder_paths)
    for i, folder_path in enumerate(selected_folder_paths):
        good_files, bad_files = extract_files_in_folder(folder_path)
        all_good_files.extend(good_files)
        all_bad_files.extend(bad_files)

        # Update the progress bar based on the number of folders processed
        progress_percent = ((i + 1) / total_folders) * 100
        window.after(0, update_progress_bar, progress_percent)

    window.after(0, display_error_window, all_good_files, all_bad_files)

def extract_specific_extension_files():
    for folder_path in selected_folder_paths:
        process_specific_extension_files(folder_path)

def extract_specific_extension_files_browse():
    destination = filedialog.askdirectory(title="Select Destination Folder")
    if not destination:
        print("No destination folder selected")
        return
    for folder_path in selected_folder_paths:
        process_specific_extension_files_browse(folder_path, destination)

def process_specific_extension_files_browse(folder_path, destination):
    if not folder_path:
        print("No folder selected for extraction")
        return

    extensions = specific_extension.get().split()
    if not extensions:
        print("No specific extensions entered")
        return

    # Create a folder inside the destination to store extracted files
    extract_folder = os.path.join(destination, "Extracted_Files")
    os.makedirs(extract_folder, exist_ok=True)

    specific_extension_files = []

    # Extract files with the specific extensions from each zip file in the folder
    zip_files = [f for f in os.listdir(folder_path) if f.endswith('.zip') and os.path.isfile(os.path.join(folder_path, f))]
    for file_name in zip_files:
        file_path = os.path.join(folder_path, file_name)
        try:
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                for file_info in zip_ref.infolist():
                    if not file_info.is_dir() and any(file_info.filename.lower().endswith('.' + ext.lower()) for ext in extensions):
                        file_info.filename = os.path.basename(file_info.filename)
                        zip_ref.extract(file_info, extract_folder)
                        specific_extension_files.append(file_info.filename)
        except zipfile.BadZipFile:
            print(f"Error extracting '{file_name}'")

def process_specific_extension_files(folder_path):
    if not folder_path:
        print("No folder selected for extraction")
        return

    extensions = specific_extension.get().split()
    if not extensions:
        print("No specific extensions entered")
        return

    extract_folder = os.path.join(folder_path, "Extracted_Files")
    os.makedirs(extract_folder, exist_ok=True)

    specific_extension_files = []

    # Extract files with the specific extensions from each zip file in the folder
    zip_files = [f for f in os.listdir(folder_path) if f.endswith('.zip') and os.path.isfile(os.path.join(folder_path, f))]
    for file_name in zip_files:
        file_path = os.path.join(folder_path, file_name)
        try:
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                for file_info in zip_ref.infolist():
                    if not file_info.is_dir() and any(file_info.filename.lower().endswith('.' + ext.lower()) for ext in extensions):
                        file_info.filename = os.path.basename(file_info.filename)
                        zip_ref.extract(file_info, extract_folder)
                        specific_extension_files.append(file_info.filename)
        except zipfile.BadZipFile:
            print(f"Error extracting '{file_name}'")

def display_error_window(good_files, bad_files):
    error_window = ThemedTk(theme="arc")
    error_window.title("Bad Zip Files")
    error_window.geometry("600x300")

    listbox = tk.Listbox(error_window)
    listbox.pack(fill=tk.BOTH, expand=True)

    # Add count of good zip files
    count_good_zip_files = len(good_files)
    count_good_zip_files_label = f"Count of Good Zip Files: {count_good_zip_files}"
    listbox.insert(tk.END, count_good_zip_files_label)

    # Add paths of good zip files
    for file_path in good_files:
        listbox.insert(tk.END, file_path)

    listbox.insert(tk.END, "")

    # Add count of bad zip files
    count_bad_zip_files = len(bad_files)
    count_bad_zip_files_label = f"Count of Bad Zip Files: {count_bad_zip_files}"
    listbox.insert(tk.END, count_bad_zip_files_label)

    # Add paths of bad zip files
    for file_path in bad_files:
        listbox.insert(tk.END, file_path)

    # Add a scrollbar to the Listbox
    scrollbar = tk.Scrollbar(error_window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    error_window.mainloop()

def display_specific_extension_files_window(extension_files, zip_count):
    # Create a new window
    extension_window = ThemedTk(theme="arc")
    extension_window.title("Extracted Files with Specific Extension")

    # Set the window size
    extension_window.geometry("600x300")

    # Create a Listbox widget to display the extracted files with the specific extension
    listbox = tk.Listbox(extension_window)
    listbox.pack(fill=tk.BOTH, expand=True)

    # Add count of extracted files with the specific extension as the first line
    count_extension_files = len(extension_files)
    count_extension_files_label = f"Count of Extracted Files: {count_extension_files}"
    listbox.insert(tk.END, count_extension_files_label)

    # Calculate count of bad zip files
    count_bad_zip_files = zip_count - count_extension_files
    count_bad_zip_files_label = f"Count of Bad Zip Files: {count_bad_zip_files}"
    listbox.insert(tk.END, count_bad_zip_files_label)
    listbox.insert(tk.END, "")  # Insert a blank line

    # Add paths of extracted files with the specific extension
    for extension_file in extension_files:
        listbox.insert(tk.END, extension_file)

    # Add a scrollbar to the Listbox
    scrollbar = tk.Scrollbar(extension_window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    # Run the extension files window's main loop
    extension_window.mainloop()

# Tkinter window setup
window = ThemedTk(theme="arc")
window.geometry("650x350")
window.resizable(0, 0)
window.title("ZIP File Extractor")

# Configure the grid
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)  # Configure the row for the tree to expand

# File explorer panel setup
explorer_frame = tk.Frame(window)
explorer_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")  # rowspan=2 makes the tree span the entire height

tree = ttk.Treeview(explorer_frame, columns=["fullpath"], displaycolumns=[])
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

tree.bind("<<TreeviewOpen>>", lambda event: update_tree())
tree.bind("<<TreeviewSelect>>", on_folder_selected)

# Set the initial root node to the Users directory for macOS
root_node = tree.insert("", "end", text="Users", values=["/Users"])
populate_tree(root_node)

# Create a progress bar variable and widget
progress_var = tk.DoubleVar()
style = Style()
style.theme_use("default")  # Use a modern theme for the progress bar

# Reduce the thickness of the progress bar
style.configure("TProgressbar", thickness=15, thicknessunit=0.1)

# Set the icon for the window
icon_path = "path_to_icon/icon.png"
window.iconphoto(True, ImageTk.PhotoImage(file="zip_icon.png"))

# Create a frame to hold other widgets (progress bar and buttons) on the right side
right_frame = tk.Frame(window)
right_frame.grid(row=0, column=1, sticky="nsew")
right_frame.columnconfigure(0, weight=1)
right_frame.columnconfigure(1, weight=1)  # New column for the image

# Add progress bar to the grid (occupying only half the width)
progress_bar = Progressbar(right_frame, variable=progress_var, style="TProgressbar", length=270)
progress_bar.grid(row=16, column=0, sticky="w", padx=10, pady=10)

# Place widgets in the first column of right_frame
specific_extension_label = tk.Label(right_frame, text="Enter Specific Extension")
specific_extension_label.grid(row=0, column=0, sticky="w", padx=5)
specific_extension = tk.StringVar()
specific_extension_entry = tk.Entry(right_frame, textvariable=specific_extension, width=5)
specific_extension_entry.grid(row=1, column=0, sticky="w", padx=5)
specific_extension_button = tk.Button(right_frame, text="Extract Specific Extension (Same Folder)", command=extract_specific_extension_files)
specific_extension_button.grid(row=2, column=0, sticky="w", pady=10)
specific_extension_button_browse = tk.Button(right_frame, text="Extract Specific Extension (Specific Folder)", command=extract_specific_extension_files_browse)
specific_extension_button_browse.grid(row=3, column=0, sticky="w", pady=2)
extract_button = tk.Button(right_frame, text="RAW Extraction (Same Folder)", command=extract_zip_files)
extract_button.grid(row=4, column=0, sticky="w", pady=10)
extract_button_browse = tk.Button(right_frame, text="RAW Extraction (Specific Folder)", command=extract_zip_files_browse)
extract_button_browse.grid(row=5, column=0, sticky="w")

# Load the background picture and place it in the second column of right_frame
background_image_path = "zip_icon.png"
background_image = Image.open(background_image_path)
background_image = background_image.resize((64, 64), Image.Resampling.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)
canvas = tk.Canvas(right_frame, width=background_image.width, height=background_image.height)
canvas.grid(row=8, column=0, rowspan=2, sticky="nsew", padx=11, pady=10)
canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)

window.mainloop()
