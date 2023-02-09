# https://leetcode.com/problems/reformat-date/


class Solution:
    def reformatDate(self, date: str) -> str:
        months_num = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12"
        }
        
        date = date.split()
        day = date[0][:-2]
        if len(day) == 1:
            day = "0" + day
        month = months_num[date[1]]
        year = date[2]
        
        return year + '-' + month + '-' + day
        
