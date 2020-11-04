from django.db import models
from django.utils.timezone import now

class Firm(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, default=None, blank=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=300, default="")
    open_date = models.DateField()
    close_date = models.DateField()
    date_created = models.DateField(auto_now_add=True)
    intro_text = models.TextField()
    firm = models.ForeignKey(
        'Firm',
        on_delete=models.CASCADE,
        related_name='article',
        null=True,
        blank=True,
    )

    def __str__(self):
        if self.firm is not None:
            return "Article on " + self.firm.__str__()
        else:
            return "General article created on " + self.date_created.__str__()

class Section(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    article = models.ForeignKey(
        'Article',
        on_delete=models.CASCADE,
        related_name='section',
    )