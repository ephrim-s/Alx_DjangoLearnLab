from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def admin_view(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(admin_view)
def admin_dashboard(request):
    return render(request, 'admin_view.html', {'user': request.user})
