from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path_info in ["/login/", "/image/code/"]:
            return
        info_dice = request.session.get("info")
        if info_dice:
            return
        return redirect("/login/")
