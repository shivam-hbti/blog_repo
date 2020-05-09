class Node:
    def __init__(self,dataval = None):
        self.dataval = dataval
        self.nextval = None

class Head:
    def __init__(self):
        self.headval = None

    def print_list(self):
        print_val = self.headval
        while print_val is not None:
            print(print_val.dataval)
            print_val = print_val.nextval

    def remove_node(self,node):
        print_n = self.headval
        print_next = self.headval.nextval
        print_d = self.headval.dataval
        pre = None
        i=0

        while print_d != node.dataval:
            pre = print_next
            print_n = pre.nextval
            print_d = print_n.dataval
            # print(pre.dataval)
            # print(print_d)
        pre.nextval = print_n.nextval



h1 = Head()
h1.headval = Node('1')
h2 = Node('2')
h3 = Node('3')
h4 = Node('4')
h1.headval.nextval = h2
h2.nextval = h3
h3.nextval = h4
h1.remove_node(Node('4'))
h1.print_list()
