
def groupAnagrams():
        strs = ["eat","tea","tan","ate","nat","bat"]
        sorted_strs=[]
        out1=[]
        out2=[]
        flag=[]
        for k in strs:
            sorted_strs.append(sorted(k))

        for i in range(len(sorted_strs)):
            out1=[] 
            if sorted_strs[i] not in flag:
                  
                for j in range(len(sorted_strs)):
                    if i!=j:
                        
                        if sorted_strs[i]== sorted_strs[j]:
                            flag.append(sorted_strs[j])
                            out1.append(strs[j])
                out2.append(out1)
                

        print(out2)

        print(sorted_strs)

        
      


