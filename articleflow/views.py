from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from articleflow.models import Article, ArticleState, State, Transition
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.template import RequestContext
from django.contrib.auth.models import User


class ArticleGrid(ListView):

    template_name = 'articleflow/grid.html'

    def get_queryset(self):
        return Article.objects.all().select_related('journal__name', 'articlestate__state__name')

class ArticleDetailTransition(View):

    template_name = 'articleflow/possible_transitions.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(kwargs)
        return render_to_response(self.template_name, context, context_instance=RequestContext(request))

    def get_context_data(self, kwargs):
        article = Article.objects.get(doi=kwargs['doi'])
        transitions = article.possible_transitions().select_related()
        context = ({
                'article': article,
                'transitions': transitions,
            })
        return context

    def post(self, request, *args, **kwargs):
        article = Article.objects.get(pk=request.POST['article'])
        transition = Transition.objects.get(pk=request.POST['transition'])
        # @TODO, fix this shit!
        user = User.objects.get(pk=1)
        
        print user
        print article
        print transition

        article.execute_transition(transition, user)
        
        context = self.get_context_data(kwargs)
        return render_to_response(self.template_name, context, context_instance=RequestContext(request))
        




