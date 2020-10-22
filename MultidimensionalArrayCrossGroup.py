#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2020/10/21 09:07
# Author  : None
# Site    : 
# File    : MultidimensionalArrayCrossGroup.py


class MultidimensionalArrayCrossGroup():

    def calculation(self, arrayStr):
        columns = self._calculation(arrayStr)
        column = columns[0]
        groups = []

        for i in range(len(column)):
            group = [column[i]]
            group.extend([item[i % len(item)] for item in columns[1:]])
            groups.append(group)
        return groups

    def _calculation(self, arrayStr):
        l = 1
        tmp = []
        for item in reversed(arrayStr):
            tmp.append([i for i in item for _ in range(l)])
            l *= len(item)
        return list(reversed(tmp))





if __name__ == '__main__':

    multi_dimensional_array_cross_group = MultidimensionalArrayCrossGroup()
    test = [['张三', '李四'], ['打', '拿', '亲'], ['鱼', '猫', '美女']]
    for i in multi_dimensional_array_cross_group.calculation(test):
        print(i)



