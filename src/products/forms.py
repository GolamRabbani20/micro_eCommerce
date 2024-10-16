from django import forms
from django.forms import modelformset_factory, inlineformset_factory
from .models import Product, ProductAttachment

input_css_class = 'form-control'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'handle', 'description', 'price', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['placeholder'] = 'Product name'
        # self.fields['handle'].widget.attrs['placeholder'] = 'Handle'
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = input_css_class
        
class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name', 'handle', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['placeholder'] = 'Product name'
        # self.fields['handle'].widget.attrs['placeholder'] = 'Handle'
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = input_css_class

class ProductAttachmentForm(forms.ModelForm):
    class Meta:
        model = ProductAttachment
        fields=['file', 'name', 'is_free', 'active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['placeholder'] = 'Product name'
        # self.fields['handle'].widget.attrs['placeholder'] = 'Handle'
        
        for field in self.fields:
            if field in ['is_free', 'active']:
                continue
            self.fields[field].widget.attrs['class'] = input_css_class
            
ProductAttachmentModelFormset = modelformset_factory(
    ProductAttachment,
    form = ProductAttachmentForm,
    fields=['file', 'name', 'is_free', 'active'],
    extra=0,
    can_delete=True
)
ProductAttachmentInlinelFormset = inlineformset_factory(
    Product,
    ProductAttachment,
    form = ProductAttachmentForm,
    formset=ProductAttachmentModelFormset,
    fields=['file', 'name', 'is_free', 'active'],
    extra=0,
    can_delete=True
)