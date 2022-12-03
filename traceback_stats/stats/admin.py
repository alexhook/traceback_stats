from django.contrib import admin
from django.template.defaultfilters import truncatechars

from traceback_stats.stats.models import Event, EventType, Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    search_fields = ('name', )
    ordering = ('id',)


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    search_fields = ('name', )
    ordering = ('id', )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_traceback', 'type', 'project', 'creation_date')
    list_filter = ('type', 'project', 'creation_date')
    search_fields = ('id', )
    readonly_fields = ('creation_date', )
    ordering = ('id', )

    @admin.display()
    def name(self, event):
        return event

    @admin.display(description='traceback')
    def short_traceback(self, event):
        return truncatechars(event.traceback, 1000)
