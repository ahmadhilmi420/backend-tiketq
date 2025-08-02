from flask import Flask,request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# Ensure the instance folder exists
if not os.path.exists("instance"):
    os.makedirs("instance")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(os.getcwd(), 'instance','ticket.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eventName = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    time = db.Column(db.String(50), nullable=False)
    isUsed = db.Column(db.Boolean, default=False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "eventName": self.eventName,
            "location": self.location,
            "time": self.time,
            "isUsed": self.isUsed
        }
        
# Create database tables
with app.app_context():
    db.create_all()

@app.route('/tickets', methods=['GET'])
def index():
    """Return a list of all tickets."""
    ticket = Ticket.query.all()
    if not ticket:
        return jsonify({"message": "No tickets found"}), 404
    return jsonify([t.to_dict() for t in ticket]), 200


@app.route('/tickets', methods=['POST'])
def create_ticket():
    data = request.get_json()
    new_ticket = Ticket(
        id=data.get('id'),
        eventName=data['eventName'],
        location=data['location'],
        time=data['time'],
        isUsed=data.get('isUsed', False)
    )
    db.session.add(new_ticket)
    db.session.commit()
    return jsonify(new_ticket.to_dict()), 201

@app.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    return jsonify(ticket.to_dict())

@app.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    data = request.get_json()
    ticket = Ticket.query.get_or_404(ticket_id)
    ticket.eventName = data['eventName']
    ticket.location = data['location']
    ticket.time = data['time']
    ticket.isUsed = data.get('isUsed', ticket.isUsed)
    db.session.commit()
    return jsonify(ticket.to_dict())

@app.route('/tickets/<int:ticket_id>', methods=['PATCH'])
def patch_ticket(ticket_id):
    data = request.get_json()
    ticket = Ticket.query.get_or_404(ticket_id)
    if 'isUsed' in data:
        ticket.isUsed = data['isUsed']
    db.session.commit()
    return jsonify(ticket.to_dict())

@app.route('/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    db.session.delete(ticket)
    db.session.commit()
    return jsonify({"message": "Ticket deleted successfully"}), 204

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)
    


