from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for bill in bills:
            # customer pays $5
            if bill == 5:
                five+=1
            # customer pays $10
            elif bill == 10:
                if five == 0 : return False
                five -= 1
                ten += 1
            # customer pays $20
            else:
                # prefer giving $10 + $5
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                # otherwise give 3 x $5
                elif five >= 3:
                    five -= 3
                else:
                    # no valid change
                    return False
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.lemonadeChange([5,5,5,10,20]))
    print(sol.lemonadeChange([5,5,10]))