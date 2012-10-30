from django import forms
from django.forms import ModelForm

from issues.models import Category, Issue
from articleflow.models import Article


#class IssueForm(forms.Form):
#    category = forms.ModelChoiceField(queryset=Category.objects.all())
#    description = forms.CharField(widget=forms.Textarea)
#    article_pk = forms.ModelChoiceField(queryset=Article.objects.all(), widget=forms.HiddenInput())

class IssueForm(ModelForm):
    
    class Meta:
        model = Issue
        exclude = ('error','status','submitter')
        widgets = {
            'article' : forms.HiddenInput(),
            }
        
    