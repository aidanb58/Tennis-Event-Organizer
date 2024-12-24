# Tennis-Event-Organizer

Python script designed to organize matchplay events at a tennis club. The script can take between 8 and 12 players. The code is object-oriented and each player is an object with 6 attributes:
name, skill, partner, singles (if player is willing to play singles), previous partners, and previous oppenents. This means the program is scalable and more players can be easily added and saved into the 
program. The program currently contains every active member at my tennis club but a user could replace these instances with the players in their respective club or event. The program is currently used by myself and other coaches at the club. There is no option for 9 players because myself or another coach will always step in or step out to avoid this.

The user of the program will enter all the players playing and the script organizes them into 3 rounds of matchplay. The user can enter a player stored in the program by entering their name. If the player is not stored as a member, the user can enter "new" and will be prompted to enter the details for a new player to be added. The user will enter "stop" when they have entered all the players. In each round, the script makes sure that no 2 players will play with each other more than once and no player will have to play the same opponents more than once. The script will also make sure that players who want to play with each other will be partnered together the whole time and that only players willing to play singles will be equaly rotated into the singles matches if the numbers require it. For each round, the script will create the most competitive/similar in skill matches that meet the previously mentioned criteria. This is calculated using each player's skill attribute and ensures the matches played are fair and fun. 

Note: The class contains a list of players that are pros/coaches. This only impacts the program if there is an uneven number of players. If there is an uneven number of players and a coach or multiple coaches are entered in as players, the program will prioritize placing the coaches into the singles matches or have a coach play 1 v 2 if the numbers require it. This ensures that most players will be able to play doubles. The coaches currently stored in the program are Aidan, Tommy, and Norbu.
