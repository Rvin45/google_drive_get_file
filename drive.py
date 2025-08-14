import requests
import pandas as pd
# Replace with your file's ID (the long string in the share link)
file_id = "1cQ8I_3T0LrTGkiFQyt7_didIU3cUtt0K"
url = f"https://drive.google.com/uc?export=download&id={file_id}"

# Where you want to save the file
destination = "downloaded_file.csv"

# Download file
response = requests.get(url)
if response.status_code == 200:
    with open(destination, "wb") as f:
        f.write(response.content)
    print(f"File downloaded as {destination}")
else:
    print("Error downloading file:", response.status_code)
