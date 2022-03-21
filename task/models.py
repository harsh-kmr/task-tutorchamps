from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

# created a sample model
class post(models.Model):
    attach_file = models.FileField(upload_to='files/',)
    description = models.TextField( null = True, blank= True)
    author = models.ForeignKey(
      User,
      on_delete=models.CASCADE, null=True
    )
    submission = models.DateTimeField(auto_now_add= True, null=True,  editable=False)

    def get_absolute_url(self):
        return reverse('dashboard')
    
