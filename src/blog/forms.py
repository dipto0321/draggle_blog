from django import forms


class BlogPostForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={"class": "validate", "id": "title"})
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={"class": "materialize-textarea", "id": "content"})
    )
