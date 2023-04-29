from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Ticket(models.Model):
    low = "low"
    medium = "medium"
    urgent = "urgent"

    urgency_choices = (
        (low, 'low'),
        (medium, 'medium'),
        (urgent, 'urgent')
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    urgency = models.CharField(max_length=100, choices=urgency_choices, default="low")
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)

    def __str__(self):
        return self.body    


    



