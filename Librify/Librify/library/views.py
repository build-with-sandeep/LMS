from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignupForm
# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Librarian, Member, Book
from .serializers import LibrarianSerializer, MemberSerializer, BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

class LibrarianViewSet(viewsets.ModelViewSet):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]



class LibrarianListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        librarians = Librarian.objects.all()
        serializer = LibrarianSerializer(librarians, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LibrarianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class LibrarianDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, username):
        try:
            return Librarian.objects.get(username=username)
        except Librarian.DoesNotExist:
            raise Http404

    def get(self, request, username):
        librarian = self.get_object(username)
        serializer = LibrarianSerializer(librarian)
        return Response(serializer.data)

    def put(self, request, username):
        librarian = self.get_object(username)
        serializer = LibrarianSerializer(librarian, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, username):
        librarian = self.get_object(username)
        librarian.delete()
        return Response(status=204)

# Similarly, you can implement views for Member actions

class MemberListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class MemberDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, username):
        try:
            return Member.objects.get(username=username)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, username):
        member = self.get_object(username)
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    def put(self, request, username):
        member = self.get_object(username)
        serializer = MemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, username):
        member = self.get_object(username)
        member.delete()
        return Response(status=204)

class BookListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class BookDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, book_id):
        try:
            return Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, book_id):
        book = self.get_object(book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, book_id):
        book = self.get_object(book_id)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, book_id):
        book = self.get_object(book_id)
        book.delete()
        return Response(status=204)


from .models import Librarian, Member

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            role = form.cleaned_data['role']
            if(role=='librarian'):
                # Create a new librarian object
                librarian = Librarian(username=username, name=name, email=email, password=password)
                librarian.save()
            else :
                member = Member(username=username, name=name, email=email, password=password)
                member.save()

            # Redirect the user to the login page after successful signup
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'library/signup.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            role = form.cleaned_data['role']

            # Create a new user object
            user = User(username=username, name=name, email=email, role=role)
            user.set_password(password)
            user.save()

            # Redirect the user to the login page after successful signup
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'library/signup.html', {'form': form})


from .models import Librarian

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            # Create a new librarian object
            librarian = Librarian(username=username, name=name, email=email, password=password)
            librarian.save()

            # Redirect the user to the login page after successful signup
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'library/signup.html', {'form': form})


from .models import Member

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            # Create a new member object
            member = Member(username=username, name=name, email=email, password=password)
            member.save()

            # Redirect the user to the login page after successful signup
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'library/signup.html', {'form': form})




from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Login the user
                login(request, user)

                # Redirect the user based on their role
                if role == 'member':
                    return redirect('member_dashboard')
                elif role == 'librarian':
                    return redirect('librarian_dashboard')
            else:
                # Authentication failed, display an error message
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'library/login.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
# from .forms import MemberForm
#
# def member_edit(request, username):
#     member = get_object_or_404(Member, username=username)
#
#     if request.method == 'POST':
#         form = MemberForm(request.POST, instance=member)
#         if form.is_valid():
#             form.save()
#             return redirect('member_list')
#     else:
#         form = MemberForm(instance=member)
#
#     return render(request, 'library/member_edit.html', {'form': form, 'member': member})
#
#
# # views.py
#
# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Member
#
# def member_delete(request, username):
#     member = get_object_or_404(Member, username=username)
#
#     if request.method == 'POST':
#         member.delete()
#         return redirect('member_list')
#
#     return render(request, 'library/member_confirm_delete.html', {'member': member})
