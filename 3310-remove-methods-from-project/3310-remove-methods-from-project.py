class Solution:
  def remainingMethods(
      self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
    graph = [[] for _ in range(n)]
    for u, v in invocations:
      graph[u].append(v)
    q = collections.deque([k])
    seen = {k}
    while q:
      curr = q.popleft()
      for v in graph[curr]:
        if v not in seen:
          seen.add(v)
          q.append(v)

    for u in range(n):
      if u in seen:
        continue
      for v in graph[u]:
        if v in seen:
          return list(range(n))
    return [i for i in range(n) if i not in seen]