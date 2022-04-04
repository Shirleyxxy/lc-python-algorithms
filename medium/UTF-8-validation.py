## Time complexity: O(N)
## Space complexity: O(N)


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # number of bytes in the current UTF-8 character
        n_bytes = 0

        for num in data:
            # we only need the least significant 8 bits for each number
            bin_rep = format(num, '#010b')[-8:]

            # if this is the case, we are to start processing a new UTF-8 character
            if n_bytes == 0:
                for bit in bin_rep:
                    if bit == '0':
                        break
                    else:
                        n_bytes += 1

                # 1-byte character
                if n_bytes == 0:
                    continue

                # invalid scenarios according to the rules of the problem
                if n_bytes == 1 or n_bytes > 4:
                    return False

            else:
                # check if they adhere to the pattern "10xxxxxx"
                if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                    return False

            # we reduce the number of bytes to process by 1 after each integer
            n_bytes -= 1

        return n_bytes == 0
