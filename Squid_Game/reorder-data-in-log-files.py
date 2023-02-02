# https://leetcode.com/problems/reorder-data-in-log-files/


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        new_log = []
        digit_logs = []
        letter_logs = []
        for log in logs:
            if log[-1].isnumeric():
                digit_logs.append( log )
            else:
                log_arr = log.split()
                arranged_log = log_arr[1:]
                letter_logs.append( ( ( " ".join( arranged_log ) , log_arr[0] ), log ) )
                
        letter_logs.sort()
        new_letter_logs = []
        for log in letter_logs:
            new_letter_logs.append( log[-1] )
        
        return new_letter_logs + digit_logs
