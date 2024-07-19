class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq = {i:[] for i in range(numCourses)}
        visited, cycle = set(), set()
        for crs, pre in prerequisites:
            preReq[crs].append(pre)
        
        output = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in preReq[crs]:
                if dfs(pre) == False: 
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
            
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
        