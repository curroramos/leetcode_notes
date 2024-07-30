### Bit Manipulation Overview

Bit manipulation involves directly operating on individual bits of binary numbers. It is a powerful technique often used to optimize performance, particularly in low-level programming and algorithm design. Understanding bit manipulation can lead to more efficient solutions for various problems.

### Common Bitwise Operators

1. **AND (`&`)**: Sets each bit to 1 if both bits are 1.
   ```python
   a = 5  # 0101
   b = 3  # 0011
   print(a & b)  # Output: 1 (0001)
   ```

2. **OR (`|`)**: Sets each bit to 1 if one of the bits is 1.
   ```python
   a = 5  # 0101
   b = 3  # 0011
   print(a | b)  # Output: 7 (0111)
   ```

3. **XOR (`^`)**: Sets each bit to 1 if only one of the bits is 1.
   ```python
   a = 5  # 0101
   b = 3  # 0011
   print(a ^ b)  # Output: 6 (0110)
   ```

4. **NOT (`~`)**: Inverts all the bits.
   ```python
   a = 5  # 0101
   print(~a)  # Output: -6 (in 32-bit, 11111111111111111111111111111010)
   ```

5. **Left Shift (`<<`)**: Shifts bits to the left, filling with zeros.
   ```python
   a = 5  # 0101
   print(a << 1)  # Output: 10 (1010)
   ```

6. **Right Shift (`>>`)**: Shifts bits to the right, filling with the sign bit (for signed numbers).
   ```python
   a = 5  # 0101
   print(a >> 1)  # Output: 2 (0010)
   ```

### Common Bit Manipulation Tricks

1. **Check if a number is even or odd**:
   ```python
   def is_even(n):
       return (n & 1) == 0

   # Example usage
   print(is_even(4))  # Output: True
   print(is_even(7))  # Output: False
   ```

2. **Swap two numbers without using a temporary variable**:
   ```python
   def swap(a, b):
       a = a ^ b
       b = a ^ b
       a = a ^ b
       return a, b

   # Example usage
   a, b = 5, 3
   a, b = swap(a, b)
   print(a, b)  # Output: 3 5
   ```

3. **Count the number of 1s in the binary representation of a number (Hamming Weight)**:
   ```python
   def hamming_weight(n):
       count = 0
       while n:
           count += n & 1
           n >>= 1
       return count

   # Example usage
   print(hamming_weight(11))  # Output: 3 (1011 has three 1s)
   ```

4. **Check if a number is a power of 2**:
   ```python
   def is_power_of_two(n):
       return n > 0 and (n & (n - 1)) == 0

   # Example usage
   print(is_power_of_two(16))  # Output: True
   print(is_power_of_two(18))  # Output: False
   ```

5. **Find the only non-repeated element in an array where every other element is repeated twice**:
   ```python
   def single_number(nums):
       result = 0
       for num in nums:
           result ^= num
       return result

   # Example usage
   nums = [4, 1, 2, 1, 2]
   print(single_number(nums))  # Output: 4
   ```

### Advanced Bit Manipulation Techniques

1. **Bit Masking**:
   - Using a bitmask to extract, set, or toggle specific bits in a number.
   - **Example**: Extract the k-th bit:
     ```python
     def get_bit(num, k):
         return (num >> k) & 1

     # Example usage
     print(get_bit(5, 0))  # Output: 1 (5 is 0101, the 0th bit is 1)
     print(get_bit(5, 1))  # Output: 0 (5 is 0101, the 1st bit is 0)
     ```

2. **Bitwise Addition (without using `+` operator)**:
   ```python
   def add(a, b):
       while b != 0:
           carry = a & b
           a = a ^ b
           b = carry << 1
       return a

   # Example usage
   print(add(5, 3))  # Output: 8
   ```

3. **Generate All Subsets of a Set**:
   ```python
   def subsets(nums):
       result = []
       n = len(nums)
       for i in range(1 << n):
           subset = [nums[j] for j in range(n) if (i & (1 << j))]
           result.append(subset)
       return result

   # Example usage
   nums = [1, 2, 3]
   print(subsets(nums))
   # Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
   ```

4. **Find the Two Non-Repeated Elements in an Array where every other element is repeated twice**:
   ```python
   def single_numbers(nums):
       xor = 0
       for num in nums:
           xor ^= num
       # Get the rightmost set bit
       rightmost_set_bit = xor & -xor
       num1, num2 = 0, 0
       for num in nums:
           if num & rightmost_set_bit:
               num1 ^= num
           else:
               num2 ^= num
       return num1, num2

   # Example usage
   nums = [1, 2, 1, 3, 2, 5]
   print(single_numbers(nums))  # Output: (3, 5)
   ```

### Applications of Bit Manipulation

1. **Cryptography**: Encryption and decryption algorithms often use bit manipulation.
2. **Data Compression**: Efficiently encoding data by manipulating bits.
3. **Error Detection and Correction**: Using parity bits and checksums.
4. **Graphics and Image Processing**: Manipulating pixels and color values.
5. **Networking**: Manipulating IP addresses and subnet masks.

### Advantages and Disadvantages

**Advantages:**
- **Efficiency**: Bit manipulation can be significantly faster and use less memory.
- **Control**: Provides low-level control over data.

**Disadvantages:**
- **Complexity**: Code can be harder to read and understand.
- **Portability**: Bit manipulation may depend on system architecture (e.g., 32-bit vs. 64-bit).
