from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from . import models
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField

class EntryAdmin(MarkdownModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}
    # Next line is a workaround for Python 2.x
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}
    filter_horizontal = ("tags",)

class TaskAdmin(MarkdownModelAdmin):
    list_display = ("title", "created",)
    list_filter=("created",)
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}
    filter_horizontal = ("tags",)


admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Task, TaskAdmin)

