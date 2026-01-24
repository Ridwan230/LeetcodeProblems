class Solution:
    def compress(self, chars: List[str]) -> int:
        pointer_iter=0
        pointer_write=0
        while pointer_iter<len(chars):
            char=chars[pointer_iter]
            count=0

            while pointer_iter<len(chars) and chars[pointer_iter]==char:
                pointer_iter+=1
                count+=1
            
            chars[pointer_write]=char
            pointer_write+=1

            if count>1:
                for i in str(count):
                    chars[pointer_write]=i
                    pointer_write+=1
        return pointer_write
            


        