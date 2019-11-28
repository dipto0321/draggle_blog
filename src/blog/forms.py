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
        instance = self.instance
        qs = BlogPost.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("This title has been already taken")
        return title
