from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def admin_view(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@login_required
@user_passes_test(admin_view)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

