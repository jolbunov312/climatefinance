from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Project(models.Model):

    def __str__(self):
        return self.project_name
    

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    project_name = models.CharField(max_length=200)
    project_desc = models.CharField(max_length=200)
    project_price = models.IntegerField()
    project_image = models.CharField(max_length=500,default="https://geekflare.com/wp-content/uploads/2023/03/img-placeholder.png")

    def get_absolute_url(self):
        return reverse('food:detail', kwargs={'pk':self.pk})
    