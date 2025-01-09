from lib2to3.fixes.fix_input import context

from django.shortcuts import render

# Create your views here.

def platform_view(request):
    return render(request,'third_task/platform.html')

def games_view(request):
    game_1 = 'Atomic Heart'
    game_2 = 'Cyberpunk'
    game_3 = 'PayDay'
    context = {
        'game_1': game_1,
        'game_2': game_2,
        'game_3': game_3
    }
    return render(request,'third_task/games.html', context)

def cart_view(request):
    return render(request,'third_task/cart.html')