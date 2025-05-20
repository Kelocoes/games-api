from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

pcs = [f"PC{i}" for i in range(1, 31)]

# Juegos con imágenes actualizadas y disponibilidad simulada
games = [
    {"id": 1, "title": "Cyberpunk 2077", "genre": ["Acción", "RPG"],
     "image": "https://cdn2.steamgriddb.com/thumb/4030e2eebb977639f8836aa25a293e40.jpg",
     "pcsAvailable": random.sample(pcs, 10)},
    {"id": 2, "title": "The Witcher 3: Wild Hunt", "genre": ["RPG", "Aventura"],
     "image": "https://cdn2.steamgriddb.com/thumb/4904f82c12cecf6ec070fe77d7e913ce.jpg",
     "pcsAvailable": random.sample(pcs, 11)},
    {"id": 3, "title": "Elden Ring", "genre": ["Acción", "RPG"],
     "image": "https://cdn2.steamgriddb.com/thumb/b7dc60f5a597d2a0687c2c43a3cd3417.jpg",
     "pcsAvailable": random.sample(pcs, 13)},
    {"id": 4, "title": "Starfield", "genre": ["RPG", "Simulación"],
     "image": "https://cdn2.steamgriddb.com/thumb/ac79bc4536e67368f7a054716ebdf36f.jpg",
     "pcsAvailable": random.sample(pcs, 14)},
    {"id": 5, "title": "Microsoft Flight Simulator", "genre": ["Simulación", "Estrategia"],
     "image": "https://cdn2.steamgriddb.com/thumb/49318f67c631cd59c097b51933b5df26.jpg",
     "pcsAvailable": random.sample(pcs, 12)},
    {"id": 6, "title": "Half-Life: Alyx", "genre": ["FPS", "Realidad_VR"],
     "image": "https://cdn2.steamgriddb.com/thumb/980c9d1c2752a29a8cdc5669b9e22e6f.jpg",
     "pcsAvailable": random.sample(pcs, 11)},
    {"id": 7, "title": "Valorant", "genre": ["FPS", "E-sports"],
     "image": "https://cdn2.steamgriddb.com/thumb/9edb6b9b7fc3b263b86740c635839dc4.jpg",
     "pcsAvailable": random.sample(pcs, 15)},
    {"id": 8, "title": "Fortnite", "genre": ["Acción", "Battle_Royale"],
     "image": "https://cdn2.steamgriddb.com/thumb/6c4d541fc68d426aa028bc05f38164d1.jpg",
     "pcsAvailable": random.sample(pcs, 14)},
    {"id": 9, "title": "Apex Legends", "genre": ["Acción", "Battle_Royale"],
     "image": "https://cdn2.steamgriddb.com/thumb/0d7a3aef18b1eb97e70a5148e2a2646f.jpg",
     "pcsAvailable": random.sample(pcs, 12)},
    {"id": 10, "title": "Overwatch 2", "genre": ["FPS", "E-sports"],
     "image": "https://cdn2.steamgriddb.com/thumb/f8013fd6d898ca4374d8113f0939c70c.jpg",
     "pcsAvailable": random.sample(pcs, 10)},
]

@app.route('/games', methods=['GET'])
def get_games():
    return jsonify(games)

if __name__ == '__main__':
    app.run()
