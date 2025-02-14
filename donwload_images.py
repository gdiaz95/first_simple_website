import requests

# URL of the image
url = "https://content.codecademy.com/courses/freelance-1/unit-2/finnish.jpeg"

# Send a GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Open a file in binary write mode and save the content
    with open("finnish.jpeg", "wb") as file:
        file.write(response.content)
    print("Image downloaded successfully!")
else:
    print("Failed to retrieve the image.")