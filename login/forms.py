from crispy_forms.bootstrap import StrictButton
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import ModelForm, forms, Form, CharField, IntegerField, PasswordInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit, HTML, Button
from django.utils.safestring import mark_safe

from .models import VerifiedUser


class CustomInputField(Field):
    template = 'login/CustomInputField.html'


class UserForm(UserCreationForm):
    class Meta:
        model = VerifiedUser
        fields = ("username",)
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'login100-form validate-form'
        self.helper.form_action = "/auth/register/"
        self.helper.form_id = "RegistrationForm"
        self.fields["username"].label = "Email Address"
        self.fields["username"].widget.attrs["type"] = "email"

        self.helper.attrs['onSubmit'] = "hashing(event)"
        fields = ["username", "password1", "password2"]
        for field in fields:
            self.fields[field].help_text = None
        self.helper.layout = Layout(
            Div(
                CustomInputField('username', css_class='input100', data_validate="Username is required", type="email",
                                 id='username'),
                CustomInputField('password1', css_class='input100', data_validate="Password must be 8 characters long",
                                 css_id='raw_password1'),
                CustomInputField('password2', css_class='input100', data_validate="Password must be same as above",
                                 css_id='raw_password2'),
                Div(
                    Submit('Submit', 'Submit', css_class="login100-form-btn", css_id='login_submit', ),
                    css_class="container-login100-form-btn"
                )

            )
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.username.lower()
        user.set_password(self.cleaned_data["password1"])
        user.set_hash()
        if commit:
            user.save()
        return user


class ResetForm(UserCreationForm):
    class Meta:
        model = VerifiedUser
        fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'login100-form validate-form'
        self.helper.form_id = "RegistrationForm"
        self.helper.attrs['onSubmit'] = "hashing2(event)"
        fields = ["password1", "password2"]
        for field in fields:
            self.fields[field].help_text = None
        self.helper.layout = Layout(
            Div(
                CustomInputField('password1', css_class='input100', data_validate="Password must be 8 characters long",
                                 css_id='raw_password1'),
                CustomInputField('password2', css_class='input100', data_validate="Password must be same as above",
                                 css_id='raw_password2'),
                Div(
                    Submit('Submit', 'Submit', css_class="login100-form-btn", css_id='login_submit', ),
                    css_class="container-login100-form-btn"
                )

            )
        )

    def save(self, user, commit=True):
        user.set_password(self.cleaned_data["password1"])
        user.set_hash()
        if commit:
            user.save()
        return user


class OTPForm(Form):
    RegisterNo = CharField()
    OTP = CharField()
    Password = CharField(widget=PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'login100-form validate-form'
        self.helper.form_action = "/auth/otp/"
        self.helper.attrs['onSubmit'] = "hashing1(event)"
        self.helper.layout = Layout(

            CustomInputField('RegisterNo', css_class='input100', data_validate="Register Number is required"),
            Div(
                CustomInputField('OTP', css_class='input100', data_validate="OTP is required"),
                CustomInputField('Password', css_class='input100', data_validate="Password is required"),
                css_id='otp', style="display: none;", css_class="container"
            ),
            Div(
                StrictButton('send otp', css_class="login100-form-btn", css_id="otp_btn"),
                css_class="container-login100-form-btn",
            ),
            Div(
                Button('submit', 'submit', css_class="login100-form-btn", css_id="submit_btn", hidden=True, ),
                css_class="container-login100-form-btn",

            )
        )


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'login100-form validate-form'
        fields = ['username', 'password']
        self.fields["username"].label = "Email Address"

        self.helper.form_action = "/auth/"
        self.helper.attrs['onSubmit'] = "hashing1(event)"
        for field in fields:
            self.fields[field].help_text = None
        self.helper.layout = Layout(
            Div(
                CustomInputField('username', css_class='input100', data_validate="Username is required"),
                CustomInputField('password', css_class='input100', data_validate="Password is required"),
                Div(
                    Submit('Submit', 'Submit', css_class="login100-form-btn", ),
                    css_class="container-login100-form-btn"
                )
            )
        )


class OTP_resendform(Form):
    Email_Address = CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'login100-form validate-form'
        self.helper.form_action = "/auth/resend/"
        self.helper.attrs['onSubmit'] = ""
        self.helper.layout = Layout(

            CustomInputField('Email_Address', css_class='input100', data_validate="Register Number is required"),
            Div(
                Submit('submit', 'submit', css_class="login100-form-btn", css_id="submit_btn"),
                css_class="container-login100-form-btn",

            )
        )
