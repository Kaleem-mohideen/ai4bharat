from django import forms
from .models import Project, Sentence

class ProjectForm(forms.ModelForm):
    class Meta: 
        model = Project 
        fields = ['articleTitle', 'target_lang']



class SentenceForm(forms.ModelForm):
    original_sentence = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    project_id = forms.CharField(widget = forms.HiddenInput(), required = False)

    def __init__(self, *args, **kwargs):
        super(SentenceForm, self).__init__(*args, **kwargs)

        for fieldname in ['original_sentence', 'translated_sentence']:
            for key, value in self.fields[fieldname].error_messages.items():
                self.fields[fieldname].required = False


    class Meta: 
        model = Sentence 
        fields = ['original_sentence', 'translated_sentence']