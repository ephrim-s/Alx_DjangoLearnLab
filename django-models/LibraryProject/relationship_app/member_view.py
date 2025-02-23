from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def membe_viewr(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(Member)
def member_dashboard(request):
    return render(request, 'member_view.html', {'user': request.user})


