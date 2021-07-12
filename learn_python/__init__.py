def isIsomorphic(s: str, t: str) -> bool:
    ss = {}
    ss2 = {}
    for i in range(len(s)):
        print(s[i],ss,ss2)
        if s[i] in ss:
            print('1:',t[i],ss[s[i]])
            if t[i] != ss[s[i]]:
                return False
        if s[i] in ss2:
            print('2:', t[i], ss[s[i]])
            if t[i] != ss2[s[i]]:
                return False
        ss[s[i]] = t[i]
        ss2[t[i]] = s[i]

    return True


flag=isIsomorphic('badc','baba')
print(flag)

