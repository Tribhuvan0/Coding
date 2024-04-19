class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seenset = set()
        for email in emails:
            local, domain= email.split('@')
            local = local.replace('.','')
            name = local.split('+')[0]
            seenset.add(name + '@' + domain)
        return len(seenset)
        