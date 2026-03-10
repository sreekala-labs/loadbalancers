#Iteration tools which is used for fast and efficient iteration and baiscyally recycles itself to the beginning and also used when there is infinite numbers.
import itertools
class WeightedRoundRobin:
  #Constructor
  def __init__(self, servers):
    #Declare an array of weighted pool.
    self.weighted_pool=[]
    for server, weight in servers.items():
      #extend method is to add elements to the array.
      self.weighted_pool.extend([server] * weight)

    #Infinite Cycle. Resets from beginning based on the condition. 
    self.selector= itertools.cycle(self.weighted_pool)

  def get_next_server(self):
    return next(self.selector)
    
#Dictionary of server and weight.
servers={
  "Server A":3,
  "Server B":2,
  "Server C":1
}

lb=WeightedRoundRobin(servers)
for i in range(1,13):
  current_server= lb.get_next_server()
  print(f"Request : {0:2d} --> {current_server}")
