from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

from .models import Article, ArticleHasTag, Tag


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        i = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                i += 1
        if i > 1:
            raise ValidationError('Основным может быть только один раздел')
        if i == 0:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class ArticleHasTagInline(admin.TabularInline):
    model = ArticleHasTag
    extra = 1
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (ArticleHasTagInline,)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # в админке заполняется только справочник тегов
    # связывание с таблицей статей не нужно:
    # inlines = (ArticleHasTagInline,)
    pass

