def findJudge(n: int, trust) -> int:
    # 表示user信任的人列表
    user_trust = [[] for s in range(n)]
    # 表示user被信任的人列表
    bei_trust = [0 for s in range(n)]

    for i in trust:
        # 人的下标
        per_idx = i[0]-1
        # 信任的人的下标
        trust_idx = i[1]-1

        user_trust[per_idx].append(trust_idx)
        bei_trust[trust_idx] += 1
    for i in range(n):
        if user_trust[i] == [] and bei_trust[i] == n-1:
            return i+1
    return -1

print(findJudge(3,[[1,3],[2,3]]))
