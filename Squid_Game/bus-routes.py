# https://leetcode.com/problems/bus-routes/


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(list)
        heap = []
        visited = {}
        m = len( routes )
        
        if source == target:
            return 0
        
        for j in range( m ):
            route = routes[j]
            n = len( route )
            for i in range( n ):
                stop = route[i]
                graph[stop].append( (route[(i+1) % n], j) )
        
                # find buses at source
                if stop == source:
                    heappush( heap, (1, stop, j) )  # the first 1 is the number of buses used
        
        final = float("inf")
        while heap:
            buses, stop, route = heappop( heap )
            if stop == target:
                final = min( final, buses )
            
            if (stop, route) not in visited or visited[(stop, route)] > buses:
                visited[(stop, route)] = buses
            
                for bus, n_route in graph[stop]:
                    if route != n_route:
                        heappush( heap, (buses + 1, bus, n_route) )
                    else:
                        heappush( heap, (buses, bus, n_route) )
                    
        if final == float("inf"):
            return -1
        return final
