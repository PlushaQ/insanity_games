from django import forms
from .models import Opinion


class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ['topic', 'rating', 'message']
        widgets = {
            'topic': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.Select(choices=Opinion.RATING_CHOICES, attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        time = kwargs.pop('time', None)
        super().__init__(*args, **kwargs)
        if user:
            self.instance.user_id = user.id
        self.instance.time = time
