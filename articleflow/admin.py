from django.contrib import admin
from articleflow.models import *

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('current_state', 'current_articlestate', 'article_extras')
    fieldsets = [
        (None            , {'fields': ['doi', 'pubdate', 'journal', 'typesetter']}),
        ('State Info'    , {'fields': ['current_state', 'current_articlestate']}),
        ('File Info'     , {'fields': ['si_guid', 'md5']}),
        ('EM info'       , {'fields': ['em_pk', 'em_ms_number', 'em_max_revision']}),
        ('Record Info'   , {'fields': ['created']}),
        ]
    list_display = ('doi', 'journal', 'pubdate', 'typesetter', 'current_state', 'current_assignee')
    list_filter = ('pubdate', 'current_state', 'journal', 'typesetter')
    search_fields = ('doi', 'current_articlestate__assignee__username')
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'unique_name', 'progress_index')

class TransitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'unique_name', 'from_state', 'to_state')

class ArticleStateAdmin(admin.ModelAdmin):
    list_display = ('article', 'state', 'assignee', 'from_transition', 'from_transition_user', 'created', 'last_modified')
    list_filter = ('state', 'assignee', 'from_transition', 'from_transition_user')
    search_fields = ('article__doi', 'assignee__username')

admin.site.register(State, StateAdmin)
admin.site.register(ArticleState, ArticleStateAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Transition, TransitionAdmin)
admin.site.register(Journal)
admin.site.register(ArticleExtras)
admin.site.register(AssignmentHistory)
admin.site.register(AssignmentRatio)
admin.site.register(Typesetter)
admin.site.register(WatchState)

