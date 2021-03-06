from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'issues.views',
    url(
        r'^comments/(?P<id>\d+)$',
        'comment_list',
        name='render_issue_comment_list'),
    url(
        r'^commentblock/(?P<pk>\d+)$',
        'comment_block',
        name='render_issue_comment_block'
    ),
    url(
        r'^issueblock/(?P<pk>\d+)$',
        'issue_block',
        name='render_issue_block'),
    url(
        r'^post_issue/$',
        'post_issue',
        name='post_issue_ajax'),
    url(
        r'^issue_status/$',
        'toggle_issue_status',
        name='toggle_issue_status'),
    url(
        '^issue_comment_count/(?P<pk>\d+)$',
        'get_issue_comment_count',
        name='issue_comment_count'),
)
