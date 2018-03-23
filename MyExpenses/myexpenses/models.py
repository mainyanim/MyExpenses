from django.db import models
from django.utils import timezone

# Create your models here.

class Expense(models.Model):
    date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    price = models.IntegerField()
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Note(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name='notes')
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField(null = True, max_length=200)

    def __str__(self):
        return self.text
