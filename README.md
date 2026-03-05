# Load Balancers

Load Balancers are like air traffic controllers, they decide where and how to route the requests to ensure that no servers are overwhelmed while others sit idle.

There are several algorithms to handle the Load Balancing Act:

1. Round Robin - Use it when you have a predictable traffic. This algo assigns requests to a server in a sequenital manner.
   Server A -> Server B -> Server C -> Repeat.
2. Weighted Round Robin -> Use it when you want servers with different CPU/RAM specs.
   Server A (Wt: 2) -> Server B . Server A gets 2 requests where as Server B gets 1 request. 
4. Least Connections -> Use it when	requests vary in processing time.
5. Least Response Time - High-Performance apps where speed is King.
6. IP Hash - Sticky Sessions, use it when you need a user to stick to one server.(For example: Shopping Cart). 
