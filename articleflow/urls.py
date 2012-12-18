from django.conf.urls import patterns, include, url
from articleflow.views import ArticleGrid, ArticleDetailMain, ArticleDetailTransition, ArticleDetailIssues
from errors.views import Errors

urlpatterns = patterns('articleflow.views',
                       url(r'^grid/$', ArticleGrid.as_view(), name='grid'),
                       url(r'^detail/(?P<doi>[a-z|\.|0-9]{0,50})/$', ArticleDetailMain.as_view(), name='detail_main'),
                       url(r'^detail/(?P<doi>[a-z|\.|0-9]{0,50})/transitions', ArticleDetailTransition.as_view(), name='detail_transition'),
                       url(r'^detail/(?P<doi>[a-z|\.|0-9]{0,50})/issues', ArticleDetailIssues.as_view(), name='detail_issues'),
                       url(r'^detail/(?P<doi>[a-z|\.|0-9]{0,50})/errors', Errors.as_view(), name='detail_errors'),
                       )

