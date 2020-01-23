from rest_framework.generics import ListCreateAPIView

from .models import Lesson
from .serializers import LessonSerializer


class ListLesson(ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
