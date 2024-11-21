from django.forms.models import ModelForm
from dictApp.models import Word

class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = '__all__'