__author__ = 'Xsank'


class Singleton(type):
    '''
    The singleton metaclass.
    '''
    def __init__(self,name,bases,dic):
        super(Singleton,self).__init__(name,bases,dic)
        self.instance=None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance=super(Singleton,self).__call__(*args,**kwargs)
        return self.instance

