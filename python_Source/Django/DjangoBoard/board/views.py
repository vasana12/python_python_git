from django.shortcuts import render

from django.shortcuts import render_to_response
from django.utils import timezone
from board.models import DjangoBoard
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from board.pagingHelper import pagingHelper

#=================================================================
rowsPerPage = 2
# Create your views here.

def home(request):
    boardList = DjangoBoard.objects.order_by('-id')[0:2]
    current_page = 1
    totalCnt = DjangoBoard.objects.all().count()

    pagingHelperIns = pagingHelper();
    totalPageList = pagingHelperIns.getTotalPageList(totalCnt, rowsPerPage)
    print('totalPageList', totalPageList)

    return render_to_response('listPage.html', {'boardList': boardList,
                                                'totalCnt': totalCnt, 'current_page': current_page,
                                                'totalPageList': totalPageList})

#================================================================================

def writeForm(request):
    return render_to_response('writeBoard.html')

#================================================================================
@csrf_exempt
def writeBoard(request):
    br = DjangoBoard(subject=request.POST['subject'],
                     name=request.POST['name'],
                     email=request.POST['email'],
                     memo=request.POST['memo'],
                     created_date=timezone.now(),
                     hits=0)
    br.save()

    #다시 조회
    url = '/listPage?current_page=1'
    return HttpResponseRedirect(url)


#=================================================================================

def listPage(request):
    current_page = request.GET['current_page']
    totalCnt = DjangoBoard.objects.all().count()

    print('current_page=', current_page)

    if (int(current_page) !=0):
        start =(int(current_page) -1) * rowsPerPage #rowsPerPage #추출할 글의 시작위치
        end = int(current_page) * rowsPerPage # rowsPerPage #추출할 글의 끝위치
        boardList = DjangoBoard.objects.order_by("-id")[start:end] #-id로 처리하면 내림차순, id 면 오름차순

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

#====================================================================

def viewBoard(request):
    pk = request.GET['memo_id']
    #print 'pk='+pk
    boardData = DjangoBoard.objects.get(id=pk)
    #print boardData.memo

    #Updata DataBase
    print('boardData.hits', boardData.hits)
    DjangoBoard.objects.filter(id=pk).update(hits=boardData.hits +1)

    return render_to_response('viewBoard.html',
                              {'memo_id': request.GET['memo_id'],
                               'current_page':request.GET['current_page'],
                               'searchStr':request.GET['searchStr'],'boardData':boardData})

#=====================================================================
def updateForm(request):
    memo_id = request.GET['memo_id']
    current_page = request.GET['current_page']
    searchStr = request.GET['searchStr']

    #totalCnt = DjangoBoard.objects.all().count()
    print('memo_id', memo_id)
    print('current_page', current_page)
    print('searchStr', searchStr)

    boardData = DjangoBoard.objects.get(id=memo_id)

    return render_to_response('updateForm.html',
                              {'memo_id': request.GET['memo_id'],
                               'current_page': request.GET['current_page'],
                               'searchStr':request.GET['searchStr'],
                               'boardData':boardData})


#=========================================================================
@csrf_exempt
def updateBoard(request):
    memo_id = request.POST['memo_id']
    current_page = request.POST["current_page"]
    searchStr = request.POST['searchStr']

    print('### updateBoard ###')
    print('memo_id', memo_id)
    print('current_page', current_page)
    print('searchStr', searchStr)

    #Update DataBase
    DjangoBoard.objects.filter(id=memo_id).update(
        email=request.POST['email'],
        subject=request.POST['subject'],
        memo=request.POST['memo'])
    #Display Page = > POST 요청은 redirection!
    url = '/listPage?current_page=' + str(current_page)
    return HttpResponseRedirect(url)
#=========================================================================

def deleteBoard(request):
    memo_id = request.GET['memo_id']
    current_page = request.GET['current_page']
    print('### DeleteSpecificRow #####')
    print('memo_id', memo_id)
    print('current_page', current_page)

    p = DjangoBoard.objects.get(id=memo_id)
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

#=================================================================
def listSearchPage(request):
    searchStr = request.GET['searchStr']
    pageForView = request.GET['pageForView'] #pageView 는 검색된 페이지 리스트에서 현재 페이지.
    print('listSearchPage:searchStr', searchStr, 'pageForView=', pageForView)

    totalCnt = DjangoBoard.objects.filter(subject__contains=searchStr).count()
    print('totalCnt=', totalCnt)

    pagingHelperIns = pagingHelper();
    totalPageList = pagingHelperIns.getTotalPageList(totalCnt, rowsPerPage)

    start = (int(pageForView)-1) * rowsPerPage # rowsPerPage # 추출한 글의 시작위치
    end = int(pageForView) * rowsPerPage # rowsPerPage # 추출한 글의 마지막 위치
    boardList = DjangoBoard.objects.filter(subject__contains=searchStr).order_by('-id')[start:end]

    print('boardList=', boardList)

    return render_to_response('listSearchPage.html',
                              {'boardList':boardList, 'totalCnt': totalCnt,
                               'pageForView': int(pageForView),
                               'searchStr': searchStr, 'totalPageList': totalPageList})
#======================================================================
@csrf_exempt
def searchSubject(request):
    searchStr = request.POST['searchStr']
    print('searchStr', searchStr)

    url = '/listSearchPage?searchStr=' + searchStr + '&pageForView=1'
    return HttpResponseRedirect(url)