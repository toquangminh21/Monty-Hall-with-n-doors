'''
Minh To
Sunday 5/31/2020
NOTE: because my computer is pretty trash (4GB CPU, 2 cores only), the benefits of multiprocessing is not as evident.
With 5M simulations, 4 processes only halve the time, when it should really quarter it. 
Because it takes so long to fire up the processes in the first place
'''

import multiprocessing as mp
import time, random
from multiprocessing.queues import Empty
from Game import Game
from GameNoMP import Game as GameNoMP
from Player import Player


def main():
    # Approach: The task that we want to do multiprocessing on is Game.playGame() method - aka "worker function"
    # Therefore, the Game object must at least have an outputQ parameters in __init__.
    # It does NOT necessarily need an inputQ because theres nothing to input.
    # We'll put the winCounter on the outputQ

    # In our main program (this one), we'll
    # 2a) initialize the queues
    # 2b) create 4 processes on 2 cores
    # 2c) call join() on the processes to block the main program until all processes are done
    # 2d) get the winCounter from the outputQ stored in a list, sum them all up, and divide by nSimulations to find probability of winning using that specific strategy

    print('=== EXERCISE 6.2.1: Multiprocessing on Monty Hall problem')
    
    # Initialize 2 queues
    # In case we need to input something
    input_queue = mp.Queue()
    output_queue = mp.Queue()

    # Initialize Game objects
    player = Player()
    stay = Game(input_queue, output_queue, player)
    stayNoMP = GameNoMP(player)
    switch = Game(input_queue, output_queue, player)
    switchNoMP = GameNoMP(player)

    # number of simulations
    nSimulations = 500000

#########################
    print('=== Staying: 500,000 simulations and 4 processes:')
    s = time.time()

    # 2b) Design the process: playGame() takes 3 parameters: strategy, initialList, simulations
    # We want 4 processes doing nSimulations, so for the simulations parameter, divide by 4
    processesStay = [mp.Process(target=stay.playGame, args=('stay', [1,2,3,4,5], int(nSimulations/4))) for _ in range(4)]

    # Start the processes
    for process in processesStay:
        process.start()

    # join() to ensure main will not proceed until all child processes are done
    # Must be a separate loop or else it will be like running linearly
    for process in processesStay:
        process.join()

    'At this point, all processes are done and should print out "A worker has finished"' \
    'output_queue should contain winCounters from all the processes, we just have to add them up now'

    totalWinsStay = 0
    while True:
        try:
            # Aggregating the results from all our child processes
            result = output_queue.get(timeout=1)
            totalWinsStay += result
        except Empty:
            break

    e = time.time()

    print(f'Number of wins: {totalWinsStay}')
    print(f'Number of losses: {nSimulations-totalWinsStay}')

    # calculate the probability of success for the chosen strategy: # wins / # simulations
    print(f'Probability of success with "stay" strategy: {totalWinsStay/nSimulations}')
    print(f'TOTAL time taken across all processes: {e-s} seconds')


###########################
    print('\n=== Staying No Multiprocessing: 500,000 simulations')
    s = time.time()
    stayNoMP.playGame('stay', [1,2,3,4,5], nSimulations)
    e = time.time()
    print(f'Time taken: {e-s} seconds')


###########################

    print('\n=== Switching: 500,000 simulations and 4 processes:')
    
    s = time.time()
    processesSwitch = [mp.Process(target=switch.playGame, args=('switch', [1, 2, 3,4,5], int(nSimulations / 4))) for _ in
                     range(4)]

    for process in processesSwitch:
        process.start()

    for process in processesSwitch:
        process.join()

    totalWinsSwitch = 0
    while True:
        try:
            result = output_queue.get(timeout=1)
            totalWinsSwitch += result
        except Empty:
            break

    e = time.time()

    print(f'Number of wins: {totalWinsSwitch}')
    print(f'Number of losses: {nSimulations-totalWinsSwitch}')
    print(f'Probability of success with "Switch" strategy: {totalWinsSwitch / nSimulations}')
    print(f'TOTAL time taken across all processes: {e-s} seconds')

###########################
    print('\n=== Switching No Multiprocessing: 500,000 simulations')
    s = time.time()
    switchNoMP.playGame('switch', [1,2,3,4,5], nSimulations)
    e = time.time()
    print(f'Time taken: {e-s} seconds')


if __name__ == '__main__':
    main()
