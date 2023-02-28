from django import forms

class SliderForm(forms.Form):
    value = forms.IntegerField(min_value=1, max_value=10, label='How stressed are you, from 1-10? (10 being incredibly stressed)')