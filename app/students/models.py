from django.db import models


def student_image_path(instance, filename):
    return 'student_{0}/{1}'.format(instance.student_id, filename)


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=256)
    student_id = models.CharField(max_length=256)
    GPA = models.FloatField()
    picture = models.ImageField(upload_to=student_image_path)
