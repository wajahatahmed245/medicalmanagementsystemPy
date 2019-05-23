from django import forms


class PatientsManagement(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Your Username"
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Your Username"
        }
    ))
    address = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Your Username"
        }
    ))
    phone_num = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            "class": "form-control",
            "placeholder": "Your Username"
        }
    ))
    email = forms.EmailField(required=False, widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "placeholder": "Your Username"
        }
    ))
    symptoms = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Your Username"
        }
    ))
    medicine = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Your Username"
        }
    ))
