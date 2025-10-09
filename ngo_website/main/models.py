from django.db import models

class Quote(models.Model):
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text[:50]


class Mission(models.Model):
    title = models.CharField(max_length=200, default="Our Mission")
    content = models.TextField()

    def __str__(self):
        return self.title


class SideImage(models.Model):
    POSITION_CHOICES = [
        ("left", "Left Side"),
        ("right", "Right Side"),
    ]
    image = models.ImageField(upload_to="side_images/")
    position = models.CharField(max_length=10, choices=POSITION_CHOICES)

    def __str__(self):
        return f"{self.position} - {self.image.name}"
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=5)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    photo = models.ImageField(upload_to='team_photos/')

    def __str__(self):
        return self.name