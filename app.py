from flask import Flask, render_template, request
from data_processing import load_pokemon_data

app = Flask(__name__)

# Load Pokémon data once when the app starts
df = load_pokemon_data()

@app.route('/', methods=['GET', 'POST'])
def home():
    query = request.form.get("search")
    
    # If query is provided, filter by Pokémon name or number (as string)
    if query:
        filtered_pokemon = df[
            df["Name"].str.contains(query, case=False, na=False) |
            df["#"].astype(str).str.contains(query, na=False)
        ]
    else:
        filtered_pokemon = df.copy()  # Show all Pokémon if no search query
    
    pokemon_list = filtered_pokemon.to_dict(orient="records")
    return render_template('index.html', pokemon=pokemon_list, query=query)

if __name__ == '__main__':
    app.run(debug=True)
