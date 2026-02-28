import re

def gdrive_to_direct_link():
    """
    Takes user input of a Google Drive share link and outputs
    a direct download link usable in pandas or requests.
    """
    shared_link = input("Enter Google Drive share link: ").strip()
    
    # Try to extract file ID for /d/FILE_ID/ style
    match = re.search(r'/d/([a-zA-Z0-9_-]+)', shared_link)
    
    # If not found, try open?id=FILE_ID style
    if not match:
        match = re.search(r'id=([a-zA-Z0-9_-]+)', shared_link)
    
    if match:
        file_id = match.group(1)
        direct_link = f'https://drive.google.com/uc?id={file_id}'
        print("Direct Download Link:", direct_link)
        return direct_link
    else:
        print("Error: Could not extract file ID. Check the link format.")
        return None


# Example usage:
direct_link = gdrive_to_direct_link()

# If you want, you can read it into pandas directly:
if direct_link:
    import pandas as pd
    try:
        df = pd.read_csv(direct_link)
        print("\nCSV Loaded Successfully. Preview:")
        print(df.head())
    except Exception as e:
        print("Error reading CSV:", e)