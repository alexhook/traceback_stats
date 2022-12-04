from django.contrib import admin
from django.template.defaultfilters import truncatechars
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

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
    readonly_fields = ('creation_date',)
    ordering = ('id', )

    @admin.display(description=_('Name'))
    def name(self, idea):
        return idea

    @admin.display(description=_('Description'))
    def short_description(self, idea):
        return truncatechars(idea.description, 1000)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'clickable_issue_url', 'type', 'project', 'creation_date')
    list_filter = ('type', 'project', 'creation_date')
    search_fields = ('id', 'issue_url')
    readonly_fields = ('creation_date', )
    ordering = ('id', )

    @admin.display(description=_('Name'))
    def name(self, event):
        return event

    @admin.display(description=_('Issue URL'))
    def clickable_issue_url(self, event):
        return format_html("<a href='{url}'>{url}</a>", url=event.issue_url)
