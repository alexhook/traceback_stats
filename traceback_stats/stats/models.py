from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class EventType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    type = models.ForeignKey('stats.EventType', on_delete=models.CASCADE, related_name='events')
    traceback = models.TextField()
    project = models.ForeignKey('stats.Project', on_delete=models.CASCADE, related_name='events')
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Event #{self.id}'
