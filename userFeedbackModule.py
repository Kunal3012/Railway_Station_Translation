# models.py
from django.db import models

class UserFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    feedback_category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

# views.py
from django.http import JsonResponse
from .models import UserFeedback

def submit_feedback(request):
    if request.method == 'POST':
        user = request.user
        feedback_text = request.POST.get('feedback_text', '')
        feedback_category = request.POST.get('feedback_category', '')

        # Save the feedback to the database
        UserFeedback.objects.create(
            user=user,
            feedback_text=feedback_text,
            feedback_category=feedback_category
        )

        return JsonResponse({'message': 'Feedback submitted successfully.'})

    return JsonResponse({'message': 'Invalid request method.'})

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    # Other app URLs...
]
