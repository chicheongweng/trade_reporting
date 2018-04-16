from modeltranslation.translator import translator, TranslationOptions
from operation_centers.models import OperationCenter

class OperationCenterTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(OperationCenter, OperationCenterTranslationOptions)