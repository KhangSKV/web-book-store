from django.shortcuts import render
from .models import Book
from django.http import JsonResponse
from .utils import get_user_details

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'catalog/book_list.html', {'books': books})

def book_borrowed_by_user(request, user_id):
    user_details = get_user_details(user_id)
    if "error" in user_details:
        return JsonResponse({"error": "User not found"}, status=404)
    return JsonResponse({"message": f"User {user_details['username']} borrowed this book"})
