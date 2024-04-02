from collections import defaultdict, deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        # Create a graph where each bus stop is a node and
        # each route is an edge connecting bus stops
        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)
        
        # Initialize a set to keep track of visited bus routes
        visited_routes = set()
        
        # Initialize a queue for BFS
        queue = deque([(source, 0)])  # (current_stop, num_buses)
        
        # Perform BFS
        while queue:
            current_stop, num_buses = queue.popleft()
            
            # Check if the current stop is the target
            if current_stop == target:
                return num_buses
            
            # Check all routes passing through the current stop
            for route_index in stop_to_routes[current_stop]:
                # If the route is not visited yet, mark it as visited
                if route_index not in visited_routes:
                    visited_routes.add(route_index)
                    # Check all stops on this route
                    for next_stop in routes[route_index]:
                        # Add unvisited stops to the queue
                        if next_stop != current_stop:
                            queue.append((next_stop, num_buses + 1))
        
        # If no path found
        return -1
