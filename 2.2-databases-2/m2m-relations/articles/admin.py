from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope

class ScopeInlineFormSet(BaseInlineFormSet):
    def clean(self):
        is_main_count = 0
        for form in self.forms:
            if form.cleaned_data['DELETE']:
                continue
            if form.cleaned_data['is_main']:
                is_main_count += 1
        if is_main_count > 1:
            raise ValidationError('Главный должен быть один')
        if is_main_count < 1:
            raise ValidationError('Должен быть один главный тег')

        return super().clean()
    pass
class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 0
    formset = ScopeInlineFormSet


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title','prew','published_at','image']
    inlines = [ScopeInline]


    @admin.display(description='текст',ordering='text')
    def prew(self, obj: Article) -> str:
        return obj.text[:50]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']



@admin.register(Scope)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag','article', 'is_main']