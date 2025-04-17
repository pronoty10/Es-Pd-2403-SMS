from django.db import models

# Create your models here.

class Student(models.Model):
    GENDER=[
     ("MALE","MALE"),
     ("FEMALE","FEMALE"),
     ("OTHERS","OTHERS"),

    ]


    RELEGION=[

        ("ISLAM","ISLAM"),
        ("HINDU","HINDU"),
        ("OTHERS","OTHERS"),
    ]

    prime_id=models.AutoField(primary_key=True,unique=True,editable=False,blank=False,null=False)
    name= models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    image=models.ImageField(upload_to='image/',default='def.png',blank=True)
    religion=models.CharField(choices=RELEGION,max_length=10)
    gender=models.CharField(choices=GENDER,max_length=10)