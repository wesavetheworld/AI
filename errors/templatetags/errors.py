from django import template
from errors.models import ErrorSet, Error, ErrorStatus


register = template.Library()

@register.inclusion_tag('errors/errorset.html', takes_context=True)
def render_errorset_block(context, errorset):
    context.update({'errorset': errorset})
    return context

@register.inclusion_tag('errors/error_block.html', takes_context=True)
def render_error_block(context, error):
    context.update({'error': error})
    return context
    
@register.inclusion_tag('errors/comment_block_wrapper.html', takes_context=True)
def render_comment_block(context, error):
    context.update({'error': error})
    return context

#@register.tag
#def render_latest_errors(context, article):
#    latest_errorset = ErrorSet.objects.filter(article=article).latest('created')
#    return render_errorset_block(context, latest_errorset)
