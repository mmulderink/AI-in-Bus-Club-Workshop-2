'''
1. Sign up here: https://huggingface.co/join
2. Confirm your email
3. Then once signed up go here: https://huggingface.co/settings/tokens
4. Create a token, the name does not matter, however, you must check the box 'Make calls to the serverless Inference API' under 'Inference'
5. Once you hit 'Create token', copy the text that begins with hf_...
6. hit the '+' icon at the top bar of the code and type 'secrets' to go to the secrets tab; Finally, name the secret 'HF' and paste that text into the secrets tab.
'''

import requests
import os
import io
from PIL import Image

input_for_output = "Stock image of a diverse students in a workshop."

# the link to the image model
# API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
headers = {"Authorization": "Bearer " + os.environ['HF']}

# send the prompt to hugging face
def query(payload):
  response = requests.post(API_URL, headers=headers, json=payload)
  return response.content
image_bytes = query({
  "inputs": input_for_output,
})

# save / open the image
image = Image.open(io.BytesIO(image_bytes))
image.save("output_image.png")