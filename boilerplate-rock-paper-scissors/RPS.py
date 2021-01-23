# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
dict={}
def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    global dict
    n = 6


    guess = "R"
    if len(opponent_history) > n:
      temp = ''.join(opponent_history[-n:])

      if ''.join(opponent_history[-(n+1):]) in dict.keys():
        dict[''.join(opponent_history[-(n+1):])] += 1
      else:
        dict[''.join(opponent_history[-(n+1):])] = 1
      
      possible = [temp+'R', temp+'P', temp+'S']
      
      for k in possible:
        if k not in dict.keys():
  
          dict[k] = 0

      predict = max(possible, key = lambda x : dict[x])
      winset = {'R':'P', 'P':'S', 'S':'R'}
      guess = winset[predict[-1]]



    return guess

