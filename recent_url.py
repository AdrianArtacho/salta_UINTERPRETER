# File: recent_url.py
import gui.gui_enterstring_t as gui_enterstring

def saveurl(filepath: str = 'INTER/recent_url.txt') -> None:

    url = gui_enterstring.main("Youtube URL", "URL", "Enter URL", 
        #  font=("Arial", 16), 
         default_text='', verbose=False)    
    
    description = gui_enterstring.main("Description of the URL", "Description", "Description", 
        #  font=("Arial", 16), 
         default_text='', verbose=False)    
    """
    Saves the given URL and description to a specified file.
    
    Args:
        url (str): The URL to save.
        description (str): A description of the URL.
        filepath (str): Path to the file where data will be saved.
    """
    try:
        with open(filepath, 'w') as file:
            file.write(f"{url}\n{description}\n")
        print(f"URL and description saved to {filepath}.")
    except Exception as e:
        print(f"An error occurred while saving the URL: {e}")

def main(filepath: str = 'INTER/recent_url.txt') -> tuple[str, str]:
    """
    Reads the saved URL and description from a specified file and returns them.
    
    Args:
        filepath (str): Path to the file where data is saved.
    
    Returns:
        tuple: A tuple containing the URL and its description.
    """
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            if len(lines) < 2:
                raise ValueError("File does not contain valid data.")
            url = lines[0].strip()
            description = lines[1].strip()
            return url, description
    except FileNotFoundError:
        print(f"The file {filepath} does not exist.")
        return None, None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None, None

# Example usage:
if __name__ == "__main__":
    # Save URL and description
    saveurl("https://example.com", "An example URL")
    
    # Retrieve and print URL and description
    url, description = main()
    print(f"URL: {url}")
    print(f"Description: {description}")
