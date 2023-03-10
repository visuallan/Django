from django.db import models

# Create your models here.
class User(models.Model):
    gender = (('male','男'),
              ('female','女'))
    username = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    c_time = models.DateTimeField(auto_now_add=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'

