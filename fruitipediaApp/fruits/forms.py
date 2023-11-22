from django import forms
from fruitipediaApp.fruits.models import Fruit, Category

class CategoryBaseForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class CategoryCreateForm(CategoryBaseForm):
    pass