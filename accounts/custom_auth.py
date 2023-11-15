from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from .models import regs
        
class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, user_name=None, password=None, **kwargs):
        try:
            user = regs.objects.get(user_name=user_name)
            if check_password(password, user.password):
                return user
        except regs.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return regs.objects.get(pk=user_id)
        except regs.DoesNotExist:
            return None