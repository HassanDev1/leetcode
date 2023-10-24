class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hmap = {}
        
        for src,dst in paths:
            if src not in hmap:
                hmap[src] = [dst]
            else:
                hmap[src].append(dst)
                
        for src,dst in paths:
            if dst not in hmap:
                return dst
        