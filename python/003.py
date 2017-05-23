import sys
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        buff_dict = dict()

        max_len = 0
        str_len = 0
        start_idx = 0
        end_idx = 0
        min_idx = -1
        while True:
            if s[end_idx] in buff_dict.keys() and buff_dict[s[end_idx]] > min_idx:
                min_idx = buff_dict[s[end_idx]]
                start_idx = buff_dict[s[end_idx]] + 1
                str_len = end_idx - start_idx

            buff_dict[s[end_idx]] = end_idx
            end_idx += 1
            str_len += 1
            max_len = max(str_len, max_len)
            if end_idx == len(s):
                break

        return max_len

if '__main__' == __name__:
    solver = Solution()
    print solver.lengthOfLongestSubstring(sys.argv[1])
