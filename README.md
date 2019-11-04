# Logix
 
## Chinese checkers players made By Jayden Geisler 

ccExp.py 

this file brings the player and the board together and regulates what player will go next 

ccBoard.py 

	this is the board of the game, will return a list of the positions of the board pieces also the value of the players positions, the values are how close you are to the winning side

ccPlayer.py 

	file that contains all the different types of players 

MC_player 

	this player uses Monte Carlo simulation to predict where the most likely to win move is on the current board state

Random_Player 

	this player just plays randomly 

Ordered_player 

	moves to the highest value position

graphics.py 

	a tool I used for displaying the current game acquired from:
	https://mcsp.wartburg.edu/zelle/python/graphics.py
