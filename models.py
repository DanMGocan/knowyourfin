from flask_sqlalchemy import SQLAlchemy

# Initialize the database instance
db = SQLAlchemy()

# Models
class SimulationSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inflation_rate = db.Column(db.Float, default=0.02)
    min_wage = db.Column(db.Float, default=15.0)
    ebc_rate = db.Column(db.Float, default=0.01)
    education_level = db.Column(db.Float, default=0.5)
    unemployment_rate = db.Column(db.Float, default=0.05)
    homeownership_percentage = db.Column(db.Float, default=50.0)
    mortgage_dependents_percentage = db.Column(db.Float, default=50.0)

class Household(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    budget = db.Column(db.Float, default=1000.0)
    income = db.Column(db.Float, default=50.0)
    spending = db.Column(db.Float, default=30.0)
