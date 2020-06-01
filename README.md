# Monty-Hall-with-n-doors
Simple Python program using OOP and the multiprocessing module to empirically prove that switching will always offer a better chance of winning, specifically an (n-1)/n probability of winnings given n doors.

Ex: 3 doors, probability of winning by switching = (3-1)/3 = 2/3 ~= 66.66%
Ex2: 100 doors, probability of winning by switching = (100-1)/100 = 99%

For those who are unfamiliar, per Wikipedia:
Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats.
You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat.
He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?


Assumptions for the formula to work:
The host must always open a door that was not picked by the contestant.
The host must always open a door (or doors if there is more than 3 doors originally) to reveal a goat (or goats) and never the car.
The host must always offer the chance to switch between the originally chosen door and the remaining closed door.

Any feedback or pull requests is welcome. Let me know!
