from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def Member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(Member)
def member_dashboard(request):
    return render(request, 'member_dashboard.html', {'user': request.user})


