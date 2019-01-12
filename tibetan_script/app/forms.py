from django import forms

class TextInputForm(forms.Form):
    orgin_text = forms.Textarea()
