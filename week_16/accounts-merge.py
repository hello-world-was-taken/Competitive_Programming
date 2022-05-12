# https://leetcode.com/problems/accounts-merge/



class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        owner = {}
        owners_parent = {} # path_compress for this too
        
        def normal_path_compress(node): # for the parents
            if owners_parent[node] == node:
                return owners_parent[node]
            owners_parent[node] = normal_path_compress(owners_parent[node])
            return owners_parent[node]
        
        def path_compress(node): # for the emails
            if owner[node] == owners_parent[owner[node]]:
                return owner[node]
            owner[node] = owners_parent[owner[node]]
            return owner[node]
        
        # for the owners
        for i, emails in enumerate(accounts):
            for email in emails:
                owners_parent[(email, i)] = (email, i)
                break # runs only for the first element
        
        for i, emails in enumerate(accounts):
            for email in emails[1:]:
                if email not in owner:
                    owner[email] = (emails[0], i)
                else:
                    owners_parent[normal_path_compress((emails[0], i))] = normal_path_compress(owner[email])

        for i, emails in enumerate(accounts):
            for email in emails:
                normal_path_compress((email, i)) # again runs only once
                break
                
        for i, emails in enumerate(accounts):
            for email in emails[1:]:
                path_compress(email)
                
        owner_set = set(owners_parent.values())
        owner_with_email = defaultdict(list)
        
        for key in owner.keys():
            owner_with_email[owner[key]].append(key)
            
        # print(owner_with_email)
        sort_keys = list(owner_with_email.keys())
        for key in sort_keys:
            owner_with_email[key].sort()
        ans = [[key[0]] for key in sort_keys]
        
        for i, key in enumerate(sort_keys):
            for email in owner_with_email[key]:
                ans[i].append(email)
        return ans
                
                    
