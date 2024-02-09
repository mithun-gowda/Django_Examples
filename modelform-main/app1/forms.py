from django import forms
from .models import TrainerModel

class TrainerForm(forms.ModelForm):
    class Meta:
        model=TrainerModel
        #fields=['empid','name','experience','date_of_joining','salary']  #one way to display selected columns\

        fields='__all__'  #shortcut to get all the items

        #exclude=['name']  #exclude any field it will dispaly other field leaving mentioned field


        widgets={
            'empid':forms.TextInput(attrs={'placeholder':'Employee ID'}),
            'date_of_joining':forms.DateInput(attrs={'type':'date'}),
        }
    #def clean(self): #its display above the form error
    #to validate
    #clean_filed method down one  (it will display error down the field)
    def clean_name(self):
        name=self.cleaned_data['name']
        if not (4<= len(name) <=12):
            raise forms.ValidationError('Name should have minimum 4 and Max 12')

        return name  #we have to return in  clean_feild