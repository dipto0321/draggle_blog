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

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        qs = BlogPost.objects.filter(title__iexact=title)
        if qs.exists():
            raise forms.ValidationError("This title has been already taken")
        return title
