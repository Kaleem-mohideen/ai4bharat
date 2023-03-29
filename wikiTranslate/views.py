from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .utils import *
from .forms import *
from nltk import tokenize
from django.views.decorators.csrf import csrf_exempt


def index(request):
	tar_lang = TargetLang.objects.all()
	form = ProjectForm()
	
	return render(request, 'wikiTranslate/index.html', context={'tar_lang':tar_lang, 'form':form})

def sentenceSplit(request):
	if request.method == "POST":
		form = ProjectForm(request.POST)
		if form.is_valid():
			project = form.save()
			project.refresh_from_db()
			summary = get_summary(project.articleTitle)
			sentences = tokenize.sent_tokenize(summary)
			lang = {'Bengali': 'bn', 'Gujarati':'gu', 'Hindi':'hi', 'Kannada':'kn', 'Malayalam':'ml', 'Marathi':'mr', 'Nepali': 'ne', 'Oriya':'or', 'Panjabi':'pa', 'Sinhala':'si', 'Tamil': 'ta', 'Telugu': 'te', 'Urdu': 'ur'}
			tar_lang= lang[project.target_lang.languages]
			for each_sentence in sentences:
				translation = translate(each_sentence, tar_lang)
				sentenceobj, created = Sentence.objects.get_or_create(project_id=project, original_sentence=each_sentence, translated_sentence=translation)

			sentences = Sentence.objects.filter(project_id= project).order_by('sentence_id')
	return render(request, 'wikiTranslate/sentenceSplit.html', {'project':project, 'sentences':sentences})

@csrf_exempt
def display(request, pid):
	projectObj = Project.objects.filter(project_id=pid).first()
	if request.method == "POST":
		sentences = Sentence.objects.filter(project_id= projectObj).order_by('sentence_id')
		for sentence in sentences:
			# print('sentencesEach', request.POST[f'translated_text{sentence.sentence_id}'])
			sentence, created = Sentence.objects.get_or_create(project_id = projectObj, sentence_id = sentence.sentence_id, original_sentence=sentence.original_sentence)
			print(sentence)
			sentence.translated_sentence = request.POST[f'translated_text{sentence.sentence_id}']
			sentence.save()
	sentences = Sentence.objects.filter(project_id= projectObj).order_by('sentence_id')
	return render(request, 'wikiTranslate/display.html', {'sentences': sentences})

def project_list(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'wikiTranslate/project_list.html', context)