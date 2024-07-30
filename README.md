# Tennis-Event-Organizer

Python script designed to organize matchplay events at my work. The script can take between 8 and 12 players. The code is object-oriented and each player is an object with 6 attributes:
name, skill, partner, singles (if player is willing to play singles), previous partners, and previous oppenents. This means the program is scalable and more players can be easily saved and added into the 
script. The program currently contains every active member at my tennis club. The program is used by myself and other coaches at the club. 
The user of the program will enter all the players playing and the script organizes them into 3 rounds of matchplay. In each round, the script makes sure that no 2 players will play with each other more than
once and no player will have to play the same opponents more than once. The script will also make sure that players who want to play with each other will be partnered together the whole time and that only 
players willing to play singles will be equaly rotated into the singles matches if the numbers require it. The script will create multiple rotations/rounds that match the criteria and select the one with the 
most equal/competetive play. This is calculated using each player's skill attribute and ensures the matches played are fair and of similar skill.
