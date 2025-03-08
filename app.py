import mysql.connector
from mysql.connector import Error

# Function to connect to the MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',  # Update with your MySQL host
            database='csdatabase',  # Your database name
            user='root',  # Your MySQL username
            password='#dIamnd321'  # Your MySQL password
        )
        if connection.is_connected():
            print("Connected to the database")
        return connection

    except Error as e:
        print(f"Error: {e}")
        return None

# Function to look up player ID from player name
def get_player_id(connection, player_name):
    cursor = connection.cursor()
    query = """
        SELECT playerID, name
        FROM Player
        WHERE name LIKE %s;
    """
    cursor.execute(query, (f"%{player_name}%",))
    results = cursor.fetchall()

    if not results:
        print("No players found with that name.")
        return None

    # If multiple players match the name, show a list
    if len(results) > 1:
        print("\nMultiple players found:")
        for i, row in enumerate(results):
            print(f"{i + 1}. {row[1]} (ID: {row[0]})")

        choice = input("Select a player by number: ")
        try:
            player_id = results[int(choice) - 1][0]
            return player_id
        except:
            print("Invalid selection.")
            return None
    else:
        # If only one player matches, return their ID
        return results[0][0]

# Function to display player statistics
def get_player_statistics(connection, player_id):
    cursor = connection.cursor()
    query = """
        SELECT p.name, s.kills, s.deaths, s.hltvRating, s.adr, gm.dateTime
        FROM Player p
        JOIN Statistics s ON p.playerID = s.playerID
        JOIN GameMatch gm ON s.matchID = gm.matchID
        WHERE p.playerID = %s
        ORDER BY gm.dateTime DESC;
    """
    cursor.execute(query, (player_id,))
    results = cursor.fetchall()

    if not results:
        print("No statistics found for this player.")
        return

    print("\nPlayer Match Statistics:")
    print(f"{'Name':<15}{'Kills':<10}{'Deaths':<10}{'HLTV Rating':<15}{'ADR':<10}{'Match Date':<15}")
    print("-" * 75)
    for row in results:
        print(f"{row[0]:<15}{row[1]:<10}{row[2]:<10}{row[3]:<15}{row[4]:<10}{row[5]:<15}")

# Function to display aggregated statistics
def get_aggregate_statistics(connection, player_id):
    cursor = connection.cursor()
    query = """
        SELECT p.name, SUM(s.kills) AS total_kills, SUM(s.deaths) AS total_deaths,
               AVG(s.hltvRating) AS avg_hltv, AVG(s.adr) AS avg_adr
        FROM Player p
        JOIN Statistics s ON p.playerID = s.playerID
        WHERE p.playerID = %s
        GROUP BY p.name;
    """
    cursor.execute(query, (player_id,))
    result = cursor.fetchone()

    if result:
        print("\nAggregate Statistics:")
        print(f"Name: {result[0]}")
        print(f"Total Kills: {result[1]}")
        print(f"Total Deaths: {result[2]}")
        print(f"Average HLTV Rating: {round(result[3], 2)}")
        print(f"Average ADR: {round(result[4], 2)}")
    else:
        print("No aggregate data found.")

# Function to update player's HLTV rating
def update_player_rating(connection, player_id, new_rating):
    cursor = connection.cursor()
    query = """
        UPDATE Statistics
        SET hltvRating = %s
        WHERE playerID = %s;
    """
    cursor.execute(query, (new_rating, player_id))
    connection.commit()
    print("Player rating updated successfully.")

# Main function to handle user interaction
def main():
    connection = connect_to_database()
    if connection is None:
        return
    
    try:
        player_name = input("\nEnter Player Name: ")
        player_id = get_player_id(connection, player_name)

        if player_id is None:
            return
        
        print("\nOptions:")
        print("1. View Match Statistics")
        print("2. View Aggregate Statistics")
        print("3. Update HLTV Rating")

        choice = input("\nEnter your choice (1/2/3): ")

        if choice == '1':
            get_player_statistics(connection, player_id)
        elif choice == '2':
            get_aggregate_statistics(connection, player_id)
        elif choice == '3':
            new_rating = input("Enter new HLTV rating: ")
            update_player_rating(connection, player_id, new_rating)
            print("\nUpdated HLTV Rating:")
            get_aggregate_statistics(connection, player_id)
        else:
            print("Invalid choice.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            connection.close()
            print("Connection closed.")

if __name__ == "__main__":
    main()
