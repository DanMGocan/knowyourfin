from flask import Blueprint, jsonify, request
from models import SimulationSettings

# Create a blueprint
create_population_bp = Blueprint('create_population', __name__)

@create_population_bp.route('/create_population', methods=['POST'])
def create_population():
    """
    Handles creating and updating population settings for the simulation.
    Accepts data including education level, unemployment rate, and homeownership vs. mortgage dependency.
    """
    data = request.json

    # Extract and validate inputs
    education_level = data.get('education_level')
    unemployment_rate = data.get('unemployment_rate')
    homeownership_percentage = data.get('homeownership_percentage')
    mortgage_dependents_percentage = data.get('mortgage_dependents_percentage')

    # Validate percentages add up to 100%
    if homeownership_percentage + mortgage_dependents_percentage != 100:
        return jsonify({'error': 'Homeownership and mortgage percentages must sum to 100%'}), 400

    # Validate education level and unemployment rate are within bounds
    if not (0 <= education_level <= 1):
        return jsonify({'error': 'Education level must be between 0 and 1'}), 400
    if not (0 <= unemployment_rate <= 1):
        return jsonify({'error': 'Unemployment rate must be between 0 and 1'}), 400

    # Update or store simulation settings
    settings = SimulationSettings.query.first()
    if not settings:
        settings = SimulationSettings()

    settings.education_level = education_level
    settings.unemployment_rate = unemployment_rate
    settings.homeownership_percentage = homeownership_percentage
    settings.mortgage_dependents_percentage = mortgage_dependents_percentage

    db.session.add(settings)
    db.session.commit()

    return jsonify({'status': 'Population settings updated successfully'})
