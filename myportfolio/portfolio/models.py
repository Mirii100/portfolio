from django.db import models



class Profile(models.Model):
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='images')

class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio_images/')  # Upload folder inside MEDIA_ROOT

    def __str__(self):
        return self.title