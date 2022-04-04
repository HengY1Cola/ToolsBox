class OnePerson(object):
    def __init__(self, name, grade :int):
        self.name = name
        self.grade = grade


def shellSort(list):
    length = len(list)
    gap = length // 2
    while gap >= 1:
        for i in range(length):
            j = i
            while j >= gap and list[j - gap].grade > list[j].grade:  # 在每一组里面进行直接插入排序
                list[j], list[j - gap] = list[j - gap], list[j]
                j -= gap
        gap = gap // 2  # 更新步长
    return list


if __name__ == '__main__':
    persons = []
    nameList = []
    gradeList = []
    flag = 0
    print('输入 q 0 退出')
    while flag != 'q':
        name, grade = list(map(str, input('请输入姓名与成绩：\n').strip().split()))
        flag = name
        person = OnePerson(name, int(grade))
        persons.append(person)
    print(persons)
    shellSort(persons)
    print(persons)
    for person in persons:
        gradeList.append(person.grade)
        nameList.append(person.name)
    print(f"名单为： {nameList}")
    print(f"成绩为： {gradeList}")


