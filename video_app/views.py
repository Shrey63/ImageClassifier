from django.shortcuts import render

from django.shortcuts import render, redirect
from video_app.models import CapturedImage
from datetime import datetime, timedelta
import cv2
import os
from django.conf import settings
from django.http import JsonResponse

def capture_image(request):
    # Open the camera
    cap = cv2.VideoCapture(0)
    # Wait for 10 seconds
    for i in range(10):
        _, frame = cap.read()
        # Discard the first few frames
    # Capture a frame and save it
    _, frame = cap.read()
    file_name = 'captured_image.jpg'
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    cv2.imwrite(file_path, frame)
    # Release the camera
    cap.release()
    # Send a response to the client
    response = {'message': 'Image captured successfully.'}
    return JsonResponse(response)



def video_player(request):
    # logic to get the video from youtube playlist
    # ...

    # context to render in template
    context = {}

    if request.method == 'POST':
        # capture the image and save it to the database
        user = request.user
        image = request.POST.get('image_data')
        captured_image = CapturedImage.objects.create(
            user=user,
            image=image
        )
        captured_image.save()
        context['captured_image'] = captured_image

    return render(request, 'video_player.html', context)

