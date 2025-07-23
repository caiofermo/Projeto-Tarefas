from django import forms
from .models import TarefasModel

class TarefaForm(forms.ModelForm):
    class Meta:
        model = TarefasModel
        fields = ['nome', 'descricao', 'concluido']


 
