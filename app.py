from flask import Flask, render_template, request
from data_processing import load_pokemon_data

app = Flask(__name__)

# Load Pokémon data
df = load_pokemon_data()

@app.route('/', methods=['GET', 'POST'])
def home():
    query = request.form.get("search")  # Get search query
    filtered_pokemon = df.copy()

    if query:
        # Search Pokémon by Name or Number
        filtered_pokemon = df[
            df["Name"].str.contains(query, case=False, na=False) |
            df["#"].astype(str).str.contains(query, na=False)
        ]
    

    pokemon_list = filtered_pokemon.to_dict(orient="records")
    return render_template('index.html', pokemon=pokemon_list, query=query)

@app.route('/pokemon/<name>')
def pokemon_details(name):
    """ Route to display details of a specific Pokémon """
    selected_pokemon = df[df["Name"].str.lower() == name.lower()]  # Case-insensitive match
    
    if selected_pokemon.empty:
        return "<h2>Pokémon not found</h2>", 404  # Return 404 if not found
    
    # Convert the single Pokémon row to a dictionary
    pokemon_data = selected_pokemon.to_dict(orient="records")[0]

    return render_template('index.html', pokemon=pokemon_data)

if __name__ == '__main__':
    app.run(debug=True)
