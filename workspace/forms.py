from django import forms
from marketplace.models import Nft
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


    class Meta:
        fields = ('username','password',)

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class CreateForm(forms.ModelForm):
    class Meta:
        model = Nft
        fields = ('img','name','description','collection','tegs','prise','is_sold')

        widgets = {
            'img':forms.FileInput(attrs={}),
            'name':forms.TextInput(attrs={'placeholder':'Названия','class':'input'}),
            'description':forms.Textarea(attrs={'placeholder':'Описания','cols':"55",'rows':"25",'class':'textrea'}),
            'collection':forms.Select(attrs={'placeholder':'Колекция'}),
            'tegs':forms.CheckboxSelectMultiple(attrs={'placeholder':'Теги'}),
            'prise':forms.NumberInput(attrs={'placeholder':'Цена','class':'input'}),
        }


        is_sold = forms.BooleanField(required=False)