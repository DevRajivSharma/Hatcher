from django.shortcuts import redirect
class check_session :
    def __init__(self,get_response):
         self.get_response = get_response
    def __call__(self,request):
        if  request.session.get('user_id') :
            print('Inside MiddleWare')
            return redirect('dashboard:home')
        response = self.get_response(request)
        return response
        