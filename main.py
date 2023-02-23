import requests
import json
from key import key
import webbrowser

# Define the API endpoint URL
url = "https://api.openai.com/v1/images/generations"

# Set your OpenAI API key
api_key = key

# Define the request headers, including the API key
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Define the prompt and image URL for the generation
prompt = input("Please enter the images you to generate\n")
# image_url = "https://example.com/cat_in_the_window.jpg"

# Define the request data
data = {
    "model": "image-alpha-001",
    "prompt": prompt,
    "num_images": 1,
    "size": "1280x720",
    "response_format": "url"
}

# Send the HTTP POST request to the API endpoint
response = requests.post(url, headers=headers, data=json.dumps(data))

# Get the generated image URL from the response
if response.status_code == 200:
    response_data = json.loads(response.content)
    generated_image_url = response_data['data'][0]['url']
    print("Generated image URL:", generated_image_url)

    # opening url in web-browser
    webbrowser.open(generated_image_url)
else:
    print("Failed to generate image. Status code:", response.status_code)
