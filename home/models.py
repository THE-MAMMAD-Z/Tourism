from django.db import models
from location_field.models.plain import PlainLocationField


class CommonInfo(models.Model):
    name = models.CharField(max_length=250 , default='default name')
    email = models.EmailField(default="default@gmail.com")
    message = models.TextField(default="default message for models")
    created_time=models.DateTimeField(auto_now_add=True,null=True)


    class Meta:
        abstract = True




class Place(models.Model):
    name = models.CharField(max_length=300)
    phone = models.IntegerField()
    description = models.TextField()
    address = models.TextField()
    rate = models.IntegerField()
    city = models.CharField(max_length=100)
    created_time=models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="places/")
    location = PlainLocationField(based_fields=['city'], zoom=7)


    place_type = [
    ("Restaurant", "Restaurant"),
    ("Park", "Park"),
    ("Zoo","Zoo"),
    ("Museum","Museum"),
    ("Amusement Park","Amusement Park"),
    ("Mall","Mall"),
    ('Tower',"Tower"),
    ('Historical','Historical'),
    ("Other","Other")
    ]
    
    location_type = models.CharField(max_length=14,choices=place_type)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(rate__lte=5), name='rate_lte_5')
        ]

    def __str__(self):
        return self.name
    

class Comment(CommonInfo):
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    active=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Contact(CommonInfo):
    subject = models.CharField(max_length=300)

    def __str__(self):
        return self.subject
    