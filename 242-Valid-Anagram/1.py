class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist=[]
        tlist=[]
        if len(s)==len(t):
            for i in s:
                slist.append(i)
            
            for i in t:
                tlist.append(i)

            for j in slist:
                for k in range(len(tlist)):
                    if j==tlist[k]:
                        tlist.remove(tlist[k])
                        break

            if len(tlist)!=0:
                return False
            else:
                return True

