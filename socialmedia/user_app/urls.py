from .views import *
from django.urls import path

urlpatterns = [
    # path('all-posts/', all_posts, name="allPosts"),
    # path('users-posts/<int:user_id>', users_posts, name="userPosts"),
    # path('post-detail/<int:post_id>', post_detail, name="postDetail"),
    # path('all-users/', all_users, name="allUsers"),
    # path('user-detail/<int:user_id>', user_detail, name="userDetail"),
    # path("comments/<int:post_id>", comment_display, name="postComments")
    # HW12 >>>
    path('', Home.as_view(), name="home"),
    path('display-posts/', DisplayPosts.as_view(), name="PostList"),
    path('postdetail/<int:pk>', PostDetail.as_view(), name='PostDetail'),
    path('new-post/', NewPost.as_view(), name='NewPost'),
    path('new-comment/<int:post_id>', new_comment, name='new_comment'),
    path('week-posts/', PostsOfWeekList.as_view(), name='WeekList'),
]
