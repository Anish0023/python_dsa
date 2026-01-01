from typing import List
class Solution:
    # Swap two numbers without using a temporary variable
    def swap2nums(self, a: int, b: int) -> tuple[int, int]:
        a = a ^ b
        b = a ^ b
        a = a ^ b
        return a, b
    # set the ith bit of a number
    def finding_set_ith_bit_leftshift(self, num: int, i: int):
        if (num & (1 << i)) != 0:
            return "Bit is already set"
        else:
            return "Bit unset"
    def finding_set_ith_bit_rightshift(self, num: int, i: int):
        if ((num >> i) & 1) != 0:
            return "Bit is already set"
        else:
            return "Bit unset"
    def set_ith_bit(self, num: int, i: int) -> int:
        return num | (1 << i)
    # clear the ith bit of a number
    def clear_ith_bit(self, num: int, i: int) -> int:
        return num & ~(1 << i)
    # toggle the ith bit of a number
    def toggle_ith_bit(self, num: int, i: int) -> int:
        return num^(1 << i)
    # remove the last set bit of a number 
    def remove_last_set_bit(self, num: int) -> int:
        return num & (num - 1)
    # check if the number is power of two
    def is_power_of_two(self, num: int) -> bool: # to be the power of  there should be only one set bit
        return num > 0 and (num & (num - 1)) == 0
    # count the number of set bits in a number
    def count_set_bits(self, num: int) -> int:
        #TC - O(k) where k is the number of set bits
        cnt = 0
        while num:
            num &= (num - 1)
            cnt += 1
        return cnt
if __name__ == "__main__":
    s = Solution()
    a, b = 5, 10
    print(f"Original a: {a}, b: {b}")
    a, b = s.swap2nums(a, b)
    print(f"Swapped a: {a}, b: {b}")
    
    num = 18  # Binary: 10010
    i = 1
    print(s.finding_set_ith_bit_leftshift(num, i))
    print(s.finding_set_ith_bit_rightshift(num, i))
    
    print(f"Set {i}th bit: {s.set_ith_bit(num, i)}")
    print(f"Clear {i}th bit: {s.clear_ith_bit(num, i)}")
    print(f"Toggle {i}th bit: {s.toggle_ith_bit(num, i)}")
    
    print(f"Remove last set bit: {s.remove_last_set_bit(num)}")
    
    power_num = 16
    print(f"Is {power_num} power of two? {s.is_power_of_two(power_num)}")
    
    count_num = 29  # Binary: 11101
    print(f"Number of set bits in {count_num}: {s.count_set_bits(count_num)}")

        