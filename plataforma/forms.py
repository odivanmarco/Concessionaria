from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Veiculo

class VeiculoForm(forms.ModelForm):
    class Meta:
            model = Veiculo
            fields = "__all__"

