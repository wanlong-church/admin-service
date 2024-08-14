from django.shortcuts import render
from django.http import HttpResponseNotFound

def handler404(request, exception):
    """
    Custom 404 error handler.
    
    Args:
        request: The request object that caused the 404 error.
        exception: The exception that was raised.
    
    Returns:
        HttpResponseNotFound: A rendered 404 error page.
    """
    context = {
        'error_message': 'The page you are looking for does not exist.',
        'error_code': 404,
    }
    return HttpResponseNotFound(render(request, '404.html', context))