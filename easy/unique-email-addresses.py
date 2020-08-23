# my solution
class Solution(object):
    def numUniqueEmails(self, emails):
        unique_emails = []
        for email in emails:
            local = email.split('@')[0]
            domain = email.split('@')[1]
            local = local.split('+', 1)[0].replace('.', '')
            unique_emails.append(local + '@' + domain)

        unique_emails = list(set(unique_emails))
        return len(unique_emails)

# leetcode solution
class Solution(object):
    def numUniqueEmails(self, emails):
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.', '') + '@' + domain)
        return len(seen)


class Solution(object):
    def numUniqueEmails(self, emails):
        '''
        :type emails: List[str]
        :rtype: int
        '''
        email_set = set()
        for email in emails:
            elements = email.split('@')
            email_set.add(elements[0].split('+')[0].replace('.', '') + '@' + elements[1])
        return len(email_set)
