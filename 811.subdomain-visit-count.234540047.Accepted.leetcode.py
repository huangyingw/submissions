class Solution:
    def subdomainVisits(self, cpdomains):
        dom_count = {}
        for domin in cpdomains:
            count, domin_s = domin.split()
            domins = domin_s.split('.')
            for i in range(len(domins)):
                temp_domin = '.'.join(domins[i:])
                dom_count[temp_domin] = dom_count.get(temp_domin, 0) + int(count)
        return [str(v) + ' ' + i for i, v in dom_count.items()]
