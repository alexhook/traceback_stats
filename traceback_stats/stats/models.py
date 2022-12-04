from django.db import models
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_('Name'))

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.name


class EventType(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_('Name'))

    class Meta:
        verbose_name = _('Event type')
        verbose_name_plural = _('Event types')

    def __str__(self):
        return self.name


class OptimizeIdea(models.Model):
    event_type = models.ForeignKey(
        'stats.EventType', on_delete=models.CASCADE, related_name='optimize_ideas', verbose_name=_('Event type'))
    description = models.TextField(verbose_name=_('Description'))
    creation_date = models.DateField(auto_now_add=True, verbose_name=_('Creation date'))

    class Meta:
        verbose_name = _('Optimize idea')
        verbose_name_plural = _('Optimize ideas')

    def __str__(self):
        return _('Idea #{}').format(self.id)


class Event(models.Model):
    type = models.ForeignKey(
        'stats.EventType', on_delete=models.CASCADE, related_name='events', verbose_name=_('Type'))
    project = models.ForeignKey(
        'stats.Project', on_delete=models.CASCADE, related_name='events', verbose_name=_('Project'))
    traceback = models.TextField(verbose_name=_('Traceback'))
    how_to_fixed = models.TextField(blank=True, verbose_name=_('How to fixed?'))
    creation_date = models.DateField(auto_now_add=True, verbose_name=_('Creation date'))

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __str__(self):
        return _('Event #{}').format(self.id)
