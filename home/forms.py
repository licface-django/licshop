from django import forms

class uploadForm(forms.Form):
    #title = forms.CharField(max_length= 50)
    file = forms.FileField()
    
class searchForm(forms.Form):
    query = forms.CharField(100, 3, True, "search music", widget = forms.TextInput(attrs = {'class': 'myFIELD',}))
    #query = forms.CharField(100, 3, True, "search music")