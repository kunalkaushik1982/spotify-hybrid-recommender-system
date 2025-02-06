import kagglehub
import os
import shutil

def download_data():
    source_dir=kagglehub.dataset_download("undefinenull/million-song-dataset-spotify-lastfm")
    return source_dir

def move1_data(source_dir,destination_dir):    
    destination_dir = destination_dir+'\\data'
    for filename in os.listdir(source_dir):
        if filename.endswith('.csv'):
            source_file = os.path.join(source_dir, filename)
            destination_file = os.path.join(destination_dir, filename)
        
            # Move the file
            shutil.move(source_file, destination_file)

def copy_data(source_dir, destination_dir):
    # Ensure the destination directory exists
    destination_dir = os.path.join(destination_dir, 'data')
    os.makedirs(destination_dir, exist_ok=True)

    # Iterate over all files in the source directory
    for filename in os.listdir(source_dir):
        if filename.endswith('.csv'):
            source_file = os.path.join(source_dir, filename)
            destination_file = os.path.join(destination_dir, filename)
            
            # Copy the file
            shutil.copy2(source_file, destination_file)
            print(f"Copied: {source_file} to {destination_file}")
        else:
            print(f"Skipped: {filename} (not a .csv file)")


if __name__ == "__main__":
    source_dir=download_data()   
    destination_dir = os.getcwd() 
    copy_data(source_dir,destination_dir)