from django import forms


class PatientsManagement(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Your firstname"
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Your lastname"
        }
    ))
    address = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Your adress"
        }
    ))
    phone_num = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            "class": "form-control",
            "placeholder": "Your number"
        }
    ))
    email = forms.EmailField(required=False, widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "placeholder": "Your Email"
        }
    ))

    CHOICES = (('Female', 'Female'), ('Male', 'Male'),)
    Gender= forms.ChoiceField(choices=CHOICES, widget=forms.Select(
        attrs={
            "class": "form-control",
            "placeholder": "Gender"
        }
    ))

