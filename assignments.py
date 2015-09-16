__author__ = 'martinpettersson'
import random
import monkdata as m
import dtree as d


def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]

monk1train, monk1val = partition(m.monk1, 0.6)

def prune_tree(tree):
    pruned_trees = d.allPruned(tree)
    pruned_trees_performance = [0 for x in range(len(pruned_trees))]
    for candidate in pruned_trees:
        index = pruned_trees.index(candidate)
        pruned_trees_performance[index] = d.check(candidate, monk1val)
    if d.check(tree, monk1val) <= max(pruned_trees_performance):
        tree = pruned_trees[pruned_trees_performance.index(max(pruned_trees_performance))]
        tree = prune_tree(tree)
    return tree


print(d.entropy(m.monk1))
print(d.entropy(m.monk2))
print(d.entropy(m.monk3))
print("\n")

print("monk-1: %f %f %f %f %f %f" % (
    d.averageGain(m.monk1, m.attributes[0]), d.averageGain(m.monk1, m.attributes[1]),
    d.averageGain(m.monk1, m.attributes[2]), d.averageGain(m.monk1, m.attributes[3]),
    d.averageGain(m.monk1, m.attributes[4]), d.averageGain(m.monk1, m.attributes[5])
))

print("monk-2: %f %f %f %f %f %f" % (
    d.averageGain(m.monk2, m.attributes[0]), d.averageGain(m.monk2, m.attributes[1]),
    d.averageGain(m.monk2, m.attributes[2]), d.averageGain(m.monk2, m.attributes[3]),
    d.averageGain(m.monk2, m.attributes[4]), d.averageGain(m.monk2, m.attributes[5])
))

print("monk-3: %f %f %f %f %f %f" % (
    d.averageGain(m.monk3, m.attributes[0]), d.averageGain(m.monk3, m.attributes[1]),
    d.averageGain(m.monk3, m.attributes[2]), d.averageGain(m.monk3, m.attributes[3]),
    d.averageGain(m.monk3, m.attributes[4]), d.averageGain(m.monk3, m.attributes[5])
))

monk1_subset = d.select(m.monk1, m.attributes[4], 3)

print len(monk1_subset)
print(d.mostCommon(monk1_subset))
monk1_subset_tree = d.buildTree(monk1_subset, m.attributes, 5)
print(monk1_subset_tree)

t1 = d.buildTree(m.monk1, m.attributes);
print(d.check(t1, m.monk1test))
print(d.check(t1, m.monk1))

t2 = d.buildTree(m.monk2, m.attributes);
print(d.check(t2, m.monk2test))
print(d.check(t2, m.monk2))

t3 = d.buildTree(m.monk3, m.attributes);
print(d.check(t3, m.monk3test))
print(d.check(t3, m.monk3))

