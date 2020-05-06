from django.contrib import admin
from .models import Snippet


# Register your models here.
class SnippetAdmion(admin.ModelAdmin):
    list_display = ['created', 'title', 'code', 'linenos',
                    'language', 'style', 'owner', 'highlighted']


admin.site.register(Snippet, SnippetAdmion)
