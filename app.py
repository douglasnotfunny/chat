import requests
import json
from gensim.models import Word2Vec
import numpy as np

from text_processing import processing

from connection_db import create, select, save_conversa

URL = "https://api.openai.com/v1/chat/completions"
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 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'
}

def read():
    msg = input("Informe o que deseja (sair para encerrar): ")
    print("Mensagem:", msg)
    return msg


def payload(msg):
    payload = json.dumps({
        "model": "gpt-3.5-turbo",
        "messages": [
            {
            "role": "user",
            "content": msg + 'responder em portugues e limitar a 500 caracteres'
            }
        ]
    })
    response_text = requests.request("POST", URL, headers=HEADERS, data=payload)
    return response_text

def get_response(response):
    content = response.__dict__['_content']
    message = json.loads(content)['choices'][0]['message']['content']
    return message

def create_table():
    mydb = None
    try:
        mydb = create()
    except Exception as exc:
        return None
    return mydb

def select_try():
    try:
        return select()
    except Exception:
        return None

def houndred(msg, result):
    for question in result:
        if msg == question[1]:
            return question[4]
    return None

def analyse_similarity(msg, corpus):
    model = Word2Vec(sentences=corpus, vector_size=100, window=5, min_count=1, workers=4)
    sentence_vector = np.mean([model.wv[word] for word in msg.split(' ')], axis=0)

    similar_sentences = []
    for sent in corpus:
        sent_vector = np.mean([model.wv[word] for word in sent], axis=0)
        # calculo do cosseno do ângulo entre os vetores
        similarity = np.dot(sentence_vector, sent_vector) / (np.linalg.norm(sentence_vector) * np.linalg.norm(sent_vector))
        similar_sentences.append((sent, similarity))

    similar_sentences.sort(key=lambda x: x[1], reverse=True)
    
    similar_sentences.pop(0)
    return similar_sentences[0][1]

def analyse(msg):
    result = select_try()
    if not result:
        return None

    accepted_answers = []
    for question in result:
        calc = analyse_similarity(msg, [msg.split(), question[1].split()])
        # valor infirido a partir de observação de resultados
        if calc > 0.75:
            accepted_answers.append((question[4], calc))

    if accepted_answers:
        print(accepted_answers)
        accepted_answers.sort(key=lambda x: x[1])
        return accepted_answers[0][0]

    return None

if __name__ == '__main__':
    msg = ''
    while msg != 0:
        msg = read()
        if msg.lower() == 'sair':
            break
        msg_processing = processing(msg)
        response = analyse(msg_processing[1][0])

        if not response:
            response_payload = payload(msg)
            response = get_response(response_payload)
            response_processing = processing(response)

            create_table()
            save_conversa((msg_processing[1][0], response_processing[1][0], msg, response))
        print(f'Resposta: {response}')
    print("Chat encerrado")