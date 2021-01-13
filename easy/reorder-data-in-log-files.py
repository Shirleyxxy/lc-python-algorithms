## Time Complexity: O(NlogN)
## Space Complexity: O(N)

## Constraint: logs[i] is guaranteed to have an identifier and a word after the identifier
## Take-away:
## Sort a list by 2 keys
class Solution:
    def reorderLogFiles(self, logs):
        '''
        :type logs: List[str]
        :rtype: List[str]
        '''
        letter_logs, digit_logs = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        # sort the letter logs by 2 keys
        # The letter logs are ordered lexicographically ignoring identifier
        # with the identifier used in case of ties
        letter_logs.sort(key = lambda log: (log.split()[1:], log.split()[0]))
        return letter_logs + digit_logs
