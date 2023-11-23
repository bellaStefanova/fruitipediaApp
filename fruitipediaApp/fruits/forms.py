from django import forms
from fruitipediaApp.fruits.models import Fruit, Category

class CategoryBaseForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class CategoryCreateForm(CategoryBaseForm):
    pass

class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields='__all__'

class FruitCreateForm(FruitBaseForm):
    category=forms.ModelChoiceField(queryset=Category.objects.all())

class FruitEditForm(FruitBaseForm):
    category=forms.ModelChoiceField(queryset=Category.objects.all())

class FruitDeleteForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields=('name', 'Image_url', 'description')