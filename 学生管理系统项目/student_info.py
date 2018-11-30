# student_info.py



from student import Student

def input_student():
    L = []
    while True:
        a = input('输入姓名:')
        if a == '':
            break
        try:
            b = int(input('输入年龄:'))
            c = int(input('输入成绩:'))
        except:
            print('非法输入')
            continue
        L.append(Student(a,b,c))
    return L


def output_student(L):
    print('+---------------+----------+----------+')
    print('|     name      |   age    |   score  |')
    print('+---------------+----------+----------+')
    for i in L:
        i.show_info()
    print('+---------------+----------+----------+')
def del_remove(L):
    s = input('输入要删除的姓名信息:')
    for i in L:
        if i.name == s:
            L.remove(i)
    return L
def xiugai_student(L):
    a = input('请输入想修改的学生姓名:')
    for i in L:
        if i.name == a:
            i.name = input('输入新姓名:')
            try:
                i.age = int(input('输入新年龄:'))
            except:
                print('非法输入')
                i.age = int(input('请重新输入新年龄:'))
            try:
                i.score = int(input('输入新成绩:'))
            except:
                print('非法输入')
                i.score = int(input('请重新输入新成绩:'))
    return L

def score_low(L):
    L2 = sorted(L,key=lambda x:x.get_score(),reverse=True)
    output_student(L2)
def low_score(L):
    L3 = sorted(L,key=lambda x:x.get_score())
    output_student(L3)


def age_low(L):
    L4 = sorted(L,key = lambda x:x.get_age(),reverse=True)
    output_student(L4)
def low_age(L):
    L5 = sorted(L,key = lambda x:x.get_age())
    output_student(L5)

def baocun(L,si = 'si.txt'):
    try:
        fw = open(si,'w')
        for x in L:
              x.save(fw)
        print('保存成功')
        fw.close()
    except OSError:
        print('保存失败')

def duqu(si = 'si.txt'):
    try:
        L1 = []
        fr = open(si)
        for y in fr:
            y = y.rstrip()
            name,age,score = y.split(',')
            L1.append(Student(name,age,score))
        output_student(L1)
        fr.close()
        return L1
    except OSError:
        print('读取失败')






