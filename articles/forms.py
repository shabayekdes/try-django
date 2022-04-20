from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean(self):
        cleaned_data = self.cleaned_data
        print('all data', cleaned_data)
        title = cleaned_data.get('title')
        content = cleaned_data.get("content")
        if title.lower().strip() == "the office":
            self.add_error('title', 'This title is taken.')
            # raise forms.ValidationError('This title is taken.')
        if "office" in content or "office" in title.lower():
            self.add_error('content', "Office cannot be in content")
            raise forms.ValidationError("Office is not allowed")
        return cleaned_data
