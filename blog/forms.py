from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from .models import Blogs


class BlogsForm(forms.ModelForm):

    class Meta:
        model = Blogs
        fields = ("title", "body", "time_read","tags","slug")

        labels = {
            'title':'titulo',
            'body':'texto',
            'time_read':'tiempo de lectura'
        }
        widgets = {
            "body": CKEditor5Widget(config_name="extends"),
            "time_read":forms.NumberInput(attrs={'min': '0'}),

        }