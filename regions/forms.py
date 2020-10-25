from django import forms
from .models import Region

# Create your forms here.

class FormData(forms.Form):

    fans = forms.IntegerField(max_value=10000, min_value=1, label=False)
    personal = forms.IntegerField(max_value=10000, min_value=1, label=False)
    budget = forms.FloatField(max_value=10000000000, min_value=1000000, label=False)
    qualification = forms.IntegerField(max_value=10000, min_value=0, label=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-2'})
            self.fields[field].widget.attrs.update({'placeholder': f'Type the total {field}'})

class RegionForm(forms.ModelForm):

    class Meta:
        model = Region
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-2'})
            self.fields[field].widget.attrs.update({'placeholder': f'Type the {self.fields[field].label}'})
            self.fields[field].label = False
            