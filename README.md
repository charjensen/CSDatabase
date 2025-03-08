# 🎯 Esports Player Performance Tracker

This project is a **Python-based application** that connects to a **MySQL database** using the **MySQL Connector**. It allows users to analyze and update player performance data from an esports tournament database.

---

## 🚀 **Project Overview**
The application is designed to track and analyze player statistics in competitive esports matches. It allows users to:

✅ Search for players by **name**  
✅ View detailed **match statistics** for individual players  
✅ View **aggregate performance statistics** for a player across all matches  
✅ **Update player statistics** (like HLTV rating) directly from the app  

The project uses Python to handle user input, connect to the database, and execute multiple SQL queries to retrieve, aggregate, and modify data.

---

## 🔍 **How It Works**
### 1. **Search for Players by Name**
- The app allows the user to input a player’s name (partial or full).  
- If multiple players match the name, the app presents a list of options to select from.  

### 2. **View Match Statistics**
- Displays detailed match statistics for the selected player, including:  
  - Kills  
  - Deaths  
  - HLTV Rating  
  - ADR (Average Damage per Round)  
  - Match Date  

### 3. **View Aggregate Statistics**
- Calculates and displays aggregate statistics for the player:  
  - Total kills  
  - Total deaths  
  - Average HLTV rating  
  - Average ADR  

### 4. **Update Player’s HLTV Rating**
- The user can update a player’s HLTV rating.  
- The app commits the changes to the database and reflects the updated values in real-time.  

---

## 🏗️ **Project Structure**
```
├── app.py     # Main Python application
├── README.md            # Project description
```

---

## 💾 **Setup Instructions**
### **1. Install Dependencies**
Make sure Python and the MySQL Connector are installed:
```bash
pip install mysql-connector-python
```

### **2. Configure Database Connection**
Update the database connection settings in `app.py`:
```python
connection = mysql.connector.connect(
    host='localhost',
    database='csdatabase',
    user='your_username',
    password='your_password'
)
```

### **3. Run the Application**
To launch the app, use:
```bash
python app.py
```

---

## 🌟 **Example Usage**
**Search for a player:**
```bash
Enter Player Name: John
```

**Example Output (multiple players):**
```
👥 Multiple players found:
1. JohnDoe (ID: 101)
2. JohnSmith (ID: 102)
Select a player by number: 1
```

**Example Output (match statistics):**
```
📊 Player Match Statistics:
Name           Kills     Deaths    HLTV Rating    ADR       Match Date
---------------------------------------------------------------------
JohnDoe        25        12        1.23           85.4      2023-10-05
JohnDoe        18        7         1.10           80.1      2023-09-12
```

**Example Output (update stats):**
```
Enter new HLTV rating: 1.45
✅ Player rating updated successfully.
➡️ Updated HLTV Rating:
Name: JohnDoe
Total Kills: 43
Total Deaths: 21
Average HLTV Rating: 1.35
Average ADR: 82.75
```

---

## 📂 **SQL Queries Used**
The application executes the following SQL operations:
✅ `SELECT` – To retrieve player and match data  
✅ `JOIN` – To combine data from multiple tables  
✅ `SUM()` and `AVG()` – To compute aggregate statistics  
✅ `UPDATE` – To modify player stats  

---

## ✅ **Why This Project Matters**
This project demonstrates:
- Effective use of Python and MySQL Connector.  
- Efficient data handling using `JOIN` and `AGGREGATE` functions.  
- Real-time modification of data in a relational database.  
- A practical use case for esports data analysis and reporting.  

---

