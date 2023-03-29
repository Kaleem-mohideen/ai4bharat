from django.contrib import admin
from .models import *

@admin.register(Project)
class MyProjectModel(admin.ModelAdmin):
    model = Project
    ordering = ['articleTitle', 'target_lang']
    list_display = ('project_id', 'articleTitle', 'target_lang')

admin.site.register(TargetLang)

@admin.register(Sentence)
class MySentenceModel(admin.ModelAdmin):
	model = Sentence
	ordering = ['project_id',  'sentence_id']
	list_display = ('project_id', 'sentence_id', 'original_sentence', 'translated_sentence')