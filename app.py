from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "equacoes_segundo_grau"

questoes = [

    {
        "pergunta": "A equação x² − 5x + 6 = 0 possui quais raízes?",
        "opcoes": {
            "a": "1 e 6",
            "b": "2 e 3",
            "c": "0 e 6",
            "d": "1 e 5"
        },
        "correta": "b",
        "explicacao": """
        x²−5x+6=0

        (x−2)(x−3)=0

        x=2 ou x=3
        """
    },

    {
        "pergunta": "Qual é o valor do discriminante (Δ) da equação x² + 4x + 3 = 0?",
        "opcoes": {
            "a": "4",
            "b": "8",
            "c": "16",
            "d": "28"
        },
        "correta": "a",
        "explicacao": """
        Δ = b² − 4ac

        Δ = 4² − 4(1)(3)

        Δ = 16 − 12

        Δ = 4
        """
    },

    {
        "pergunta": "Na equação 2x² − 8x + 6 = 0, qual é o valor do coeficiente b?",
        "opcoes": {
            "a": "2",
            "b": "8",
            "c": "-8",
            "d": "6"
        },
        "correta": "c",
        "explicacao": """
        ax² + bx + c

        2x² − 8x + 6

        a = 2
        b = -8
        c = 6
        """
    },

    {
        "pergunta": "Qual fórmula é utilizada para resolver equações completas do 2º grau?",
        "opcoes": {
            "a": "Teorema de Pitágoras",
            "b": "Regra de Três",
            "c": "Fórmula de Bhaskara",
            "d": "Fórmula da Área do Triângulo"
        },
        "correta": "c",
        "explicacao": """
        x = (-b ± √Δ) / 2a
        """
    },

    {
        "pergunta": "A equação x² − 9 = 0 possui quais raízes?",
        "opcoes": {
            "a": "9 e 0",
            "b": "-9 e 9",
            "c": "-3 e 3",
            "d": "1 e 9"
        },
        "correta": "c",
        "explicacao": """
        x² = 9

        x = ±3
        """
    },

    {
        "pergunta": "Qual é o valor de Δ na equação x² − 6x + 9 = 0?",
        "opcoes": {
            "a": "0",
            "b": "3",
            "c": "9",
            "d": "12"
        },
        "correta": "a",
        "explicacao": """
        Δ = (-6)² − 4(1)(9)

        Δ = 36 − 36

        Δ = 0
        """
    },

    {
        "pergunta": "Quando Δ é menor que zero, a equação possui:",
        "opcoes": {
            "a": "Duas raízes reais diferentes",
            "b": "Uma raiz real",
            "c": "Nenhuma raiz real",
            "d": "Três raízes reais"
        },
        "correta": "c",
        "explicacao": """
        Quando Δ < 0

        Não existem raízes reais.
        """
    },

    {
        "pergunta": "Na equação x² + 7x + 10 = 0, quais são as raízes?",
        "opcoes": {
            "a": "2 e 5",
            "b": "-2 e -5",
            "c": "-2 e 5",
            "d": "2 e -5"
        },
        "correta": "b",
        "explicacao": """
        x² + 7x + 10 = 0

        (x+2)(x+5)=0

        x=-2

        x=-5
        """
    },

    {
        "pergunta": "Qual é o coeficiente 'a' da equação 5x² + 2x − 7 = 0?",
        "opcoes": {
            "a": "2",
            "b": "-7",
            "c": "5",
            "d": "0"
        },
        "correta": "c",
        "explicacao": """
        a = 5
        """
    },

    {
        "pergunta": "Resolver uma equação do 2º grau significa:",
        "opcoes": {
            "a": "Encontrar os valores de x que tornam a igualdade verdadeira",
            "b": "Somar todos os coeficientes",
            "c": "Calcular apenas o discriminante",
            "d": "Multiplicar os coeficientes"
        },
        "correta": "a",
        "explicacao": """
        Resolver significa encontrar os valores de x que satisfazem a igualdade.
        """
    }

]

@app.route('/')
def index():

    session.clear()
    session['pontuacao'] = 0
    session['questao'] = 0

    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():

    indice = session.get('questao', 0)

    if indice >= len(questoes):
        return redirect(url_for('resultado'))

    if request.method == 'POST':

        resposta = request.form.get('resposta')

        if resposta == questoes[indice]['correta']:
            session['pontuacao'] += 1

        session['questao'] += 1

        return redirect(url_for('quiz'))

    progresso = int((indice / len(questoes)) * 100)

    return render_template(
        'quiz.html',
        questao=questoes[indice],
        numero=indice + 1,
        total=len(questoes),
        progresso=progresso
    )

@app.route('/resultado')
def resultado():

    pontuacao = session['pontuacao']
    total = len(questoes)

    percentual = round((pontuacao / total) * 100)

    if percentual >= 90:
        medalha = "🥇 Ouro"
    elif percentual >= 70:
        medalha = "🥈 Prata"
    else:
        medalha = "🥉 Bronze"

    return render_template(
        'resultado.html',
        pontuacao=pontuacao,
        total=total,
        percentual=percentual,
        medalha=medalha
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
