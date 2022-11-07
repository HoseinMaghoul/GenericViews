from django import forms


class PostForm(forms.ModelForm):
    author = forms.CharField()
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    created_on = forms.DateTimeField()



