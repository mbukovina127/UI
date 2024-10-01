from queue import Queue
import random

import myUtils
from gen import neighbour_swap
from salesperson import Salesperson


class TabooGuy(Salesperson):
    def __init__(self, path: list, taboo_size: int):
        super().__init__(path)
        self.taboo = Queue(taboo_size)
        self.o_min = myUtils.length_of_path(self.path)

    def find_better_paths(self, amount: int):
        m_paths = list()
        for i in range(amount):
            m_paths.append(self.find_path())

        m_paths.sort(key=lambda x: myUtils.length_of_path(x[1]), reverse=True)

        itt = 0
        while m_paths[itt][0] in self.taboo:
            itt += 1
        self.taboo.queue(m_paths[itt])
        return m_paths[itt]




    def find_path(self):
        copy = list()
        hash_n = 0
        index = 1
        for n in self.path:
            copy.append(n)
            hash_n += (n.x * n.y % list.__len__) * index
            index += 1
        # neighbour swap
        while random.randint(0,1) > 0:
            #not sure if it changes the list
            neighbour_swap(copy)
        #will and other mutations
        return [hash_n, copy]