from django import forms

class TodosForm(forms.Form):
    task=forms.CharField(widget=forms.TextInput(attrs={'class':'text_inp',}),label='Enter Your Task')
    #date = forms.DateField(widget=forms.DateInput(attrs={'id':'datepicker','class':'text_inp',}),input_formats=['%d/%m/%Y'],label='Pick Date')
    date=forms.CharField(widget=forms.TextInput(attrs={'id':'datepicker','class':'text_inp',}),label='Pick Date')
    statuses={
        ("","Select Status"),
        ("Completed","True"),
        ("Not Completed","False")
    }
    status=forms.ChoiceField(widget=forms.Select(attrs={'class':'text_inp',}),label='Status',choices=statuses)