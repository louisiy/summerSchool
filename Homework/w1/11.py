class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        i = 0
        j = 0
        answerList = []
        # 选取目标字符子串
        while i+9 < len(s)-1:
            j = i + 1
            target = s[i:i+10]
            # 选取比较子串
            while j+9 < len(s)-1 :
                compare = s[j:j+10]
                # 比较
                if compare == target:
                    if target not in answerList:
                        answerList.append(target)
                    break
                j += 1
            i += 1
        return answerList

#主程序
solu = Solution()
str0 = input("DNA：")
print(solu.findRepeatedDnaSequences(str0))