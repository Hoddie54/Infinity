from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.dispatch import receiver

STAGE_CHOICES = [('1', 'Stage 1'), ('2', 'Stage2'), ('3', 'Stage 3'),
                 ('4', 'Stage4'), ('5', 'Stage 5')]


class Application(models.Model):
    PRIORITY_CHOICES = [('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')]
    priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES)
    industry = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    open_date = models.DateField()
    close_date = models.DateField()
    stage = models.CharField(max_length=150, choices=STAGE_CHOICES, default=STAGE_CHOICES[0][0])
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    link = models.URLField(default="#")
    creation_time = models.DateTimeField(auto_now_add=True)

    notes = models.ForeignKey(
        'Notes', on_delete=models.CASCADE, related_name='notes', null=True,
    )

    def __str__(self):
        return self.user.email + ": " + self.industry + " @ " + self.company

    def get_absolute_url(self):
        return reverse('table')

    def save(self, *args, **kwargs):
        is_new = not self.pk
        if is_new:
            self.notes = Notes.objects.create()
        super().save(*args, **kwargs)


class Notes(models.Model):

    notes1 = models.TextField(default="", blank=True, verbose_name=STAGE_CHOICES[0][1])
    notes2 = models.TextField(default="", blank=True, verbose_name=STAGE_CHOICES[1][1])
    notes3 = models.TextField(default="", blank=True, verbose_name=STAGE_CHOICES[2][1])
    notes4 = models.TextField(default="", blank=True, verbose_name=STAGE_CHOICES[3][1])
    notes5 = models.TextField(default="", blank=True, verbose_name=STAGE_CHOICES[4][1])

    def __str__(self):
        return "Notes"

    def get_absolute_url(self):
        return reverse('table')

