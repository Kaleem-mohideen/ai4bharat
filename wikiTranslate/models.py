from django.db import models

# Create your models here.

class TargetLang(models.Model):
	languages = models.CharField(max_length=200, verbose_name='Target Languages')

	def __str__(self):
		return self.languages

class Project(models.Model):
	project_id = models.AutoField(primary_key=True)
	articleTitle = models.CharField(max_length=500, null=False)
	target_lang = models.ForeignKey(TargetLang, on_delete=models.SET_NULL, null=True, verbose_name='Target Language')


	# class Meta:
	# 	unique_together = (("articleTitle","target_lang"),)
	def __str__(self):
		return str(self.project_id)


class Sentence(models.Model):
	project_id = models.ForeignKey(Project, to_field="project_id", on_delete=models.CASCADE, blank=False, null=True)
	sentence_id = models.AutoField(primary_key=True)
	original_sentence = models.CharField(max_length=1000, null=False)
	translated_sentence = models.CharField(max_length=1000, null=False)
	def __str__(self):
		return str(self.sentence_id)
