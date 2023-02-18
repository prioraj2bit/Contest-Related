n = int(input())
balls = list(map(int, input().split()))

buckets = set()

for ball in balls:
    buckets.add(ball)

print(len(buckets))
