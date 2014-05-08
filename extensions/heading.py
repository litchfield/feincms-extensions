from django.db import models
from feincms import extensions

def register(cls, unused):
    cls.add_to_class('heading',
        models.CharField(max_length=255, blank=True, 
            help_text='On-page heading if it varies from the page title above')
    )


class Extension(extensions.Extension):
    def handle_model(self):
        self.model.add_to_class(
            'heading',
            models.CharField(
                max_length=255,
                help_text='On-page heading if it varies from the page title above',
                blank=True)
        )

    def handle_modeladmin(self, modeladmin):
        modeladmin.add_extension_options('On-page heading', {
            'fields': ('heading',),
        })