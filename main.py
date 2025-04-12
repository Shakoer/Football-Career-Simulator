import random

# ANSI escape codes for colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

# clubs
clubs = [
    {"name": "Real Madrid", "country": "Spain", "league": "La Liga", "division": 1, "rating": 93, "trophy_weight": 0.95},
    {"name": "Barcelona", "country": "Spain", "league": "La Liga", "division": 1, "rating": 88, "trophy_weight": 0.9},
    {"name": "Bayern Munich", "country": "Germany", "league": "Bundesliga", "division": 1, "rating": 92, "trophy_weight": 0.9},
    {"name": "Manchester City", "country": "England", "league": "Premier League", "division": 1, "rating": 89, "trophy_weight": 0.9},
    {"name": "Liverpool", "country": "England", "league": "Premier League", "division": 1, "rating": 88, "trophy_weight": 0.85},
    {"name": "Paris Saint-Germain", "country": "France", "league": "Ligue 1", "division": 1, "rating": 91, "trophy_weight": 0.9},
    {"name": "Juventus", "country": "Italy", "league": "Serie A", "division": 1, "rating": 87, "trophy_weight": 0.85},
    {"name": "Chelsea", "country": "England", "league": "Premier League", "division": 1, "rating": 85, "trophy_weight": 0.8},
    {"name": "Boca Juniors", "country": "Argentina", "league": "Primera División", "division": 1, "rating": 83, "trophy_weight": 0.75},
    {"name": "Flamengo", "country": "Brazil", "league": "Campeonato Brasileiro", "division": 1, "rating": 84, "trophy_weight": 0.8},
    {"name": "Arsenal", "country": "England", "league": "Premier League", "division": 1, "rating": 82, "trophy_weight": 0.7},
    {"name": "Atletico Madrid", "country": "Spain", "league": "La Liga", "division": 1, "rating": 85, "trophy_weight": 0.8},
    {"name": "Inter Milan", "country": "Italy", "league": "Serie A", "division": 1, "rating": 83, "trophy_weight": 0.75},
    {"name": "Napoli", "country": "Italy", "league": "Serie A", "division": 1, "rating": 80, "trophy_weight": 0.7},
    {"name": "Leicester City", "country": "England", "league": "Premier League", "division": 1, "rating": 78, "trophy_weight": 0.65},
    {"name": "Sevilla FC", "country": "Spain", "league": "La Liga", "division": 1, "rating": 79, "trophy_weight": 0.7},
    {"name": "Porto", "country": "Portugal", "league": "Primeira Liga", "division": 1, "rating": 81, "trophy_weight": 0.75},
    {"name": "West Ham United", "country": "England", "league": "Premier League", "division": 1, "rating": 77, "trophy_weight": 0.6},
    {"name": "Real Sociedad", "country": "Spain", "league": "La Liga", "division": 1, "rating": 76, "trophy_weight": 0.6},
    {"name": "Real Betiz", "country": "Spain", "league": "La Liga", "division": 1, "rating": 79, "trophy_weight": 0.65},
    {"name": "Monaco", "country": "France", "league": "League 1", "division": 1, "rating": 79, "trophy_weight": 0.65},
    {"name": "Marsaille", "country": "France", "league": "League 1", "division": 1, "rating": 78, "trophy_weight": 0.6},
    {"name": "Burnley", "country": "England", "league": "Premier League", "division": 1, "rating": 70, "trophy_weight": 0.4},
    {"name": "Alaves", "country": "Spain", "league": "La Liga", "division": 1, "rating": 69, "trophy_weight": 0.35},
    {"name": "Leganes", "country": "Spain", "league": "La Liga", "division": 1, "rating": 68, "trophy_weight": 0.3},
    {"name": "Huesca", "country": "Spain", "league": "La Liga", "division": 1, "rating": 65, "trophy_weight": 0.2},
    {"name": "Espanyol", "country": "Spain", "league": "Segunda", "division": 2, "rating": 68, "trophy_weight": 0.1},
    {"name": "Stoke City", "country": "England", "league": "Championship", "division": 2, "rating": 67, "trophy_weight": 0.2},
    {"name": "Celtic FC", "country": "Scotland", "league": "Scottish Premiership", "division": 1, "rating": 75, "trophy_weight": 0.65},
    {"name": "Maritimo", "country": "Portugal", "league": "Primeira Liga", "division": 1, "rating": 63, "trophy_weight": 0.15},
    {"name": "Hertha BSC", "country": "Germany", "league": "Bundesliga", "division": 1, "rating": 70, "trophy_weight": 0.25},
    {"name": "Como", "country": "Italy", "league": "Serie A", "division": 1, "rating": 75, "trophy_weight": 0.05},
    {"name": "Saint-Ettiene", "country": "France", "league": "League 1", "division": 1, "rating": 68, "trophy_weight": 0.1},
    {"name": "Pendikspor", "country": "Turkey", "league": "1. Lig", "division": 2, "rating": 65, "trophy_weight": 0.05},
    {"name": "St. Pauli", "country": "Germany", "league": "2. Bundesliga", "division": 2, "rating": 70, "trophy_weight": 0.05},
    {"name": "Getafe", "country": "Spain", "league": "La Liga", "division": 1, "rating": 62, "trophy_weight": 0.1},
    {"name": "Al Hilal FC", "country": "Saudi Arabia", "league": "Saudi Pro League", "division": 1, "rating": 78, "trophy_weight": 0.6},
    {"name": "Legia Warsaw", "country": "Poland", "league": "Ekstraklasa", "division": 1, "rating": 71, "trophy_weight": 0.3},
    {"name": "Bournemouth", "country": "England", "league": "Championship", "division": 2, "rating": 68, "trophy_weight": 0.2},
    {"name": "Alaves", "country": "Spain", "league": "La Liga", "division": 1, "rating": 64, "trophy_weight": 0.1},
    {"name": "Mamelodi Sundowms", "country": "South Africa", "league": "DSTV Premiership", "division": 1, "rating": 72, "trophy_weight": 0.7},
    {"name": "Kaizer Chiefs", "country": "South Africa", "league": "DSTV Premiership", "division": 1, "rating": 69, "trophy_weight": 0.2},
    {"name": "Orlando Pirates", "country": "South Africa", "league": "DSTV Premiership", "division": 1, "rating": 70, "trophy_weight": 0.4},
    {"name": "Troye", "country": "France", "league": "League 2", "division": 2, "rating": 65, "trophy_weight": 0.05},
]

# positions
position_stats = {
    "ST": {"goals": (15, 45), "assists": (2, 10)},
    "LW/RW": {"goals": (10, 35), "assists": (5, 15)},
    "CAM": {"goals": (10, 20), "assists": (10, 20)},
    "CM": {"goals": (3, 10), "assists": (5, 15)},
    "DM": {"goals": (1, 5), "assists": (3, 10)},
    "LB/RB": {"goals": (0, 5), "assists": (3, 10)},
    "CB": {"goals": (0, 5), "assists": (0, 3), "clean_sheets": (10, 20)},
    "GK": {"goals": (0, 0), "assists": (0, 1), "clean_sheets": (10, 25)}
}

positions = list(position_stats.keys())
traits = ["Dribbling", "Shooting", "Passing", "Set Pieces", "Stamina", "Vision", "Tackling", "Reflexes"]
growth_options = ["Balanced Growth", "Focus on Shooting", "Focus on Pace", "Focus on Defense", "Focus on Passing"]

# Player Creation
print(f"{CYAN}Choose a position:{RESET}")
for i, pos in enumerate(positions):
    print(f"{i + 1}. {pos}")
position = positions[int(input("Position number: ")) - 1]

print(f"\n{CYAN}Choose your main trait:{RESET}")
for i, tr in enumerate(traits):
    print(f"{i + 1}. {tr}")
trait = traits[int(input("Trait number: ")) - 1]

player = {
    "name": input("Enter your player's name: "),
    "age": 16,
    "nationality": input("Enter your nationality: "),
    "position": position,
    "strengths": trait,
    "club": None,
    "rating": 60,
    "transfer_value": 50000,
    "career_stats": [],
    "total_goals": 0,
    "total_assists": 0,
    "total_matches": 0,
    "total_clean_sheets": 0,
    "trophies": [],
    "awards": [],
    "Ballon Dor": 0,
    "best_season": {},
    "international_caps": 0,
    "international_goals": 0,
    "world_cup_wins": 0,
    "clubs_played": [],
    "sponsorship": None,
}

# Initial club assignment
matching_clubs = [club for club in clubs if club["country"].lower() == player["nationality"].lower()]
player["club"] = random.choice(matching_clubs if matching_clubs else clubs)
player["clubs_played"].append(player["club"]["name"])

# Main
while player["age"] < 39:
    print(f"\n{YELLOW}--- Age {player['age']} Season at {player['club']['name']} ---{RESET}")
    
    # Stat generation
    stats_range = position_stats[player["position"]]
    matches = random.randint(20, 38)
    multiplier = min(1.0, player["rating"] / 100)
    if player["age"] <= 18:
        multiplier *= 0.7
    elif player["age"] >= 32:
        multiplier *= 0.85

    goals = int(random.randint(*stats_range.get("goals", (0, 0))) * multiplier)
    assists = int(random.randint(*stats_range.get("assists", (0, 0))) * multiplier)
    clean_sheets = int(random.randint(*stats_range.get("clean_sheets", (0, 0))) * multiplier) if "clean_sheets" in stats_range else 0

    # Growth
    print(f"\n{CYAN}Choose how to develop this season:{RESET}")
    for i, g in enumerate(growth_options):
        print(f"{i + 1}. {g}")
    growth_choice = int(input("Growth choice: "))
    growth = growth_options[growth_choice - 1]

    if growth == "Balanced Growth":
        growth_factor = 1.0
    elif "Shooting" in growth and "ST" in position:
        growth_factor = 1.3
    elif "Defense" in growth and position in ["CB", "LB/RB", "DM"]:
        growth_factor = 1.3
    elif "Passing" in growth and position in ["CM", "CAM", "DM"]:
        growth_factor = 1.3
    elif "Pace" in growth and position in ["LW/RW", "LB/RB", "ST"]:
        growth_factor = 1.2
    else:
        growth_factor = 0.9

    # Update player stats
    player["career_stats"].append({
        "age": player["age"],
        "club": player["club"]["name"],
        "goals": goals,
        "assists": assists,
        "clean_sheets": clean_sheets,
        "matches": matches
    })
    player["total_goals"] += goals
    player["total_assists"] += assists
    player["total_clean_sheets"] += clean_sheets
    player["total_matches"] += matches

    if not player["best_season"] or goals + assists > player["best_season"].get("impact", 0):
        player["best_season"] = {"age": player["age"], "goals": goals, "assists": assists, "impact": goals + assists}

    player["rating"] = min(100, player["rating"] + (goals * 0.3 + assists * 0.15 + clean_sheets * 0.2) * growth_factor)
    player["transfer_value"] = int(player["rating"] * 1000)

    print(f"Player Rating: {player['rating']:.2f} | Club Rating: {player['club']['rating']} | Player Value: ${player['transfer_value']}")

    # Trophies
    chance = player["club"]["rating"] * player["club"]["trophy_weight"] / 100
    if random.random() < chance:
        for _ in range(random.randint(1, 3)):
            trophy = random.choice(["League Title", "Cup", "Continental Trophy"])
            player["trophies"].append(f"{trophy} ({player['age']})")
            print(f"{GREEN}>>> Won {trophy}!{RESET}")
    if player["rating"] > 80 and player["sponsorship"] is None:
      if random.random() < 0.7:
          deal = random.choice(["Nike", "Adidas", "Puma", "New Balance"])
          player["sponsorship"] = deal
          print(f"{GREEN}Signed a sponsorship deal with {deal}!")

    # Awards
    if goals >= 25:
        player["awards"].append(f"Golden Boot ({player['age']})")
        print(f"{YELLOW}>>> Won Golden Boot!{RESET}")
    elif goals + assists >= matches:
        award = random.choice(["Player of the Year", "Player of the Season"])
        player["awards"].append(f"{award} ({player['age']})")
        print(f"{YELLOW}>>> Won {award}!{RESET}")

    if player["rating"] >= 90:
      if player["rating"] < 95:
        chance = 0.10
      elif player["rating"] < 100:
        chance = 0.20
      else:  # rating == 100
        chance = 0.30
      if random.random() < chance:
          print(f"{YELLOW}>>> Won Ballon D'or!!!")
          player["Ballon Dor"] += 1

    # National Team
    if player["rating"] >= 80 and random.random() < 0.5:
        print(f"{CYAN}>>> Called up to national team!{RESET}")
        intl_matches = random.randint(2, 8)
        intl_goals = random.randint(0, 4)
        player["international_caps"] += intl_matches
        player["international_goals"] += intl_goals
        if player["age"] % 4 == 0 and random.random() < 0.3:
            player["world_cup_wins"] += 1
            print(f"{GREEN}>>> Won World Cup!{RESET}")

    print(f"Season Stats: {matches} matches | {goals} goals | {assists} assists | {clean_sheets} clean sheets")

    # End of season choice
    print("\nDo you want to:")
    print(f"{CYAN}1. Stay at current club{RESET}")
    print(f"{CYAN}2. Retire{RESET}")
    print(f"{CYAN}3. View transfer offers{RESET}")
    choice = input("Choose an action: ")

    if choice == "2":
        break
    elif choice == "3":
        performance_score = (goals + assists + clean_sheets) / max(1, matches)
        max_rating = min(99, int(player["rating"] + performance_score * 10))
        offers = [club for club in clubs if club["rating"] >= player["club"]["rating"] and club["rating"] <= max_rating]
        if offers:
            print(f"{CYAN}Transfer offers:{RESET}")
            for i, offer in enumerate(offers):
                print(f"{BLUE}{i + 1}. {offer['name']} ({offer['league']}) - Rating {offer['rating']}{RESET}")
            offer_choice = int(input("Accept which offer? (0 to stay): "))
            if offer_choice > 0 and offer_choice <= len(offers):
                player["club"] = offers[offer_choice - 1]
                
        if player["club"]["name"] not in player["clubs_played"]:
          player["clubs_played"].append(player["club"]["name"])

    player["age"] += 1

# Career Summary
print(f"\n{MAGENTA}--- Career Summary for {player['name']} ---{RESET}")
print(f"{CYAN}Total Matches:{RESET} {player['total_matches']}")
print(f"{CYAN}Total Goals:{RESET} {player['total_goals']}")
print(f"{CYAN}Total Assists:{RESET} {player['total_assists']}")
print(f"{CYAN}Clean Sheets:{RESET} {player['total_clean_sheets']}")
print(f"{CYAN}Best Season:{RESET} Age {player['best_season']['age']} - {player['best_season']['goals']} goals, {player['best_season']['assists']} assists")
print(f"{CYAN}Trophies Won:{RESET} {len(player['trophies'])} ({', '.join(player['trophies'])})")
print(f"{CYAN}Awards:{RESET} {', '.join(player['awards'])}")
print(f"{CYAN}International Caps:{RESET} {player['international_caps']}, {CYAN}Goals:{RESET} {player['international_goals']}")
print(f"{CYAN}Ballon D'ors won:{RESET} {player['Ballon Dor']}")
print(f"{CYAN}World Cups Won:{RESET} {player['world_cup_wins']}")
print(f"\n{CYAN}Clubs Played For:{RESET} {', '.join(player['clubs_played'])}")
