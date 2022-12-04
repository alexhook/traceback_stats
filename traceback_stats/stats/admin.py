from django.contrib import admin
from django.template.defaultfilters import truncatechars

from traceback_stats.stats.models import Event, EventType, Project, OptimizeIdea


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


@admin.register(OptimizeIdea)
class OptimizeIdeaAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'event_type')
    list_filter = ('event_type', )
    ordering = ('id', )

    @admin.display()
    def name(self, idea):
        return idea

    @admin.display(description='description')
    def short_description(self, idea):
        return truncatechars(idea.description, 1000)


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
