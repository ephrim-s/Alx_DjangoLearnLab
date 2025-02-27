from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def member_view(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(member_view)
def member_dashboard(request):
    return render(request, 'relationship_app/member_view.html', {'user': request.user})


