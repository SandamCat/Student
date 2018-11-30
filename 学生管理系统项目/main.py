# main.py  #主模块


from student_info import *
from menu import show_menu
def main():
    # L = []
    while True:
        show_menu()
        s = input("请选择: ")
        if s == 'q':
            break
        elif s == '1':
            L = input_student()
            # print(L)
        elif s == '2':
            output_student(L)
        elif s == '3':
            del_remove(L)
        elif s == '4':
            xiugai_student(L)
            # print(L)
        elif s == '5':
            score_low(L)
        elif s == '6':
            low_score(L)
        elif s == '7':
            age_low(L)
        elif s == '8':
            low_age(L)
        elif s == '9':
            baocun(L,si = 'si.txt')
        elif s == '10':
            L = duqu(si = 'si.txt')
if __name__ == '__main__':     
    main()
