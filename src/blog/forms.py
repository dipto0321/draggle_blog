from django import forms
from .models import BlogPost


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "validate"}),
            "content": forms.Textarea(attrs={"class": "materialize-textarea"}),
        }
