from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def Admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(Admin)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html', {'user': request.user})