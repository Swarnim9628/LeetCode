class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        a=[first]
        for i in range(len(encoded)):           
                first^=encoded[i]
                a.append(first)
        return a
            
        