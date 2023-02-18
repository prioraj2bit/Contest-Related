n = int(input()) # number of balls
balls = list(map(int, input().split())) # ball values

buckets = set() # set to store the different ball values

for ball in balls:
    buckets.add(ball)

print(len(buckets)) # print the number of buckets
