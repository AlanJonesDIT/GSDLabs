#Import HttpResponse since that is what we want to do
from django.http import HttpResponse

#import our Board model
from .models import Board 
 
#define a method home which will get a list of board names from our database
#and iterate to them appending them to a simple html response which we return
#when this method is called
def home(request):
    boards = Board.objects.all()
    boards_names = list() 
 
    for board in boards:
        boards_names.append(board.name) 
 
    response_html = '<br>'.join(boards_names) 
 
    return HttpResponse(response_html) 
