from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def Librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

@user_passes_test(Librarian)
def librarian_dashboard(request):
    return render(request, 'librarian_dashboard.html', {'user': request.user})
