# # middleware.py

# from django.utils import timezone
# from django.contrib.auth import logout

# class AutoLogoutMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#     def __call__(self, request):
#         response = self.get_response(request)

#         # Check if user is authenticated
#         if request.user.is_authenticated:
#             last_activity = request.session.get('last_activity')
#             now = timezone.now()

#             # If last activity time exists and it's been more than 1 hour, log out
#             if last_activity and (now - last_activity > timezone.timedelta(hours=1)):
#                 logout(request)

#             # Update last activity time in session
#             request.session['last_activity'] = now

#         return response
