from django import forms
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    """
    A form for Reviews.
    """
    class Meta:
        model = Review
        fields = ('rating', 'user_review')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'user_review': 'Product Review Description',
        }
        self.fields['user_review'].widget.attrs['autofocus'] = True
        self.fields['rating'].label = 'Rate the product out of 5 Stars:'
        for field in self.fields:
            if field != 'rating':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            if field == 'rating':
                self.fields[field].choices = self.fields[field].choices[1:]
