from django import forms
from basic.models import EmailForNews
from basic.models import Massage

class NameForm(forms.ModelForm):
    class Meta():
        model = EmailForNews
        fields = ('name', 'email')
        fields_order = ['name', 'email']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].label = "نام و نام خانوادگی"
        self.fields["email"].label = "آدرس ایمیل"

class MassageForm(forms.ModelForm):
    class Meta():
        model = Massage
        fields = ('first_name', 'last_name', 'email', 'number', 'massage')
        fields_order = ['first_name', 'last_name', 'email', 'number', 'massage']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].label = "نام"
        self.fields["last_name"].label = "نام خانوادگی"
        self.fields["email"].label = "آدرس ایمیل"
        self.fields["number"].label = "شماره تماس"
        self.fields["massage"].label = "پیام"
