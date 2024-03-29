from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
import datetime

from django.dispatch import receiver

STAGE_CHOICES = [('Not started', 'Not started'), ('Application submitted', 'Application Submitted'), ('Online tests completed', 'Online tests completed'),
                 ('Phone / Video interview received', 'Phone / Video interview received'), ('Phone / Video interview complete', 'Phone / Video interview complete'),
                 ('Final stage interview received', 'Final stage interview received'), ('Rejected', 'Rejected')]


class Application(models.Model):
    PRIORITY_CHOICES = [('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')]
    priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES)
    industry = models.CharField(max_length=150, null=True, blank=True)
    company = models.CharField(max_length=150)
    job_title = models.CharField(max_length=150, null=True)
    open_date = models.DateField(null=True, blank=True)
    close_date = models.DateField(null=True, blank=True)
    stage = models.CharField(max_length=150, choices=STAGE_CHOICES, default=STAGE_CHOICES[0][0])
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    link = models.URLField(default="#")
    creation_time = models.DateTimeField(auto_now_add=True)

    notes = models.ForeignKey(
        'Notes', on_delete=models.CASCADE, related_name='notes', null=True, blank=True,
    )

    def __str__(self):
        try:
            str = self.user.email + ": " + self.job_title + " @ " + self.company
        except:
            str = "Unknown"
        return str

    def get_absolute_url(self):
        return reverse('table')

    def save(self, *args, **kwargs):
        is_new = not self.pk
        if is_new:
            self.notes = Notes.objects.create()
        super().save(*args, **kwargs)


class Notes(models.Model):

    notes1 = models.TextField(default="", blank=True, verbose_name="Research phase")
    notes2 = models.TextField(default="", blank=True, verbose_name="Phone / Video interview preparation")
    notes3 = models.TextField(default="", blank=True, verbose_name="Phone / Video interview reflections")
    notes4 = models.TextField(default="", blank=True, verbose_name="Final interview preparation")
    notes5 = models.TextField(default="", blank=True, verbose_name="Reflection on job outcome")

    def __str__(self):
        return "Notes"

    def get_absolute_url(self):
        return reverse('table')

class AutoAddApplication(Application):
    user = None

    def __str__(self):
        return 'Automatic application ' + self.company