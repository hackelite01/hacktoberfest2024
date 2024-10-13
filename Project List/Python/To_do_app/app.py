from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuring the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids warning
db = SQLAlchemy(app)

# TodoItem model representing a table in the database
class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<TodoItem {self.id}>'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form.get('content', '').strip()
        if content:
            new_item = TodoItem(content=content)
            db.session.add(new_item)
            db.session.commit()
        return redirect(url_for('index'))
    else:
        items = TodoItem.query.all()
        return render_template('index.html', items=items)

@app.route('/complete/<int:item_id>')
def complete(item_id):
    item = TodoItem.query.get_or_404(item_id)
    item.completed = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>')
def delete(item_id):
    item = TodoItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:item_id>', methods=['POST'])
def edit(item_id):
    item = TodoItem.query.get_or_404(item_id)
    new_content = request.form.get('content', '').strip()
    if new_content:
        item.content = new_content
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)