#coding:utf-8

#写一个四行四列的小网格绘制的程序。

def draw_grid(rows, columns):
    def do_four(f, arg):# f 调用print_it
        f(arg)
        f(arg)
        f(arg)
        f(arg)
    def print_it(string):
        print (string)
    def print_line():
        start_hline = "+ - - - - +"
        add_hline = " - - - - +"
        print (start_hline + add_hline * (columns-1)) #打印横线
    def print_row():
        start_row = "|         |"
        adj_col_row = "         |"
        do_four(print_it, (start_row + adj_col_row * (columns-1))) #竖线
        
    def init_grid():
        print_line()
        print_row()
        print_line()

    def add_grid():
        print_row()
        print_line()
        print_row()
        print_line()
        print_row()
        print_line()

    init_grid()
    add_grid()

draw_grid(4,4)
