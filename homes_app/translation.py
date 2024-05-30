from modeltranslation.translator import register, TranslationOptions
from .models import Homes, Category

@register(Homes)
class HomesTranslationOptions(TranslationOptions):
    fields = ('title', 'manzil')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)