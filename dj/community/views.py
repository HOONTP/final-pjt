from django.shortcuts import get_object_or_404, get_list_or_404



from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from .models import Article, Comment, Reply, Board
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer, ReplySerializer
# from .forms import ReviewForm, CommentForm


@api_view(['GET', 'POST'])
@authentication_classes([])
def article(request, community_pk=0, user_pk=0):
    if request.method == 'GET':
        if user_pk == 0:
            # movies = Movie.objects.all()
            articles = get_list_or_404(Article, board=community_pk)
        else:
            articles = get_list_or_404(Article, user=user_pk)
        serializer = ArticleListSerializer(articles, many=True, partial=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(request.data)
            board = get_object_or_404(Board, pk=community_pk)
            # serializer.save()
            serializer.save(user=request.user, board=board)
            return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([])
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
def comment_detail(request, article_pk, comment_pk=0):
    if request.method == 'GET':
        comments = get_list_or_404(Comment, user=request.user)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'POST':
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

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def reply_detail(request, comment_pk, reply_pk=0):
    if request.method == 'GET':
        replys = get_list_or_404(Reply, user=request.user)
        serializer = ReplySerializer(replys, many=True)
        return Response(serializer.data)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'POST':
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(comment=comment, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        reply = get_object_or_404(Reply, pk=reply_pk)
        if request.method == 'DELETE':
            # if Review.user == request.user:
            reply.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'PUT':
            serializer = ReplySerializer(reply, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_article(request, article_pk):
    article = get_object_or_404(Article, id=article_pk)
    # 현재 사용자가 이미 좋아요를 했다면 제거, 그렇지 않다면 추가
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)

    article.save()
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_comment(request, comment_pk):
    comment = get_object_or_404(Comment, id=comment_pk)
    if request.user in comment.like_users.all():
        comment.like_users.remove(request.user)
    else:
        comment.like_users.add(request.user)
    comment.save()
    serializer = CommentSerializer(comment)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_reply(request, reply_pk):
    reply = get_object_or_404(Reply, id=reply_pk)

    if request.user in reply.like_users.all():
        reply.like_users.remove(request.user)
    else:
        reply.like_users.add(request.user)
    reply.save()
    serializer = ReplySerializer(reply)
    return Response(serializer.data)