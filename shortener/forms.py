from django import forms

class Form(forms.Form):
    url = forms.CharField(label='Submit Url')

    def clean(self):
        cleaned_data = super(Form, self).clean()
        url = cleaned_data.get('url')
        print(url)

    def clean_url(self):
        url = self.cleaned_data['url']