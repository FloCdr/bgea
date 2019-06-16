from django.forms import ModelForm
from .models import *

class EpreuveForm(ModelForm):
    class Meta:
        model = Epreuve
        fields = '__all__'
