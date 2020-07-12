from django.db import models
from django.urls import reverse
from django.utils import timezone
from colorfield.fields import ColorField
from colour import Color
from .validators import validate_is_glb


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Game(models.Model):
    unityroom_url = models.CharField(max_length=255)
    def __str__(self):
        return self.unityroom_url

class Video(models.Model):
    url = models.CharField(max_length=255)
    def __str__(self):
        return self.url

class Model3D(models.Model):
    glb = models.FileField(upload_to="3dmodels/", null=False, validators=[validate_is_glb])
    def __str__(self):
        return self.glb.url

class Genre(models.Model):
    title = models.CharField(max_length=255, null=False, default="Genre")
    bg_color = ColorField(default="#ff0000")

    def __str__(self):
        return self.title

    def bg_color_lighten(self):
        delta = 0.1
        c = Color(self.bg_color)
        if(c.luminance + delta > 1):
            c.luminance = 1
        else:
            c.luminance += delta
        return c.hex_l

    def card_color(self):
        delta = 0.3
        c = Color(self.bg_color)
        if(c.luminance + delta > 1):
            c.luminance = 1
        else:
            c.luminance += delta
        return c.hex_l

    def text_color(self):
        bg_c = Color(self.bg_color)
        txt_c = Color()
        if bg_c.luminance < 0.5:
            txt_c.luminance = 1
        else:
            txt_c.luminance = 0
        return txt_c

class Work(models.Model):
    class WorkType(models.TextChoices):
        UNITY_3D = 'U3D', 'Unity 3D'
        UNITY_2D = 'U2D', 'Unity 2D'
        VIDEO = 'VID', 'VIDEO'
        MODEL_3D = 'M3D', 'MODEL 3D'
        OTHER = 'OTHER', 'OTHER'

    title = models.CharField(max_length=255)
    description = models.TextField(default="None")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    type_choice = models.TextField(choices=WorkType.choices, default=WorkType.OTHER)
    card_image = models.ImageField(null=False, upload_to='images/system/')
    goods = models.IntegerField(null=False, default=0)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, blank=True)
    model3d = models.ForeignKey(Model3D, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("work", args=[str(self.id)])

class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    text = models.TextField()
    
    def __str__(self):
        return "[{}] {}".format(self.name, self.text)


    def ja_created_at_str(self):
        return self.created_at.strftime("%Y/%m/%d %H:%M")

class LiveSchedule(models.Model):
    start = models.DateTimeField(null=False)
    end = models.DateTimeField(null=False)

    def __str__(self):
        return "{} - {}".format(self.start, self.end)
