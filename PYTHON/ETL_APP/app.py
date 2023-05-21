from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd


# Crea una instancia de la aplicación Flask
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:1234@localhost:5433/bi_database?options=-c%20search_path=desarrollo"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Jobs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String(255))
    insert_date = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())


# Define una ruta y una función controladora
@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        seleccion =request.form['mi_combobox']
        if file:
            df = pd.read_csv(file)
            for index, row in df.iterrows():
                if seleccion == 'jobs':
                    new_row = Jobs(id=row['id'], job=row['job'])
                db.session.add(new_row)
            db.session.commit()
        return f'Archivo cargado correctamente el la tabla {seleccion}'
    return render_template('upload.html')




# Inicia el servidor de desarrollo de Flask
if __name__ == '__main__':
    app.run()


