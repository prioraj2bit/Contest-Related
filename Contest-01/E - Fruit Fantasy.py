n, x = map(int, input().split())
trees = list(map(int, input().split()))

i, j = 0, 0
sum_fruits = 0
min_trees = float('inf')

while j < n:
    sum_fruits += trees[j]
    while sum_fruits >= x:
        min_trees = min(min_trees, j - i + 1)
        sum_fruits -= trees[i]
        i += 1
    j += 1

if min_trees == float('inf'):
    print("Shombhob na")
else:
    print(min_trees)
