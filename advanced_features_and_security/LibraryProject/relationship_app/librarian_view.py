from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def librarian_view(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

@user_passes_test(librarian_view)
def librarian_dashboard(request):
    return render(request, 'relationship_app/librarian_view.html', {'user': request.user})
