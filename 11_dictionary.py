kohli = {
    "full_name": "Virat Kohli",
    "birth_date": "5 November 1988",
    "birth_place": "Delhi, India",
    "age": 37,
    "nationality": "Indian",
    "role": "Batsman",
    "batting_style": "Right-handed",
    "bowling_style": "Right-arm medium",
    "current_team": "India & Royal Challengers Bengaluru (RCB)",
    "odi_runs": 13848,
    "test_runs": 8848,
    "t20i_runs": 4188,
    "total_centuries": 80,
    "major_awards": "ICC Cricketer of the Decade, Padma Shri"
}
print(kohli)
print("Only keys ",kohli.keys())
print("Only values ",kohli.values())
print("key value as item ",kohli.items())
print("runs",kohli.get('odi_runs'))
print("t20 runs",kohli.get('t20_runs','info not available'))

kohli2 = kohli.copy()
print(kohli,kohli2)

#empty dictionary 
kohli2.clear()
print(kohli,kohli2)

#remove total_centuries
kohli.pop('total_centuries')

#remove last key value pair 
kohli.popitem()

print("after removing keys ",kohli)

kohli.update({'isMarried':True,'t20i_runs':9999})
print(kohli)