from django import forms
from .validators import validate_url
class SubmitUrlForm(forms.Form):
    url=forms.CharField(
        label='', 
        validators=[validate_url],
        widget=forms.TextInput(
            attrs={
                "placeholder":"Eg:http://www.xyz.com",
                "Class": "form-control "
            }
        )
    )


#def clean_url(self):
 #   url=self.cleaned_data['url']
  #  if "http" in url:
   #     return url
   # return "http://"+url