import webbrowser
import os

# Define the path to your local HTML file
# file_path = '/path/to/your/file.html'
def main(file_path):
    # Check if the file exists
    if os.path.exists(file_path):
        # Convert the file path to a URL format
        file_url = 'file://' + os.path.abspath(file_path)
        
        # Print the link (optional)
        print(f"Open this link in your browser: {file_url}")
        
        # Open the file in the default web browser
        webbrowser.open(file_url)
    else:
        print("File does not exist.")


if __name__ == "__main__":
    file_path = 'youtube_video_with_padding_intervals.html'
    main(file_path)