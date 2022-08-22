from csv import field_size_limit
from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUSerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username','password1',]


        # def __init__(self, *args, **kwargs):
        #     super(CustomUSerForm, self).__init__(*args, **kwargs)

        #     for name, field in self.fields.items():
        #         field.widget.attrs.update({'class': 'input'})

    def __init__(self, *args, **kwargs):
        super(CustomUSerForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})