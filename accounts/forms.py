from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


from core.forms import BaseForm, BaseModalForm



class CustomUserCreationForm(BaseModalForm,UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.fields.get('dob') is not None:
            self.fields['dob'].widget = forms.TextInput(attrs={
                'type':'date',
                'placeholder':self.fields['dob'].label,
                'class':self.input_css+' border-red-700 dark:border-red-500 ' if self.errors is not None else self.input_css

            })
    class Meta:
        model = get_user_model()
        fields = ("email",'dob','first_name','last_name','password1','password2','image')



class AdminCreationForm(UserCreationForm):

    
    class Meta:
        model = get_user_model()
        fields = ("email",)




class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ("email",)



class LoginForm(BaseForm,AuthenticationForm):
    pass