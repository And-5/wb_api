def check_relation(net, first: str, second: str):
    friend = list(net)
    ls = [first]
    count = 0
    while count <= 6:
        ls_2 = friend.copy()
        set_1 = set(ls)
        count += 1
        if count == 6 and second not in set_1:
            print(f'Связи между {first} и {second} нет')
            return True
        if count == 6 and second in set_1:
            print(f'Связь между {first} и {second} есть')
            return True
        else:
            for tupl in ls_2:
                for name in tupl:
                    for nam in set_1:
                        if nam == name:
                            for i in tupl:
                                if i not in ls:
                                    ls.extend(tupl)
                                    friend.pop(friend.index(tupl))
            for g in ls:
                if g == first:
                    ls.pop(ls.index(g))


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша"),
    )

    assert check_relation(net, "Петя", "Стёпа")
    assert check_relation(net, "Маша", "Петя")
    assert check_relation(net, "Ваня", "Дима")
    assert check_relation(net, "Лёша", "Настя")
    assert check_relation(net, "Стёпа", "Маша")
    assert check_relation(net, "Лена", "Маша")
    assert check_relation(net, "Вова", "Лена")
