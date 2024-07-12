class Invitation:

    venu='venu:Bangaluru palaca'
    date='date on 09-05-2023'
    location='Location :bangaluru'

    @classmethod
    def invi(cls):
        print(cls.venu)
        print(cls.date)
        print(cls.location)
obj=Invitation()

for i in range(1, 100):
    n = input('enter the name to whom you want to invite :')
    print('________________'
          'dear ', n, 'i am glad to invite to my 22 year of my birthday celebration')
    obj.invi()
    print('from vani')