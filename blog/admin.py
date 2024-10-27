from django.contrib import admin
from .models import Document, PPTDocument
# Register your models here.


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')


@admin.register(PPTDocument)
class PPTDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')

