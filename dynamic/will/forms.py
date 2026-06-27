from django import forms
class QRcode(forms.Form):
    text = forms.CharField(label="Enter text or URL", max_length=200)