from django import forms
class AddItemForm(forms.Form):
    name=forms.CharField()
    qunatity=forms.IntegerField()
