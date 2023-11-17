from django.shortcuts import get_object_or_404, get_list_or_404



from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from .models import Article, Comment, Reply
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer, ReplySerializer
# from .forms import ReviewForm, CommentForm


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article(request):
    if request.method == 'GET':
        # movies = Movie.objects.all()
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True, partial=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(request.data)

            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # movie = Movie.objects.get(pk=movie_pk)
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        print(article)
        serializer = ArticleSerializer(article, context={'request': request})
        return Response(serializer.data)       
        
    elif request.method == 'DELETE':
        if article.user == request.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def comment_detail(request, article_pk=-1, comment_pk=-1):
    if request.method == 'GET':
        comments = get_list_or_404(Comment, user = request.user)
        return Response(serializer.data)

    if request.method == 'POST':
        article = get_object_or_404(Article, pk=article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.method == 'DELETE':
            # if Review.user == request.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'PUT':
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.like_users.add(request.user)
    article.save()
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.like_users.add(request.user)
    comment.save()
    serializer = CommentSerializer(comment)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_reply(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id)
    reply.like_users.add(request.user)
    reply.save()
    serializer = ReplySerializer(reply)
    return Response(serializer.data)