import json

from django.core.files.storage import default_storage
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST


@require_POST
def upload_images(request):
    images = request.FILES.getlist('images')
    saved_files = []

    for image in images:
        filename = default_storage.save(f'uploads/{image.name}', image)
        saved_files.append(filename)

    return JsonResponse({'status': 'success', 'files': saved_files})


def home(request):
    if request.method == 'POST' and request.headers.get('Content-Type') == 'application/json':
        data = json.loads(request.body)
        message = data.get('message')
        send_mail(
            subject='Msg from PicturePets',
            message=message,
            from_email=None,  # Uses DEFAULT_FROM_EMAIL
            recipient_list=['emailjakefrench@googlemail.com'],  # Replace with your actual email
            fail_silently=False
        )
        return JsonResponse({'status': 'success'})
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')