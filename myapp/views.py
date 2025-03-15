from django.http import HttpResponse
from django.shortcuts import render
# from .models import Menu


# def home(request):
#     return HttpResponse("Welcome to Little Lemon!")
# def pathview(request,name,id):
#     return HttpResponse(f"Name:{name} UserId:{id}")
# def pathview(request):
#     name=request.GET['name']
#     id=request.GET['id']
#     return HttpResponse(f"Name:{name} UserId:{id}")
# def showform(request):
#     return render(request,'form.html')
# def getform(request): 
#     if request.method == "POST":  # Check if form was submitted
#         id = request.POST['id']   # Get the 'id' input value
#         name = request.POST['name']  # Get the 'name' input value
#     return HttpResponse(f"Name: {name}, UserID: {id}")  # Show data in response


# def drinks(request, drink_name):
   
#     drink = {
#         'mocha': 'type of coffee',
#         'tea': 'type of beverage',
#         'lemonade': 'type of refreshment',
#     }

#     choice_of_drink = drink.get(drink_name, "This drink is not available.")
    
#     return HttpResponse(f"<h2>{drink_name.capitalize()}</h2><p>{choice_of_drink}</p>")



# def home(request):
#     return HttpResponse("Welcome to Little Lemon!")

# def menu(request):
#     return HttpResponse("Menu")

# def about(request):
#     return HttpResponse("About Us")

# def book(request):
#     return HttpResponse("Make a Booking!!")

# def about(request):
#     content={'About':"Based in Chicago, Atlanta, Little Lemon is a family owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12-15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices,making it a popular place for a meal any time of the day."}
#     return render(request,"about.html",content)





# Create your views here for menu.
# def about(request):
#     about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."} 
#     return render(request, "about.html", {'content': about_content})

# def menu(request):
#     about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."} 
#     return render(request, "menu.html", {'content': about_content})

# def menu_card(request):
#     new_menu=Menu.objects.all()
#     new_menu_dict={'menu':new_menu}
#     return render(request,'menu_card.html',new_menu_dict)

# def about(request):
#     return render(request, "about.html")
# def menu(request):
#     return render(request, "menu.html")




# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def book(request):
    return render(request, 'book.html')