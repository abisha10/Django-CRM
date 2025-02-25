from django.db import models

# Create your models here.
class Record(models.Model):
    creaed_at = models.DateTimeField(auto_now_add=True)
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.TextField()
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")