class pass_err(Exception):
    def __init__(self,msg):
        self.msg = msg



try:
    a = str(input('enter the pass   '))
    n = len(a)
    print(n)
    if n >= 8 and a == 'asdfghjkl':
        print('-------------')
        print('pass accpted')
    else:
        raise pass_err('lenght error')

except pass_err:
    print('pass lenght error')



        