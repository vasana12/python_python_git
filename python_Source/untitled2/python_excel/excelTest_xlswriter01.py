#-*-coding: utf-8 -*-
#http://github.com/jmcnamara/XlsxWriter 사이트에서 압축파일 다운로드 후
#  압축 푼 다음
#엑셀문서로 출력하기 위한 용도 사용 (읽기 불가, load 안됨)
import xlsxwriter

workBook = xlsxwriter.Workbook("xlsxwriter1.xlsx")
ws = workBook.add_worksheet("테스트") #워크시트 추가

ws.write('A1','korea')
ws.write(3,3,"test")
ws.write(4,4,"test2")
ws.write('B1',10)
ws.write('B2',20)
ws.write('B3','=sum(B1:B2)')
ws.write('A2',"fighting")

workBook.close()