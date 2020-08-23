class Solution:
    def reorderLogFiles(self, logs):
        '''
        :type logs: List[str]
        :rtype: List[str]
        '''
        letter_logs = []
        digit_logs = []
        for log in logs:
            if log.split()[1].isnumeric():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        letter_logs = sorted(letter_logs, key = lambda x: (x.split()[1:], x.split()[0]))
        return letter_logs + digit_logs
