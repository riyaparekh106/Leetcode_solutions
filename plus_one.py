class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = int(''.join(str(i) for i in digits))
        b = []
        c = str(a+1)
        for i in c:
            b.append(i)
        return b
