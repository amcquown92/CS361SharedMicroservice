"""
microservice.py
---------------
This module implements a Flask microservice for processing user data 
and determining achievements based on game attributes.
Endpoints: - /process (POST): Processes user data and returns updated data with achievements.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)


def determine_achievements(user):
    """
    Determines new achievements for a user based on their games' attributes.
    Args: user (dict): Dictionary containing user and game details.
    Returns: list: List of achievements earned by the user.
    """
    achievements = []

    # Gear Master
    if any(game['attributes']['type'] == 'gear' for game in user['games']):
        achievements.append("Gear Master")

    # Button Fanatic
    if any(game['attributes']['type'] == 'button' for game in user['games']):
        achievements.append("Button Fanatic")

    # Wheel Whiz
    if any(game['attributes']['type'] == 'wheel' for game in user['games']):
        achievements.append("Wheel Whiz")

    # High Functionality Hero
    if all(game['attributes']['functionality'] == 'high' for game in user['games']):
        achievements.append("High Functionality Hero")

    # Quiet Comfort
    if all(not game['attributes']['sound'] for game in user['games']):
        achievements.append("Quiet Comfort")

    # Grey Collector
    if all(game['attributes']['color'] == 'grey' for game in user['games']):
        achievements.append("Grey Collector")

    # Colorful Connoisseur
    if all(game['attributes']['color'] == 'colorful' for game in user['games']):
        achievements.append("Colorful Connoisseur")

    # Vibration Lover
    if sum(game['attributes']['vibration'] for game in user['games']) > len(user['games']) // 2:
        achievements.append("Vibration Lover")

    # Sound Enthusiast
    if any(game['attributes']['sound'] for game in user['games']):
        achievements.append("Sound Enthusiast")

    # Minimalist Gamer
    if all(game['attributes']['functionality'] == 'low' for game in user['games']):
        achievements.append("Minimalist Gamer")

    # Threepeat
    if len(user['games']) >= 3:
        achievements.append("Threepeat")

    return list(set(achievements))  # Remove duplicate achievements


@app.route('/process', methods=['POST'])
def process_user_data():
    """
    Processes user data sent via POST request, determines achievements, 
    and returns updated user data in the specified format.
    Returns: Response: JSON response containing updated user data.
    """
    users = request.json  # Parse input JSON data
    updated_users = []

    for user in users:
        user["achievements"] = determine_achievements(user)  # Add achievements
        updated_users.append(user)

    return jsonify(updated_users)  # Return updated data as JSON


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Start the microservice
