from django import forms


class ContactForm(forms.Form):
    firstname = forms.CharField(
        widget=forms.TextInput(attrs={"class": "validate", "id": "first_name"})
    )
    lastname = forms.CharField(
        widget=forms.TextInput(attrs={"class": "validate", "id": "last_name"})
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={"class": "validate", "id": "email"})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"class": "materialize-textarea", "id": "message"})
    )
