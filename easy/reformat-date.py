## My solution
class Solution:
    def reformatDate(self, date):
        '''
        :type date: str
        :rtype: str
        '''
        months_d = {'Jan':'01', 'Feb':'02', 'Mar':'03',
                    'Apr':'04', 'May':'05', 'Jun':'06',
                    'Jul':'07', 'Aug':'08', 'Sep':'09',
                    'Oct':'10', 'Nov':'11', 'Dec':'12'}
        day, month, year = date.split()
        if len(day[:-2]) == 2:
            day = day[:-2]
        else:
            day = '0' + day[:-2]
        month = months_d[month]
        return '-'.join([year, month, day])



## Another solution using format function
class Solution:
    def reformatDate(self, date):
        '''
        :type date: str
        :rtype: str
        '''
        parts = date.split()
        day = int(parts[0][:-2])
        month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'].index(parts[1]) + 1
        year = int(parts[2])
        ## 02d formats an integer (d) to a field of minimum width 2 (2), with zero-padding on the left (leading 0)
        return '{:04d}-{:02d}-{:02d}'.format(year, month, day)
