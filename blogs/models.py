from django.db import models
# Create your models here.

class Blogs(models.Model):
    name = models.CharField(max_length=255)
    des = models.TextField()
    image = models.ImageField(upload_to="blogs_image",blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
       return self.name