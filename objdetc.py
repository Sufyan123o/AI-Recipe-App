# Object detection alg w/ API ninjas's API
import requests

# Specify the API endpoint and your API key
api_url = "https://api.api-ninjas.com/v1/objectdetection"
api_key = "I9YnK/kN0MMzdE98UccqXw==H8uiKc4nxVz2nTA0"

# Specify the path to the image you want to analyze
image_path = "/Users/salma/Downloads/image1.jpg"

# Prepare the headers
headers = {
    "Content-Type": "multipart/form-data",
    "x-api-key": api_key,
}

# Create a form with the image file
files = {"image": (image_path, open(image_path, "rb"))}

# Send a POST request to the API
response = requests.post(api_url, headers=headers, files=files)

if response.status_code == 200:
    # Parse the response JSON
    data = response.json()

    # Check if the response contains food objects
    if "food" in data:
        food_objects = data["food"]
        if food_objects:
            print("Food objects detected:")
            for food_object in food_objects:
                print(f"Label: {food_object['label']}")
                print(f"Confidence: {food_object['confidence']}")
                print(f"Bounding Box: {food_object['bbox']}\n")
        else:
            print("No food objects detected in the image.")
    else:
        print("No food objects detected in the image.")
else:
    print("Error: Failed to process the image. Status code:", response.status_code)
    print("Response content:", response.text)
