def my_f(a,*args,**kwargs):
    print('a',a)
    print('args=',args)
    print('kwargs=',kwargs)
if __name__=='__main__':
   print('===case 1========')
   my_f(11)
   print('\n===case 2======')
   my_f(11,22,33)
   print()