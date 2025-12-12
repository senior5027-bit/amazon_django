from django import forms
import re

class SignupForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'})
    )
    repassword = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'تکرار رمز عبور'})
    )

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < 8:
            raise forms.ValidationError('رمز عبور باید حداقل ۸ کاراکتر باشد')

        if not re.search(r'[A-Z]', password):
            raise forms.ValidationError('حداقل یک حرف بزرگ لازم است')

        if not re.search(r'\d', password):
            raise forms.ValidationError('حداقل یک عدد لازم است')

        if not re.search(r'[!@#$%^&*]', password):
            raise forms.ValidationError('حداقل یک کاراکتر خاص لازم است')

        return password

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('repassword'):
            raise forms.ValidationError('رمز عبور و تکرار آن یکسان نیستند')
