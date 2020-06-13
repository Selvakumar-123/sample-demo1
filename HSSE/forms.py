from django import forms
from .models import BiCycle_Registration


# DataFlair #File_Upload
class BiCycle_Form(forms.ModelForm):
    class Meta:
        model = BiCycle_Registration
        fields = '__all__'
