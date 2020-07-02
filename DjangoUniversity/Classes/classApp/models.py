from django.db import models

class djangoClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=False, null=False)
    courseNumber = models.PositiveSmallIntegerField(default=0, blank=False, null=False)
    instructorName = models.CharField(max_length=60, default="", blank=False, null=False)
    duration = models.FloatField(default=0.00, blank=False, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.title