class Test():
    def __init__(self, list1):
        self.list1 = []
        self.list2 = list1

    def print_list1(self):
        for i in self.list1:
            print('_', i)

    def print_list2(self):
        for i in self.list2:
            print('_', i)

    def append_list(self, l):
        for i in l:
            self.list1.append(i)


my_list = Test(['Ganesh', 'Kalidas', 'Manoj'])
my_list.print_list1()

my_list_1 = ['This', 'is', 'fake', 'list']
my_list.append_list(my_list_1)
my_list.print_list1()
my_list.print_list2()
