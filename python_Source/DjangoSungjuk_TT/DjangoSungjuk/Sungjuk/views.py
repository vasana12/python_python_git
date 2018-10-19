from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import DjangoSungjuk
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from .pagingHelper import pagingHelper

# Create your views here.
rowsPerPage = 2
def home(request) :
    sungjukList = DjangoSungjuk.objects.order_by('hakbun')[0:2]
    current_page = 1
    totalCnt = DjangoSungjuk.objects.all().count()

    pagingHelperIns = pagingHelper();
    totalPageList = pagingHelperIns.getTotalPageList(totalCnt, rowsPerPage)
    print('totalPageList', totalPageList)

    return render_to_response('listSungjuk.html', {'sungjukList': sungjukList,
                                                   'totalCnt':totalCnt, 'current_page': current_page,
                                                   'totalPageList':totalPageList})
#===================================================================================
def writeFormSungjuk(request):
    return render_to_response('writeFormSungjuk.html')

#===================================================================================
@csrf_exempt
def writeSungjuk(request):
    tot = int(request.POST['kor']) + int(request.POST['eng']) + int(request.POST['math'])
    avg = int(tot/3 *100) /100
    if avg >= 90:
        grade = "수"
    elif avg >= 80:
        grade = "우"
    elif avg >= 70:
        grade = "미"
    elif avg >= 60:
        grade = "양"
    else:
        grade = "가"
    br = DjangoSungjuk(hakbun=request.POST['hakbun'],
                       irum=request.POST['irum'],
                       kor=request.POST['kor'],
                       eng=request.POST['eng'],
                       math=request.POST['math'],
                       tot=tot,
                       avg=avg,
                       grade=grade)
    br.save()

    #다시 조회
    url= '/listSungjuk?current_page=1'
    return HttpResponseRedirect(url)
#==============================================================================
def viewSungjuk(request):
    hakbun = request.GET['hakbun']
    #print 'pk=' + pk
    sungjukData = DjangoSungjuk.objects.get(hakbun=hakbun)
    #print boardData.memo

    return render_to_response('viewSungjuk.html',
                              {'hakbun': request.GET['hakbun'],
                               'current_page':request.GET['current_page'],
                               'sungjukData': sungjukData})
#==============================================================================
def listSungjuk(request):
    current_page = request.GET['current_page']
    totalCnt = DjangoSungjuk.objects.all().count()

    print('current_page=', current_page)

    if(int(current_page) != 0) :
        start = (int(current_page) - 1) * rowsPerPage # rowsPerPage # 추출할 글의 시작위치
        end = int(current_page) * rowsPerPage # rowsPerPage #추출할 글의 끝 위치
        sungjukList = DjangoSungjuk.objects.order_by("hakbun")[start:end] # -id 로 처리하면 내림차순, id 면 오름차순

        print('boardSungjuk=', sungjukList,'count()=', totalCnt)

        #전체 페이지를 구해서 전달...
        pagingHelperIns = pagingHelper();

        totalPageList = pagingHelperIns.getTotalPageList(totalCnt, rowsPerPage)
        print('totalPageList', totalPageList)

        return render_to_response("listSungjuk.html",{'sungjukList':sungjukList,
                                                      'totalCnt':totalCnt, 'current_page': int(current_page),
                                                      'totalPageList': totalPageList})
    else:
        return render_to_response('listSungjuk.html', {'current_page':int(current_page)})

#===================================================================

def updateFormSungjuk(request):
    hakbun = request.GET['hakbun']
    current_page = request.GET['current_page']


    #totalCnt = DjangoBoard.objects.all().count()
    print('hakbun', hakbun)
    print('current_page', current_page)

    sungjukData = DjangoSungjuk.objects.get(hakbun=hakbun)

    return render_to_response('updateFormSungjuk.html',
                              {'hakbun':request.GET['hakbun'],
                               'current_page':current_page,
                               'sungjukData':sungjukData})
#====================================================================

@csrf_exempt
def updateSungjuk(request):
    hakbun = request.POST['hakbun']
    current_page = request.POST['current_page']

    print('### updateSungjuk ###')
    print('hakbun', hakbun)
    print('current_page', current_page)

    #Update DataBase
    tot = int(request.POST['kor']) + int(request.POST['eng']) + int(request.POST['math'])
    avg = int(tot / 3 * 100) / 100
    if avg >= 90:
        grade = "수"
    elif avg >= 80:
        grade = "우"
    elif avg >= 70:
        grade = "미"
    elif avg >= 60:
        grade = "양"
    else:
        grade = "가"

    DjangoSungjuk.objects.filter(hakbun=hakbun).update(
        kor=request.POST['kor'],
        eng=request.POST['eng'],
        math=request.POST['math'],
        tot=tot,
        avg=avg,
        grade=grade)
    #Display Page => POST 요청은 redirection!
    url = '/listSungjuk?current_page=' + str(current_page)
    return HttpResponseRedirect(url)

#=========================================================
def deleteSungjuk(request):
    hakbun = request.GET['hakbun']
    current_page = request.GET['current_page']
    print('### DeleteSungjuk ###')
    print('hakbun', hakbun)
    print('current_page', current_page)

    p = DjangoSungjuk.objects.get(hakbun=hakbun)
    p.delete()

    # Display Page
    # 마지막 메모를 삭제하는 경우, 페이지를 하나 줄임.
    totalCnt = DjangoSungjuk.objects.all().count()
    pagingHelperIns = pagingHelper();

    totalPageList = pagingHelperIns.getTotalPageList(
        totalCnt, rowsPerPage)
    print('totalPages', totalPageList)

    if int(current_page) in totalPageList:
        print("current_page No Change")
        current_page = current_page
    else:
        current_page = int(current_page) -1
        print('current_page--')
    url = '/listSungjuk?current_page=' + str(current_page)
    return HttpResponseRedirect(url)

#=====================================================