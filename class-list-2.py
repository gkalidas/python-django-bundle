# class with list example 2


class Test():
    def __init__(self, li):
        self.li = li

    def check_type(self):
        if isinstance(self.li, str):
            print(self.li, 'is a string.')
            s = (self.li).split()
            self.print_list(s)
        elif isinstance(self.li, list):
            print(self.li, 'is a list.')
            self.print_list(self.li)

    def print_list(self, l):
        for i in l:
            print('_', i)


test = Test('Hi this is python tuple')
test.check_type()
test1 = Test(['Hi this is python list'])
test1.check_type()
