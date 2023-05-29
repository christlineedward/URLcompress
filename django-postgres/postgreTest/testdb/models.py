from django.db import models

# Create your models here.
class URLMapping(models.Model):
    # Define the fields of the URLMapping model

    # CharField to store the short code, with a maximum length of 8 characters
    short_code = models.CharField(max_length=8, unique=True)

    # URLField to store the long URL
    long_url = models.URLField()

    def __str__(self):
        # Define a string representation for the URLMapping object
        
        # It will return the short code when the object is printed as a string
        return self.short_code