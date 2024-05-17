from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/webhook', methods=['GET'])
def webhook():
    if request.method == 'GET':
        # Bibliothèques populaires de Python avec descriptions en français
        libraries = {
            "Pandas": "Pandas est une bibliothèque open-source rapide, puissante, flexible et facile à utiliser pour l'analyse et la manipulation de données, construite sur le langage de programmation Python.",
            "NumPy": "NumPy est la bibliothèque fondamentale pour le calcul scientifique en Python. Elle contient entre autres un puissant objet tableau N-dimensionnel.",
            "PySpark": "PySpark est l'API Python pour Apache Spark, un moteur d'analyse unifié open-source pour le traitement de données à grande échelle.",
            "SciPy": "SciPy est une bibliothèque Python utilisée pour le calcul scientifique et technique. Elle se base sur NumPy et fournit un grand nombre de fonctions de haut niveau.",
            "Matplotlib": "Matplotlib est une bibliothèque complète pour créer des visualisations statiques, animées et interactives en Python.",
            "Seaborn": "Seaborn est une bibliothèque de visualisation de données en Python basée sur Matplotlib. Elle offre une interface de haut niveau pour dessiner des graphiques statistiques attrayants et informatifs.",
            "Scikit-learn": "Scikit-learn est une bibliothèque d'apprentissage automatique pour Python qui fournit des outils simples et efficaces pour l'exploration et l'analyse de données.",
            "TensorFlow": "TensorFlow est une plateforme open-source de bout en bout pour l'apprentissage automatique développée par Google.",
            "Keras": "Keras est une bibliothèque open-source qui offre une interface Python pour les réseaux de neurones artificiels. Keras agit comme une interface pour la bibliothèque TensorFlow."
        }

        return jsonify(libraries), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
