from django import forms

class OriginInputForm(forms.Form):
    orgin_text = forms.CharField ( widget=forms.widgets.Textarea() )
