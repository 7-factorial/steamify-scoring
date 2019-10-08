from django.forms.models import model_to_dict



def score_instance_to_dict(instance):
    """model_to_dict with appropriate fields excluded."""
    return model_to_dict(instance, exclude=["id", "shared_ptr", "judge"])

