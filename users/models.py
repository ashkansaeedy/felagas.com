from django.db import models
from django.contrib.auth.models import User

# class upload(models.Model):
	
# class Document(models.Model):
#     description = models.CharField(max_length=255, blank=True)
#     document = models.FileField(upload_to='documents/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='defaults.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'