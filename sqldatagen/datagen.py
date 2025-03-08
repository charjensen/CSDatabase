import random
import datetime

NUM_PLAYERS = 10000
NUM_TEAMS = 500
NUM_TOURNAMENTS = 100
NUM_MATCHES = 5000
NUM_STATS = 20000
NUM_RELATIONS = 15000

# Helper function to generate random dates
def random_date(start_year=2012, end_year=2025):
    start_date = datetime.date(start_year, 1, 1)
    end_date = datetime.date(end_year, 12, 31)
    delta = end_date - start_date
    return str(start_date + datetime.timedelta(days=random.randint(0, delta.days)))

# File paths for MySQL Uploads directory
UPLOAD_DIR = "C:/ProgramData/MySQL/MySQL Server 9.1/Uploads/"

# Unique ID sets to prevent duplicates
used_players = set()
used_teams = set()
used_tournaments = set()
used_matches = set()

# Generate Player Data
with open(UPLOAD_DIR + "players.csv", "w") as f:
    for i in range(1, NUM_PLAYERS + 1):
        f.write(f"{i},Player{i},{random.choice(['USA', 'Canada', 'Germany', 'UK', 'France'])},"
                f"{random.choice(['AWPer', 'Rifler', 'Support', 'Entry Fragger'])},{random.randint(16, 35)}\n")
        used_players.add(i)  # Track used IDs

# Generate Team Data
with open(UPLOAD_DIR + "teams.csv", "w") as f:
    for i in range(1, NUM_TEAMS + 1):
        f.write(f"{i},Team{i},{random.choice(['NA', 'EU', 'Asia', 'South America'])},{random.randint(1, 500)}\n")
        used_teams.add(i)

# Generate Tournament Data
with open(UPLOAD_DIR + "tournaments.csv", "w") as f:
    for i in range(1, NUM_TOURNAMENTS + 1):
        f.write(f"{i},Tournament{i},{random.choice(['USA', 'Germany', 'France'])},{random.randint(10000, 1000000)}\n")
        used_tournaments.add(i)

# Generate Match Data
with open(UPLOAD_DIR + "matches.csv", "w") as f:
    for i in range(1, NUM_MATCHES + 1):
        winner_team_id = random.choice(list(used_teams))
        f.write(f"{i},{random_date()},{winner_team_id},{random.randint(1, 3)}-{random.randint(0, 2)}\n")
        used_matches.add(i)

# Generate Statistics Data
with open(UPLOAD_DIR + "statistics.csv", "w") as f:
    for i in range(1, NUM_STATS + 1):
        f.write(f"{i},{random.choice(list(used_players))},{random.choice(list(used_matches))},"
                f"{random.randint(0, 40)},{random.randint(0, 40)},{round(random.uniform(0.5, 1.5), 2)},"
                f"{round(random.uniform(50, 120), 2)}\n")

# Generate has_player
with open(UPLOAD_DIR + "has_player.csv", "w") as f:
    unique_relations = set()
    while len(unique_relations) < NUM_RELATIONS:
        team_id = random.choice(list(used_teams))
        player_id = random.choice(list(used_players))
        relation = (team_id, player_id)
        if relation not in unique_relations:
            f.write(f"{team_id},{player_id}\n")
            unique_relations.add(relation)

# Generate invited_to
with open(UPLOAD_DIR + "invited_to.csv", "w") as f:
    unique_relations.clear()
    while len(unique_relations) < NUM_RELATIONS:
        team_id = random.choice(list(used_teams))
        tournament_id = random.choice(list(used_tournaments))
        relation = (team_id, tournament_id)
        if relation not in unique_relations:
            f.write(f"{team_id},{tournament_id}\n")
            unique_relations.add(relation)

# Generate competes_in
with open(UPLOAD_DIR + "competes_in.csv", "w") as f:
    unique_relations.clear()
    while len(unique_relations) < NUM_RELATIONS:
        player_id = random.choice(list(used_players))
        tournament_id = random.choice(list(used_tournaments))
        relation = (player_id, tournament_id)
        if relation not in unique_relations:
            f.write(f"{player_id},{tournament_id}\n")
            unique_relations.add(relation)

# Generate participates_in
with open(UPLOAD_DIR + "participates_in.csv", "w") as f:
    unique_relations.clear()
    while len(unique_relations) < NUM_RELATIONS:
        team_id = random.choice(list(used_teams))
        match_id = random.choice(list(used_matches))
        relation = (team_id, match_id)
        if relation not in unique_relations:
            f.write(f"{team_id},{match_id}\n")
            unique_relations.add(relation)

# Generate contains 
with open(UPLOAD_DIR + "contains.csv", "w") as f:
    unique_relations.clear()
    while len(unique_relations) < NUM_RELATIONS:
        tournament_id = random.choice(list(used_tournaments))
        match_id = random.choice(list(used_matches))
        relation = (tournament_id, match_id)
        if relation not in unique_relations:
            f.write(f"{tournament_id},{match_id}\n")
            unique_relations.add(relation)

# Generate achieves
with open(UPLOAD_DIR + "achieves.csv", "w") as f:
    unique_relations.clear()
    while len(unique_relations) < NUM_RELATIONS:
        player_id = random.choice(list(used_players))
        stat_id = random.randint(1, NUM_STATS)
        match_id = random.choice(list(used_matches))
        relation = (player_id, stat_id, match_id)
        if relation not in unique_relations:
            f.write(f"{player_id},{stat_id},{match_id}\n")
            unique_relations.add(relation)

# Generate generates
with open(UPLOAD_DIR + "generates.csv", "w") as f:
    unique_relations.clear()
    while len(unique_relations) < NUM_RELATIONS:
        match_id = random.choice(list(used_matches))
        stat_id = random.randint(1, NUM_STATS)
        player_id = random.choice(list(used_players))
        relation = (match_id, stat_id, player_id)
        if relation not in unique_relations:
            f.write(f"{match_id},{stat_id},{player_id}\n")
            unique_relations.add(relation)
