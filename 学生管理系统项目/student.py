class Student:
    def __init__(self,name,age,score = 0):
        self.__name = name
        self.__age = age
        self.__score = score
    def show_info(self):
          chinese_cnt = get_chinese_char_count(self.__name)
          print('|%s|%s|%s|' % (self.__name.center(15-chinese_cnt),
                         str(self.__age).center(10),
                         str(self.__score).center(10)
                         )
          )
    def get_score(self):
        return self.__score
    def get_age(self):
        return self.__age
    def save(self,file):
        file.write(self.__name)
        file.write(',')
        file.write(str(self.__age))
        file.write(',')
        file.write(str(self.__score))
        file.write('\n')


def get_chinese_char_count(x):
    count = 0  # 先假设个数为0
    for ch in x:
        # 如果ch为中文字典,则count 做加一操作
        if ord(ch) > 127:
            count += 1
    return count