from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

from rest_framework import permissions

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from .permissions import EhSuperUser

"""
API V1
"""


# API de Cursos
class CursosAPIView(generics.ListCreateAPIView):  # Lista e cria cursos
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):  # Busca um curso, atualiza um curso e deleta um curso.
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


# API de Avaliação
class AvaliacoesAPIView(generics.ListCreateAPIView):  # Lista e cria avaliações
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    # Lista todas as avaliações de um determinado curso
    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()


class AvaliacaoAPIView(
    generics.RetrieveUpdateDestroyAPIView):  # Busca uma avaliação, atualiza uma avaliação e deleta uma avaliação
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    # Pega uma avaliação especifica de um determinado curso
    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get('curso_pk'),
                                     pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


"""
API V2
"""


class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = (
        EhSuperUser,
        permissions.DjangoModelPermissions,
    )
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    # Lista todas as avaliações de um determinado curso
    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        # configurando paginação das avaliações
        self.pagination_class.page_size = 1
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)


"""
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
"""


class AvaliacaoViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
