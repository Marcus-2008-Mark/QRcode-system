import os
import shutil

path = "C:\\Users\\PC\\Desktop\\TestFolder"

file_categories = { 
    'Images': [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3"],
    "Archives": [".zip", ".rar"],
    "Apps": [".exe", ".dmg"],
    "program": ['.py', '.html', '.css']
}


def organize_files(path):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        # Skip directories to avoid moving category folders into themselves
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        actual_ext = os.path.splitext(file_path)[1].lower()
        file_moved = False
        
        # Check categories
        for category, extensions in file_categories.items():
            if actual_ext in extensions:
                category_folder = os.path.join(path, category)
            
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)

                destination = os.path.join(category_folder, filename)
                shutil.move(file_path, destination)
                print(f"Moved {filename} to {category}")
                
                file_moved = True
                break  # Stop checking other categories for this file
                
        # Move to 'others' if no category matched
        if not file_moved:
            other_folder = os.path.join(path, "others")
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
                
            destination = os.path.join(other_folder, filename)
            shutil.move(file_path, destination)
            print(f"Moved {filename} to others")
    print("✅file Organized successfully! 📁")
if __name__ == "__main__":
    organize_files(path)