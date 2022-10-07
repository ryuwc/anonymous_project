from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    release_date = forms.DateField(
        label='Release_date',
        widget=forms.DateInput(
            attrs={
                'class':'form-control',
                'placeholder':'연도-월-일',
                'type':'date'
            }
        )
    )
        
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':"form-control",
                'placeholder':'Title',
            }
    ))   

    audience = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class':"form-control",
                'placeholder':'Audience',
            }
    ))

    genre = forms.CharField(
        widget=forms.Select(
            attrs={
                'class':"form-select",
                
            },
            choices = (
                ('코미디', '코미디'),
                ('로맨스', '로맨스'),
                ('SF', 'SF'),
                ('액션', '액션')
            )
    ))

    score = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'class':"form-control",
                'placeholder':'Score',
                'min':0,
                'step':0.5,
                'max':5
            }
    ))          
    
    poster_url = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':"form-control",
                'placeholder':'Poster_url',
            }
    ))   

    description = forms.CharField(
        widget=forms.Textarea(
            
            attrs={
                'class':"form-control",
                'placeholder':'Description',
            }
    )) 


    class Meta:
        model = Movie
        fields = '__all__'
        
