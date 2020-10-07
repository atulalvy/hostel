from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from .models import VerifiedUser
from .forms import UserForm, OTP_resendform, LoginForm,ResetForm


class AuthenticationView(LoginView):
    template_name = 'login/login.html'
    form_class = LoginForm
    extra_context = {
        'form1': UserForm,
        'reset':True
    }
    redirect_authenticated_user = True

    def get_success_url(self):
        if self.request.user.Department_portal == "office":
            return "/office/"
        elif self.request.user.Department_portal!="student":
            return  "/department/"
        if not self.request.user.applications.Pincode:
            return "/apply/"
        return "/apply/view/"



    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.POST['username'] = request.POST['username'].lower()
        request.POST._mutable = False

        try:

            verifieduser = VerifiedUser.objects.get(username=request.POST['username'].lower())
            if (verifieduser.is_active):
                return super().post(request, *args, **kwargs)

            context = {'error_heading': 'A Verification link has been sent to your email account',
                       'error_message': 'Please click on the link that has been sent to your email account to verify '
                                        '   your email and continue login again',
                       "resend":True}
        except VerifiedUser.DoesNotExist:

            context = {'error_heading': 'Seems like you are not registered yet',
                       'error_message': 'Please SignUp to continue'}
        return render(request, 'login/login.html', context=context)


def register(request):
    if request.method == 'POST':
        context = {
            "form1": LoginForm,
            "login": 'Sign Up',
            'signup': 'Login',

        }
        user = UserForm(request.POST)
        if (user.is_valid()):
            user = user.save()

            if user.is_active:
                return HttpResponseRedirect('/apply/')
            else:
                context = {'error_heading': 'A Verification link has been sent to your email account',
                           'error_message': 'Please click on the link that has been sent to your email account to verify '
                                            '   your email and continue login again',
                           "resend": True}
                return render(request, 'login/login.html', context=context)

        else:
            context["form"] = user
            user.show_error = True
            return render(request, 'login/login.html', context=context)

    else:
        return HttpResponseRedirect("/auth/")


def verification(request, token):
    print(token)
    try:
        verifying_user = VerifiedUser.objects.get(userhash=token)
        verifying_user.is_active = True
        verifying_user.save()
        context = {
            'form1': UserForm,
            'form': LoginForm,
            'valid': "Successfully Verified . Login To Apply"
        }
    except VerifiedUser.DoesNotExist:
        context = {'error_heading': 'Seems like your are verifying a old otp',
                   'error_message': 'Please use the latest otp to continue'}

    return render(request, 'login/login.html', context=context)


def resend_otp(request):
    context = {
        "form": OTP_resendform,
        "login": "Resend OTP"
    }
    if request.method == "POST":
        form = OTP_resendform(request.POST)
        email = form["Email_Address"].value().lower()
        try:
            user = VerifiedUser.objects.get(username=email)
            if user.is_active:
                return HttpResponseRedirect('/apply/')
            else:
                user.set_hash()
                context = {'error_heading': 'A Verification link has been sent to your email account',
                           'error_message': 'Please click on the link that has been'
                                            ' sent to your email account to verify'
                                            ' your email and continue login again',
                           }
        except VerifiedUser.DoesNotExist:
            context = {'error_heading': 'Seems like you are not registered yet',
                       'error_message': 'Please SignUp to continue'}
    return render(request, 'login/login.html', context=context)


def reset_password(request):
    resend_form = OTP_resendform()
    resend_form.helper.form_action = "/auth/reset_pass/"
    context = {
        "form": resend_form,
        "login": "Resend Password"
    }
    if request.method == "POST":
        form = OTP_resendform(request.POST)
        email = form["Email_Address"].value().lower()
        try:
            user = VerifiedUser.objects.get(username=email)
            user.reset_hash()
            context = {'error_heading': 'A Verification link has been sent to your email account',
                       'error_message': 'Please click on the link that has been'
                                        ' sent to your email account to verify'
                                        ' your email and Reset the password',
                       }
        except VerifiedUser.DoesNotExist:
            context = {'error_heading': 'Seems like you are not registered yet',
                       'error_message': 'Please SignUp to continue'}
    return render(request, 'login/login.html', context=context)


def reset_confirm(request, token):
    print(token)
    context = {}
    if request.method=="GET":
        try:
            verifying_user = VerifiedUser.objects.get(userhash=token)
            reform = ResetForm()
            reform.helper.form_action = "/auth/reset"+token+'/'
            context = {
                'form': reform,
                'valid': "Successfully Verified . reset password to continue"
            }

        except VerifiedUser.DoesNotExist:
            context = {'error_heading': 'Seems like you are verifying a old otp',
                       'error_message': 'Please use the latest otp to continue'}

    else:
        try:
            verifying_user = VerifiedUser.objects.get(userhash=token)
            reform = ResetForm(request.POST)
            if reform.is_valid():
                verifying_user.is_active = True
                verifying_user.save()
                reform.save(verifying_user)
                return HttpResponseRedirect("/auth/")

        except VerifiedUser.DoesNotExist:
            context = {'error_heading': 'Seems like you are verifying a old otp',
                       'error_message': 'Please use the latest otp to continue'}

    return render(request, 'login/login.html', context=context)
