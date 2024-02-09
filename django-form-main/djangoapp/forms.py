from django import forms

class RegisterForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username','class':'register'}))
    password=forms.CharField(widget=forms.PasswordInput)
    mob=forms.IntegerField(widget=forms.NumberInput)
    email=forms.EmailField(widget=forms.EmailInput)
    date_of_birth=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    time=forms.TimeField(widget=forms.TimeInput(attrs={'type':'time'}))
    datetime=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    data=[['male','male'],['female','female']]
    gender=forms.CharField(widget=forms.RadioSelect(choices=data))

    english=forms.BooleanField(widget=forms.CheckboxInput)
    Kannada=forms.BooleanField(widget=forms.CheckboxInput)

    dataa=[['kannada','kannada'],['hindi','hindi'],['malayalam','malayalam']]
    languages=forms.CharField(widget=forms.CheckboxSelectMultiple(choices=dataa))

    lang=forms.CharField(widget=forms.Select(choices=dataa))

