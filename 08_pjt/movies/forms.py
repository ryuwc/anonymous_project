from django import forms
from movies.models import Movie

# Create your forms here.

class MovieForm(forms.ModelForm):
    
    class Meta:
        model = Movie
        fields = '__all__'
        

