from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pickJourneyApi.db'
db = SQLAlchemy(app)

class Aventura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.Text, nullable=False)
    opcionesText =  db.Column(db.PickleType, nullable=True)

def crear_datos_iniciales():
    if Aventura.query.first() is None:
        aventura1 = Aventura(
            descripcion="Recien te despertas, te levantas sin recordar nada de lo que sucedio. Estas en el coche, sentis los vidrios en tu piel, el frio en tu cara y no entendes nada....Tu cabeza te da vueltas tratando de recordar algo pero te duele demasiado, debe ser por el golpe, estas en tu auto chocado dado vuelta!! te arrastras para salir y te encontras al costado de la ruta, en la entrada de un bosque oscuro, solo, perdido....intentas buscar tu celular pero se debe haber caido en los trompos..... solo tenes 2 opciones",
            opcionesText=["Empezar a caminar - OPT 2", "Quedarte a esperar por ayuda - OPT 3"]
        )
        aventura2 = Aventura(
            descripcion="Nunca es buena idea quedarse solo en el medio de la ruta al costado de un bosque, eso pasa en las películas de terror....salis a caminar por la ruta subiendo una colina para ver si desde arriba se llega a ver algo. Al rato ves que viene un auto a lo lejos, desesperado le haces señas, te paras en el medio de la ruta para que te vea y frene. Las luces cada vez son más intensas y cada vez se escucha mas el ruido del motor.... no esta des-acelerando!! En la desesperacion pensando que te va a chocar empezar a correr en direccion contraria, pero no hay caso, cada vez sentis mas cerca el auto....a ultimo momento decidis saltar y caes por el barranco nuevamente a la entrada del bosque. El miedo te invade y empezar a correr hacia el bosque, la adrenalina te ahce olvidar por un momento todos los golpes que tenes, dudas de auto, será ellos los que me hicieron esto? De pronto escuchas las puertas del auto cerrarse, sabes que alguien bajo a buscarte y decidis esconderte en el hueco de un arbol....De pronto empezas a escuchar auxilio, ayuda, ellos tambien me buscan a mi ayudame ...... solo tenes 2 opciones",
            opcionesText=["Confias y ayudas al extraño - OPT 4", "Desconfias y escapas aun mas dentro del bosque - OPT 5"]
        )
        aventura3 = Aventura(
            descripcion="Te quedas al costado del auto, empezas a escuchar ruidos extraños, de pronto un auto se acerca, le haces señas para que te vean y responden con luces. Al llegar, bajan 2 personas tapas y sabes que estas en problemas, intentas correr pero el frio y los golpes que tenes no te permiten mover, ellos te alcanzan, te duermen y te llevan....fue la ultima vez que se supo de ti",
            opcionesText=None
        )
        aventura4 = Aventura(
            descripcion="Decidis volver, confias que tu buen acto te ayudo a salir de esta situación, lleno de dudas salis de tu escondite y empezas a caminar por el oscuro bosque en busca de esta persona....en el camino los pensamientos te invaden, queres escapar pero no! seguis avanzando.....de pronto sentis una presion fuerte en el tobillo, es un hombre aferrandose a tu pierna que te dice gracias por volver por mi, gracias por ayudarme! Intentas subirlo a caballito y se alejan como pueden, pero no mucho, los 2 estan golpeados y cansados. Se logran esconder en unos arbustos y se quedan en silencio aunque tenes mil preguntas para hacerle. Él es el primero en hablar, la unica forma de escapar es llegar antes que ellos que nos estan buscando al auto, dudas del extraño pero sabes que es la unica oportunidad de salir de ahi, en algún momento va a salir el sol y si siguen buscandolos ya no se van a poder esconder.....comienzan a caminar hacia la luces del auto, a medido que se van acercando la luz se hace mas fuerte, al llegar la 1er buena noticia, el auto esta vacio y andando....te dispones a subir del lado del conductor pero escuchas un ruido viniendo detras tuyo.....el extraño que rengueando esta pasando por delante del auto y te grita DALE FEDE RAPIDO ARRANCA!!!.....como sabe mi nombre?!?!?! volteas instintivamente a verlo y apoyado en el capo del auto ves como le cambia la cara, el pànico se apodera de vos, CAI EN SU TRAMPA! rapidamente te subis al auto y arrancas, el extraño se tira a un costado y ves por el espejo como empieza a correr detras tuyo mientra cada vez su silueta se hace mas chica....abris la guantera para buscar un celular pero en su lugar encontras una nota.....CONTINUARA",
            opcionesText=None
        )
        aventura5 = Aventura(
            descripcion="No confias ni por un segundo para volver por esa persona, en su lugar salis corriendo hacia el auto para llegar antes que él y poder escapar......mala idea, al llegar al auto hay 2 personas esperandote, tal vez el extraño decia la verdad pero ya es muy tarde......no tenes escapatoria",
            opcionesText=None
        )

        db.session.add_all([aventura1, aventura2, aventura3, aventura4, aventura5])
        db.session.commit()
        
story_post_args = reqparse.RequestParser()
story_post_args.add_argument('option', type=int, help='Option to chose is required', required=True)

class Start(Resource):
    def post(self):
        start = Aventura.query.filter_by(id=1).first()
        starting_point={
            'story': start.descripcion,
            'choose': start.opcionesText,
        }
        return starting_point

class Choose(Resource):
    def post(self):
        args = story_post_args.parse_args()
        choose = Aventura.query.filter_by(id=args['option']).first()
        you_choose={
            'story': choose.descripcion,
        }
        if args['option'] == 2:
            you_choose['choose'] = choose.opcionesText
        return you_choose
            
api.add_resource(Start, '/start')
api.add_resource(Choose, '/choose')
        
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Base de datos creada")
        crear_datos_iniciales()
        print("Datos iniciales creados")

    app.run(debug=True)