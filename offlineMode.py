# views.py
from django.http import JsonResponse
from .models import LanguagePack

def download_language_pack(request, language_code):
    # Check if the requested language pack exists
    try:
        language_pack = LanguagePack.objects.get(language_code=language_code)
        # Serve the language pack file for download
        response = FileResponse(open(language_pack.file_path, 'rb'))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = f'attachment; filename="{language_pack.filename}"'
        return response
    except LanguagePack.DoesNotExist:
        return JsonResponse({'message': 'Language pack not found.'})
