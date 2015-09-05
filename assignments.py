__author__ = 'martinpettersson'

import monkdata as m
from dtree import entropy, averageGain, select, mostCommon, buildTree
import dtree as d

print(entropy(m.monk1))
print(entropy(m.monk2))
print(entropy(m.monk3))
print("\n")

print("monk-1: %f %f %f %f %f %f" % (
                                     averageGain(m.monk1, m.attributes[0]), averageGain(m.monk1, m.attributes[1]),
                                     averageGain(m.monk1, m.attributes[2]), averageGain(m.monk1, m.attributes[3]),
                                     averageGain(m.monk1, m.attributes[4]), averageGain(m.monk1, m.attributes[5])
                                     ))

print("monk-2: %f %f %f %f %f %f" % (
                                     averageGain(m.monk2, m.attributes[0]), averageGain(m.monk2, m.attributes[1]),
                                     averageGain(m.monk2, m.attributes[2]), averageGain(m.monk2, m.attributes[3]),
                                     averageGain(m.monk2, m.attributes[4]), averageGain(m.monk2, m.attributes[5])
                                     ))

print("monk-3: %f %f %f %f %f %f" % (
                                     averageGain(m.monk3, m.attributes[0]), averageGain(m.monk3, m.attributes[1]),
                                     averageGain(m.monk3, m.attributes[2]), averageGain(m.monk3, m.attributes[3]),
                                     averageGain(m.monk3, m.attributes[4]), averageGain(m.monk3, m.attributes[5])
                                     ))

monk1_subset = select(m.monk1, m.attributes[4], 3)

print len(monk1_subset)
print(mostCommon(monk1_subset))
monk1_subset_tree = buildTree(monk1_subset, m.attributes, 5)
print(monk1_subset_tree)

t1=d.buildTree(m.monk1, m.attributes);
print(d.check(t1, m.monk1test))

t2=d.buildTree(m.monk2, m.attributes);
print(d.check(t2, m.monk2test))

t3=d.buildTree(m.monk3, m.attributes);
print(d.check(t3, m.monk3test))