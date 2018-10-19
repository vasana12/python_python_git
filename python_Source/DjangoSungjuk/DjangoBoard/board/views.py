from django.shortcuts import render
from django.shortcuts import render_to_response
from django.utils import timezone
from .models import DjangoBoard
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from .pagingHelper import pagingHelper

# Create your views here.
rowsPerPage = 2

def home(request):
    boardList = DjangoBoard.objects.order_by('-hakbun')[0:2]
    current_page = 1
    totalCnt = DjangoBoard.objects.all().count()

    pagingHelperIns = pagingHelper();
    totalPageList = pagingHelperIns.getTotalPageList(totalCnt, rowsPerPage)
    print('totalPageList', totalPageList)
    print('current_page', current_page)

    return render_to_response('listPage.html',{'boardList': boardList,
                                                'totalCnt': totalCnt, 'current_page':current_page,
                                               'totalPageList': totalPageList})


#===============================================================================


def listPage(request):
    current_page = request.GET['current_page']
    totalCnt = DjangoBoard.objects.all().count()

    print('current_page=', current_page)

    if (int(current_page) !=0):
        start =(int(current_page) -1) * rowsPerPage #rowsPerPage #추출할 글의 시작위치
        end = int(current_page) * rowsPerPage # rowsPerPage #추출할 글의 끝위치
        boardList = DjangoBoard.objects.order_by("-hakbun")[start:end] #-id로 처리하면 내림차순, id 면 오름차순

        print('boardList=', boardList, 'count()=', totalCnt)

        #전체 페이지를 구해서 전달...
        pagingHelperIns = pagingHelper();

        totalPageList = pagingHelperIns.getTotalPageList(totalCnt,
                                                        rowsPerPage)

        print('totalPageList', totalPageList)

        return render_to_response('listPage.html', {'boardList':boardList,
                                                    'totalCnt':totalCnt, 'current_page':int(current_page),
                                                    'totalPageList':totalPageList})
    else:
        return render_to_response('listPage.html',
                                  {'current_page':int(current_page)})
#================================================================================

def writeForm(request):
    return render_to_response('writeBoard.html')

#================================================================================
@csrf_exempt
def writeBoard(request):
    br = DjangoBoard(hakbun=request.POST['hakbun'],
                     irum=request.POST['irum'],
                     kor=request.POST['kor'],
                     eng=request.POST['eng'],
                     math=request.POST['math'],
                     hits=0)
    br.save()

    #다시 조회
    url = '/listPage?current_page=1'
    return HttpResponseRedirect(url)

#=================================================================================

def viewBoard(request):
    hakbun = request.GET['hakbun']
    boardData = DjangoBoard.objects.get(hakbun=hakbun)

    #Update DataBase
    print('boardData.hits', boardData.hits)
    DjangoBoard.objects.filter(hakbun=hakbun).update(hits=boardData.hits +1)
    boardData.tot= boardData.kor + boardData.eng + boardData.math
    boardData.avg = boardData.tot / 3
    if boardData.avg >= 90:
        boardData.grade = "수"
    elif boardData.avg >= 80:
        boardData.grade = "우"
    elif boardData.avg >= 70:
        boardData.grade = "미"
    elif boardData.avg >= 60:
        boardData.grade = "양"
    else:
        boardData.grade = "가"

    DjangoBoard.objects.filter(hakbun=hakbun).update(
        hits= boardData.hits+1,
        tot=boardData.tot,
        avg=boardData.avg,
        grade=boardData.grade)

    return render_to_response('viewBoard.html',
                              {'boardData': boardData,
                               'current_page': request.GET['current_page']
                               })

#==========================================================================

def updateForm(request):
    hakbun = request.GET['hakbun']
    current_page = request.GET['current_page']

    #totalCnt = DjangoBoard.objects.all().count()
    print('hakbun', hakbun)
    boardData = DjangoBoard.objects.get(hakbun=hakbun)

    return render_to_response('updateForm.html',
                              {'boardData': boardData,
                               'hakbun': hakbun,
                               'current_page': current_page})
#=========================================================================
@csrf_exempt
def updateBoard(request):
    hakbun = request.POST['hakbun']
    current_page = request.POST["current_page"]

    print('### updateBoard ###')
    print('hakbun', hakbun)
    print('current_page', current_page)
    #Update DataBase
    DjangoBoard.objects.filter(hakbun=hakbun).update(
        irum=request.POST['irum'],
        kor=request.POST['kor'],
        eng=request.POST['eng'],
        math=request.POST['math']
        )
    #Display Page = > POST 요청은 redirection!
    url = '/listPage?current_page=' + str(current_page)
    return HttpResponseRedirect(url)
#=========================================================================

def deleteBoard(request):
    hakbun = request.GET['hakbun']
    current_page = request.GET['current_page']
    print('### DeleteSpecificRow #####')
    print('hakbun', hakbun)
    print('current_page', current_page)

    p = DjangoBoard.objects.get(hakbun=hakbun)
    p.delete()

    #Display Page
    # 마지막 메모를 삭제하는 경우 페이지를 하나 줄임.
    totalCnt = DjangoBoard.objects.all().count()
    pagingHelperIns = pagingHelper();

    totalPageList = pagingHelperIns.getTotalPageList(
        totalCnt, rowsPerPage)
    print('totalPages', totalPageList)

    if int(current_page) in totalPageList:
        print('current_page No change')
        current_page = current_page
    else:
        current_page = int(current_page)-1
        print('current_page--')

    url ='/listPage?current_page=' +str(current_page)
    return HttpResponseRedirect(url)
