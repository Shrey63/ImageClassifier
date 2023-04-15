import cv2
import time
import os
from django.http import JsonResponse


from django.http import JsonResponse
import base64

def save_image(request):
  # Get the image data from the AJAX request
  image_data = request.POST['image_data']

  # Strip the data URL prefix from the image data
  image_data = image_data.replace('data:image/jpeg;base64,', '')

  # Decode the base64-encoded image data into a binary string
  image_binary = base64.b64decode(image_data)

  # Save the image to your server
  with open('../media/pic/image.jpg', 'wb') as f:
    f.write(image_binary)

  # Return a success response
  return JsonResponse({'status': 'success'})
