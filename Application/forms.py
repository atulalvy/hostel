import re

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit
from crispy_forms.utils import TEMPLATE_PACK
from django.forms import ModelForm, DateField
from django.utils import timezone

from Hostel import settings
from login.models import ApplicationSettings
from .models import Applications


class CustomTextInput(Field):
    template = "Application/CustomFields/CustomTextInput.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wrapper_class = kwargs.pop("wrapper_class", "wrap-input100 validate-input m-b-26")
        self.keywords = kwargs
    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, extra_context=None, **kwargs):
        if extra_context is None:
            extra_context = {}

        extra_context = {**extra_context, **self.keywords}
        if hasattr(self, 'wrapper_class'):
            extra_context['wrapper_class'] = self.wrapper_class

        template = self.get_template_name(template_pack)

        return self.get_rendered_fields(
            form, form_style, context, template_pack,
            template=template, attrs=self.attrs, extra_context=extra_context,
            **kwargs
        )


class ApplicationForm(ModelForm):
    Course_completion_date = DateField(input_formats=settings.DATE_INPUT_FORMATS)
    Admission_date = DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = Applications
        fields = ['Registration_No', 'Name', 'Address_For_Communication', 'Permanent_Address', 'distance', 'State',
                  'District', 'Mobile_Number', 'Name_of_Guardian', 'PhoneNumber_of_Guardian', 'Year_of_Study', "Gender",
                  "Category", "Physically_Handicapped", 'Keralite', "Sub_Category", "Department", "Course_of_study",
                  "Course_completion_date", "Admission_date", "CAT_Rank", "Prime_Ministers_program", "Photo_upload", "Date_of_birth" , 'Pincode']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.fields["Sub_Category"].widget.attrs["required"] = False
        self.fields["Sub_Category"].widget.attrs["disabled"] = True
        self.fields["Prime_Ministers_program"].label = "Prime Ministers Education Program"
        self.fields["Physically_Handicapped"].label = "Differently Abled"
        self.helper.form_class = 'login100-form validate-form'
        self.helper.form_id = 'application_form'
        self.helper.form_action = '/apply/submitted/'
        self.helper.layout = Layout(
            CustomTextInput('Registration_No', label=' Exam Registration No'),
            CustomTextInput('Name', label='Name as in University records'),
            CustomTextInput('Date_of_birth', template='Application/CustomFields/CustomDate.html',
                            wrapper_class="wrap-input100 validate-input m-b-18", placeholder="Birth",
                            type_id='date'),
            CustomTextInput('Address_For_Communication', template='Application/CustomFields//CustomTextArea.html'),
            CustomTextInput('Permanent_Address', template='Application/CustomFields/CustomTextArea.html'),
            CustomTextInput('distance', label='Distance between permanent residence and university',
                            css_class='wrap-input100 validate-input m-b-18 validating'),
            Div(Div(
                CustomTextInput('Pincode', label='Pincode', css_class='wrap-input100 validate-input m-b-18 validating', css_id='pin'),
               css_class="col-sm-4"),
                Div(css_class='col-sm-3'),
                Div(CustomTextInput('State', template='Application/CustomFields//CustomSelect.html',
                                    onchange="load_district()", id="state"), css_class="col-sm-5 m-t-11"),
                css_class='form-row'),
            CustomTextInput('District', template='Application/CustomFields/CustomSelect.html', id='district'),
            CustomTextInput('Mobile_Number', css_id='mobile'),
            CustomTextInput('Name_of_Guardian', label='Name of Parent/Guardian'),
            CustomTextInput('PhoneNumber_of_Guardian', label='Phone Number of Parent/Guardian'),
            CustomTextInput('Year_of_Study', template='Application/CustomFields/CustomSelect.html', id='Year',
                            css_class='validating'),
            Div(
                Div(
                    CustomTextInput('Gender', template='Application/CustomFields/CustomSelect.html', id='Gender'),
                    css_class='col-sm-4'),
                Div(css_class='col-sm-4'),
                Div(CustomTextInput('Category', template='Application/CustomFields/CustomSelect.html', id='Category',
                                    onchange='load_subcategory()'),
                    css_class='col-sm-4'),
                css_class='form-row w-100',

            ),
            CustomTextInput('Sub_Category', template='Application/CustomFields/CustomSelect.html',
                            id='subcategory'),
            Div(CustomTextInput('Physically_Handicapped', template='Application/CustomFields/CustomBool.html', label="Differently Abled",
                                wrapper_class='wrap-input100 -line validate-input m-b-18', css_class='validating'),
                Div(css_class='col-sm-4'),
                CustomTextInput('Keralite', template='Application/CustomFields/CustomBool.html',
                                wrapper_class='wrap-input100 -line validate-input m-b-18', css_class='validating'),
                css_class='form-row w-100'),

            CustomTextInput('Department', template='Application/CustomFields/CustomSelect.html',
                            id='dept', wrapper_class="wrap-input100 validate-input m-b-26 m-t-26",
                            onchange='load_course1()'),
            CustomTextInput('Course_of_study', template='Application/CustomFields/CustomSelect.html', id='course'),
            Div(
                CustomTextInput('Admission_date', template='Application/CustomFields/CustomDate.html',
                                wrapper_class="wrap-input100 validate-input m-b-18", placeholder="Admission",
                                type_id='date'),
                CustomTextInput('Course_completion_date', template='Application/CustomFields/CustomDate.html',
                                wrapper_class="wrap-input100 validate-input m-b-18", placeholder="Course Completion",
                                type_id='date'),
                css_class='form-row w-100',
            ),
            Div(
                Div(CustomTextInput('CAT_Rank', css_class='wrap-input100 validate-input m-b-18 validating',
                                    css_id='CAT_rank', label='CAT RANK (optional)'),
                    css_class="col-sm-3",
                    ),
                Div(css_class='col-sm-5'),
                CustomTextInput('Prime_Ministers_program', template='Application/CustomFields/CustomBool.html'),
                css_class="form-row w-100"),

            CustomTextInput('Photo_upload', type_id='file', css_id="fileInput", label='Profile Photo (passport size)'),
            Div(template="Application/CustomFields/CustomDeclaration.html"),
            Div(
                Submit('Submit', 'Submit', css_class="login100-form-btn w-25", onclick="new_function(event)"),
                css_class="container-login100-form-btn"

            )

        )

    def clean(self):
        cleaned_data = super().clean()
        try:
            mobile = cleaned_data["Mobile_Number"]
            reg = re.compile(r"^\d{3}\d{3}\d{4}$")
            if not reg.match(str(mobile)):
                self.add_error('Mobile_Number', "mobile number is not valid")

        except KeyError:
            self.add_error('Mobile_Number', "mobile number is not valid")

        try:
            pin = cleaned_data["Pincode"]
            pin_reg = re.compile(r"^\d{6}$")
            if not pin_reg.match(str(pin)):
                self.add_error('Pincode', "Pincode is not valid")
        except KeyError:
            self.add_error('Pincode', "Pincode is not valid")

        exeception_list = ["Ph.D", 'M.Phil']

        # try:
        allow_application = ApplicationSettings.objects.get(pk=1)
        course = self.cleaned_data["Course_of_study"]
        year = self.cleaned_data["Year_of_Study"]
        if course in exeception_list:
            self.instance.verified_department = True
        if course not in exeception_list and not allow_application.active_applications:
            if year == 1 and allow_application.first_years:
                return cleaned_data

            self.add_error("Course_of_study", "The Time Frame for this Application is over")

        # except KeyError:
        #     self.add_error("Course_of_study", "please select a value")

        return cleaned_data
