from django.db import models

# Create your models here.


class About(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=500)
    image = models.ImageField(upload_to='about/')
    from_adress = models.CharField(max_length=80)
    lives_in = models.CharField(max_length=80)
    age = models.IntegerField()
    gender = models.CharField(max_length=15)
    cv = models.FileField(upload_to='cv', help_text='upload your cv')

    def __str__(self):
        return self.name

SKILL_TYPE = (
    ('Coding','Coding'),
    ('Design','Design')
)
class Skills(models.Model):
    skill = models.CharField(max_length=100)
    percentage = models.IntegerField()
    type = models.CharField(max_length=10,choices=SKILL_TYPE)
    def __str__(self):
        return self.skill

class Education(models.Model):
    year = models.IntegerField()
    title = models.CharField(max_length=100)
    place = models.CharField(max_length=50)
    description = models.CharField(max_length=300) 

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-year',)

class Experience(models.Model):
    year = models.IntegerField()
    title = models.CharField(max_length=100)
    place = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-year',)


class Service(models.Model):
    icon = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Projects(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/')
    tags = models.CharField(max_length=100)

    def __str__(self):
        return self.name