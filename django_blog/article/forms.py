from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 50:
            raise forms.ValidationError("Name must be at most 50 characters long.")
        return name
    
    def clean_body(self):
        body = self.cleaned_data['body']
        if len(body) > 1000:
            raise forms.ValidationError("Body must be at most 1000 characters long.")
        return body

        

