# matches: (str_a, str_b)
def can_a_beat_b(matches, str_a, str_b):
    # graph: {str:set([])}
    graph = {}
    for t in matches:
        if t[0] not in graph:
            graph[t[0]] = set([t[1]])
        else:
            graph[t[0]].add(t[1])

    visited = set([])
    return is_reachable(graph, str_a, str_b, visited)

def is_reachable(graph, cur, dst, visited):
    if cur == dst:
        return True
    elif (cur in visited) or (cur not in graph):
        return False
    visited.add(cur)
    for s in graph[cur]:
        if is_reachable(graph, s, dst, visited):
            return True
    return False
