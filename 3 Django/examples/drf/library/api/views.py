from rest_framework import generics
from books.models import Book
from .serializers import BookSerializer
from django.utils import timezone


class BookAPIView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        # maybe you need more lines of code here
        return Book.objects.all()


class CreateBook(generics.CreateAPIView):
    serializer_class = BookSerializer


# this replaces all three of the views below
class BookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class BookDetailView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class BookUpdateView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class BookDeleteView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookCheckOutView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_update(self, serializer):
        book = Book.objects.get(pk=self.kwargs['pk'])
        if book.is_checked_out():
            serializer.save(check_in_date=timezone.now())
        else:
            serializer.save(check_out_date=timezone.now(),
                            times_checked_out=book.times_checked_out + 1)
