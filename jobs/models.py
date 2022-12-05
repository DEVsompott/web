from django.db import models

# Create your models here.
class Jobs(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="jobs_image",blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
       return self.name