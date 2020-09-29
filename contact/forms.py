from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={'placeholder': 'Enter Full Name'}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'placeholder': 'Enter Email'}))
    comment = forms.CharField(label="Comment", widget=forms.Textarea(attrs={'placeholder': 'Comment'}))

