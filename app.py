from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define database model
class StudyGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    members = db.Column(db.String(500), default="")  # list of member names

    def __repr__(self):
        return f'<StudyGroup {self.group_name}>'

    def get_members(self):
        return [m.strip() for m in self.members.split(',') if m.strip()]


# Home route — list all groups
@app.route('/')
def index():
    groups = StudyGroup.query.all()
    return render_template('index.html', groups=groups)

# Add group route
@app.route('/add', methods=['GET', 'POST'])
def add_group():
    if request.method == 'POST':
        name = request.form['group_name']
        subject = request.form['subject']
        description = request.form['description']

        new_group = StudyGroup(group_name=name, subject=subject, description=description)
        db.session.add(new_group)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add_group.html')

# Edit group route
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_group(id):
    group = StudyGroup.query.get_or_404(id)

    if request.method == 'POST':
        group.group_name = request.form['group_name']
        group.subject = request.form['subject']
        group.description = request.form['description']
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit_group.html', group=group)

# Delete group route
@app.route('/delete/<int:id>')
def delete_group(id):
    group = StudyGroup.query.get_or_404(id)
    db.session.delete(group)
    db.session.commit()
    return redirect(url_for('index'))

# Join group route
@app.route('/join/<int:id>', methods=['POST'])
def join_group(id):
    username = request.form.get('username', 'Anonymous')  # Simulated user
    group = StudyGroup.query.get_or_404(id)

    members = group.get_members()
    if username not in members:
        members.append(username)
        group.members = ', '.join(members)
        db.session.commit()

    return redirect(url_for('index'))

# Leave group route
@app.route('/leave/<int:id>', methods=['POST'])
def leave_group(id):
    username = request.form.get('username', 'Anonymous')
    group = StudyGroup.query.get_or_404(id)

    members = group.get_members()
    if username in members:
        members.remove(username)
        group.members = ', '.join(members)
        db.session.commit()

    return redirect(url_for('index'))


# Run app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
