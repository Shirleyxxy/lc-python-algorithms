class Solution:
    def subdomainVisits(self, cpdomains):
        '''
        :type cpdomains: List[str]
        :rtype: List[str]
        '''
        count_d = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count) #easy to miss
            subdomains = domain.split('.')
            for i in range(len(subdomains)):
                curr = '.'.join(subdomains[i:])
                if curr not in count_d:
                    count_d[curr] = count
                else:
                    count_d[curr] += count

        return ['{} {}'.format(ct, dom) for dom, ct in count_d.items()]
