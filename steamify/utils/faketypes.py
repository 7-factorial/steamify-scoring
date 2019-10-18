import django


# django.db.models.fields.Field
class ModelField():
    name = "fakestring"
    verbose_name = "fakestring"

    def get_choices(self, include_blank=False):
        return ["fake", "list"]
    
    def formfield(self, **kwargs):
        # type: (...) -> django.forms.Field
        return django.forms.Field()

