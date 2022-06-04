CREATE DATABASE mlb;


-- Imported CSV files from web as tables using MySQL import wizard -- 

-- Confirming/ previewing tables created -- 


SELECT * 
FROM mlb.players -- basic MLB player info --
LIMIT 10;

SELECT * 
FROM mlb.atbats -- 2018 season statistcal counts for per player
LIMIT 10;

SELECT * 
FROM mlb.teams -- basic team information from 2018 season
LIMIT 10;

-- What was the highest win total?

SELECT MAX(W)
FROM mlb.teams;

-- What were the 5 winningest teams in the National League

SELECT teamID, W
FROM mlb.teams 
WHERE lgID = 'NL'
ORDER BY W DESC
LIMIT 5;

-- Did the American League or National League combine for more wins?

SELECT lgID, SUM(W)
FROM mlb.teams
GROUP BY lgID;

-- The players table doesnt include team. Let's create a modified table to add it

USE mlb;

CREATE TABLE players_new AS
SELECT p.*, a.team
FROM players AS p, atbats AS a
WHERE p.name = a.name;

-- What is the average strikout rate among qualified hitters?

SELECT AVG(SO/AB) as avg_k_rate
FROM mlb.atbats
WHERE AB > 200;

-- How does each player's strikeout rate compare to league average?

SELECT 
	name,
    ROUND((SO/AB),2) as k_rate,
    (SELECT ROUND(AVG(SO/AB), 2) as avg_k_rate
		FROM mlb.atbats
		WHERE AB > 200) AS League_avg_k_rate,
	ROUND((SO/AB)- (SELECT AVG(SO/AB) 
		FROM mlb.atbats
		WHERE AB > 200), 2) AS diff 
FROM mlb.atbats
WHERE AB > 200 
ORDER BY K_rate ASC;

-- Creating a view of players table for just international (Non-US) players

Create View intl_players AS
(SELECT a.*, p.birthCountry
FROM atbats as a
LEFT JOIN players as p
ON a.name = p.name
WHERE birthCountry NOT IN ('USA'));

-- Getting a running average of stolen bases per player, sorted by team

SELECT 
	name,
    team,
    SB,
    AVG(SB) OVER(partition by team) AS running_avg
FROM atbats
;
    
-- Did stolen bases correlate to more wins? This compares where each team ranks for both stolen bases and wins

SELECT 
	teamID,
    SB,
    W,
    RANK () OVER (order by SB DESC) as SB_rank,
    RANK () OVER (order by W DESC) as W_rank
FROM teams
ORDER BY SB_rank;


-- creating a list of just rookiw players using a CTE

WITH Rookie_players AS
(SELECT  name, team, height, weight, birthyear, EXTRACT(YEAR FROM debut) AS year
FROM players_new)

SELECT *
FROM Rookie_players
WHERE year = '2018'



    
    
    



    






    
 









