from django.shortcuts import redirect,render
class check_session :
    def __init__(self,get_response):
         self.get_response = get_response
    def __call__(self,request):
        if  request.session.get('user_id') :
            return redirect('dashboard:home')
        else :
            return self.get_response(request)
        