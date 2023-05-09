from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    role = forms.ChoiceField(choices=[('librarian', 'Librarian'), ('member', 'Member')])

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    role = forms.ChoiceField(choices=[('member', 'Member'), ('librarian', 'Librarian')])

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        role = cleaned_data.get('role')


        return cleaned_data
