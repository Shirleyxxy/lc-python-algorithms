## lc811: Subdomain Visit Count
## Topics: string, list, dictionary / hashmap

## Time complexity: O(N), where N is the length of cpdomains and
## assuming the length of cpdomains[i] is fixed

## Space complexity: O(N)

## d.items()
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dom2cnt = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            subdomains = domain.split(".")
            for i in range(len(subdomains)):
                curr = ".".join(subdomains[i:])
                if curr not in dom2cnt:
                    dom2cnt[curr] = count
                else:
                    dom2cnt[curr] += count
        return [f"{cnt} {dom}" for dom, cnt in dom2cnt.items()]
