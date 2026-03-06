class RoundRobinBalancer:
  def __init__(self, servers):
    self.servers= servers
    #Initialize the index to 0 
    self.index =0 

  #get next server 
  def get_next_server():
    #Get the server at the current index.
    current_server= self.servers[self.index]
    # This ensures that once the index reaches the end of the length of the servers, repeats again. 
    self.index = (self.index + 1) % len(self.servers) 
    return current_server

servers = ["Server A","Server B"]
rr= RoundRobinBalancer(servers)

# For length of says 10 requests 
for i in range(1,11):
  current_server = rr.get_next_server()
  print("Request : {i:02d} --> routed to {current_server}")


#Output :
#Request 01 --> routed to Server A
#Request 02 --> routed to Server B
#Request 03 --> routed to Server A
#Request 04 --> routed to Server B
#Request 05 --> routed to Server A
#Request 06 --> routed to Server B
#Request 07 --> routed to Server A
#Request 08 --> routed to Server B
#Request 09 --> routed to Server A
#Request 10 --> routed to Server B
