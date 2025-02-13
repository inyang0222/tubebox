from django.shortcuts import render
from tubeboxApp.models import user,apis
from tubeboxApp.v3_api import youtube_v3
from django.http import JsonResponse

def main(request):
    return render(request, 'main.html')
def search_video(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword', '')
        list = youtube_v3(keyword)
        response_data = {"result": list['items']}
        return JsonResponse(response_data)

def process_data(request):
    if request.method == 'POST':
        data = request.POST.get('user_input', '')  # HTML 폼에서 받은 데이터
        data += "123"
        response_data = {"message": f"입력한 값: {data}"}
        return JsonResponse(response_data)  # JSON 응답 반환
    
def login(request):
    response_data = {}

    if request.method == "GET" :
        return render(request, 'login.html')

    elif request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if not (username and password):

            response_data['error']='아이디와 비밀번호를 모두 입력해주세요.'
            return render(request, 'login.html',response_data)
        try:
            myuser = user.objects.get(username=username)
            #if check_password(password,myuser.password):
            #    request.session['user'] = myuser.id
            #    return redirect('')
            #else:
            #    return render(request, 'login.html',{'error': '잘못된 비밀번호입니다.'})
        except:
            return render(request, 'login.html',{'error': '존재하지 않는 회원입니다.'})
    else :
        return render(request, 'login.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        insert_data("user2","123123123")
        return render(request, 'register.html')
    '''elif request.method == 'POST':
        username = request.POST.get('username',None)
        useremail = request.POST.get('useremail',None)
        password = request.POST.get('password',None)
        repasswd = request.POST.get('repasswd',None)

        res_data = {}
        if not (username and useremail and password and repasswd):
            res_data['error'] = '모든 값을 입력해야 합니다.'
        elif password != repasswd:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            user = User(
                username = username,
                useremail = useremail,
                password = make_password(password)
            )
            user.save()
            return redirect('')
        return render(request, 'register.html',res_data)
    '''

def youtube(request):
    #owner_obj = user.objects.get(pk=pk)
    #api_objs = apis.objects.filter(owner_id=owner_obj.user_id)
    #context = {
    #        "api_key": api_objs,
    #        "user" : owner_obj
    #        }
    item_list = youtube_v3("test")
    context = {
            "items": item_list["items"]
            }
    return render(request, 'api.html', context)

def insert_data(user_name,password):
    user_instance = user.objects.create(name=user_name,pw=password)
