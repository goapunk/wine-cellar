import json
from datetime import datetime

from django import forms
from django.core import validators
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import ImageField
from django.utils.translation import gettext as _

from wine_cellar.apps.wine.fields import OpenMultipleChoiceField
from wine_cellar.apps.wine.models import Categories, Grape


class WineForm(forms.Form):
    name = forms.CharField(max_length=100, help_text=_("Designation of the wine"))
    wine_type = forms.CharField(max_length=2, widget=forms.Select(choices=Categories))
    abv = forms.FloatField()
    capacity = forms.FloatField()
    vintage = forms.IntegerField(
        validators=[
            validators.MinValueValidator(1900),
            validators.MaxValueValidator(datetime.now().year),
        ],
    )
    grapes = OpenMultipleChoiceField(
        required=False, queryset=Grape.objects.all(), field_name="name"
    )
    classification = forms.CharField(
        required=False, max_length=100, help_text=_("Comma-separated list of grapes")
    )
    comment = forms.CharField(max_length=250, required=False, widget=forms.Textarea)
    rating = forms.IntegerField(
        required=False,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )
    image = ImageField(required=False)
    stock = forms.IntegerField(
        required=False,
        validators=[MinValueValidator(0)],
    )
    grapes.widget.attrs.update(
        {"data-tom_config": json.dumps({"create": True, "maxItems": None})}
    )


class WineFilterForm(forms.Form):
    template_name = "wine_filter_field.html"
