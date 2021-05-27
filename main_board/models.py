from django.db import models
from django.contrib.auth.models import User
# Create your models here


class user_info(models.Model):

    MF={
        'male':'male',
        'famale': 'famale'
    }
    city = {
        'city1': 'khartoum',
        'city2': 'bahry',
        'city3': 'omdurman',
    }

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    fristName=models.CharField(max_length=50,null=True)
    lastName = models.CharField(max_length=50,null=True)
    emile=models.EmailField()
    numpper=models.CharField(max_length=50,null=True)
    gender=models.CharField(max_length=7, null=True)
    place=models.CharField(max_length=50,null=True)
    image=models.ImageField(blank=True,null=True)
    book1=models.CharField(max_length=25,blank=True)
    book2=models.CharField(max_length=25,blank=True)
    book3=models.CharField(max_length=25,blank=True)
    book4=models.CharField(max_length=25,blank=True)

class order_up(models.Model):
     supject=models.CharField(max_length=100,null=True)
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     raelName_order = models.CharField(max_length=25)
     nummper_order = models.CharField(max_length=25)
     place_order = models.CharField(max_length=25)
     book1_order = models.CharField(max_length=25, blank=True)
     book2_order = models.CharField(max_length=25, blank=True)
     book3_order = models.CharField(max_length=25, blank=True)
     book4_order = models.CharField(max_length=25, blank=True)
     stats_order = models.CharField(max_length=25, blank=False, default='Wating')




