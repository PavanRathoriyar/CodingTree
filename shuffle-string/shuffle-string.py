class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        a=list(s)
        for i in range(len(s)):
            a[indices[i]]=s[i]
        s=''
        for i in a:
            s+=i
        return s