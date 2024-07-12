class Shopping:
    print('______welcome to grocery big basket _____')
    s={ }
    i=1
    n=int(input('enter the total number of item in number '))
    z=0
    a=0
    c=' '
    e=0
    for i in range(1,n+1):
      while True:
        food=input('enter the name of item ')
        price = int(input('enter the price '))

        s[food]=price
        break
    print(s)

    for i in s:
        z+=s.get(i)
    print('your total amount is ',z)

    print('__________________')

    print('______to remove a iterm____')
    q = input('Say (yes/no) to remove any item ')
    if q=='yes':
      v = int(input('enter the no of item to remove in numbers '))

      for i in range(0,v):
        for i in s:
          if q=='yes':
            w=input('enter the iterm to remove ')
            s.pop(w)
            print(s)
            break
    l=s
    for i in l:
         a+=s.get(i)
    print('total amount after removing of item ',a)
    print('__________________')
    print('_______to add the item___')
    d=input('Say (yes/no) to add any item ')
    if d=='yes':
       h = int(input('enter the no of item to add in numbers '))
       for i in range(1,h+1):
        for i in s:
          if d=='yes':
            t= input('Add the iterm  ')
            m=int(input('Add its price'))
            s.setdefault(t,m)
            print(s)
            break
    g=s
    for i in g:
      e+=s.get(i)
    print('total amount after the addition of iterm ',e)

    print('_____for payment____')
    f=int(input('please enter the total amount '))
    if z==f or a==f or e==f :
        print('payment succesfull'
              ' do visit next time'
              ' thank you for visiting')
obj=Shopping()

