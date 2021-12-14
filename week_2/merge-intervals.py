#QUESTION
#https://leetcode.com/problems/merge-intervals/

def merge(self, intervals):
        arr_len = len(intervals)
        intervals.sort()
        print(intervals)
        
        i = 0
        while (i < arr_len-1):
            if(intervals[i][1] >= intervals[i+1][0]):
                if(intervals[i][1] < intervals[i+1][1]):
                    intervals[i][1] = intervals[i+1][1]
                intervals.pop(i+1)
                i -= 1
                arr_len -= 1
                
            i += 1
        return(intervals)