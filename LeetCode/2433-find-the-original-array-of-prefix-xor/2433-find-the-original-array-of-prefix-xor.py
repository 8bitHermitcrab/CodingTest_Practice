class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [0] * len(pref)
        arr[0] = pref[0]
        
        for i in range(1, len(arr)):
            arr[i] = pref[i] ^ pref[i-1]
        return arr
        