Examples of Round Robin: 

1. Your computer or smartphone is constantly multitasking. 
However, a single CPU core can technically only do one thing at a exact microsecond.
How it works: The OS gives each running app a small "time slice" (e.g., 10 milliseconds). 
When the time is up, the CPU moves to the next app in the queue.
Result: Because it rotates so fast, it looks like all your apps are running simultaneously.

2. When you type google.com, your request doesn't go to just one massive computer.
A DNS server can have a list of several different IP addresses for the same website. 
Each time a user asks for the address, the DNS server hands out the next IP in the list.
It's a "poor man's load balancer"—it’s a simple, cheap way to distribute web traffic across multiple global data centers.

Fun take at the Round Robin: Imagine you are at a party and everyone gets 1 slice of pizza per round. 
