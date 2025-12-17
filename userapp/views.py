from django.http import JsonResponse
from django.views import View

from utils.decorators import handle_exception
from utils.validations import validate_empty_string

from .db_query import get_user_by_username


class UserView(View):
    @handle_exception
    def get(self, request):
        username = request.GET.get('username', '')
        validate_empty_string(username, 'username')

        user = get_user_by_username(username)

        return JsonResponse(user.to_json())
