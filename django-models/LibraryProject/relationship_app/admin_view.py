from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def Admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# @login_required
@user_passes_test(Admin)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

