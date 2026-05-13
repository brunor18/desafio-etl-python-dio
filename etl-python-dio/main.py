import pandas as pd
import random


## No desafio original, se utiliza a API do openai gratuita para gerar as mensagens da etapa transform,
## como a API gratuita foi descontinuada, adaptei o código com esta lista

DICAS_INVESTIMENTOS = [
    "Olá {name}, investir é o primeiro passo para sua liberdade!",
    "{name}, faça seu dinheiro trabalhar por você hoje mesmo.",
    "O futuro começa agora. Invista com inteligência, {name}.",
    "{name}, diversificar é a chave para um patrimônio sólido.",
    "Poupe hoje, conquiste amanhã. Invista conosco, {name}!",
    "{name}, já pensou em ver seu dinheiro render todo mês?",
    "Não deixe seu dinheiro parado. Invista agora, {name}!",
    "{name}, pequenos aportes geram grandes resultados no futuro.",
    "Segurança e rentabilidade para seus planos, {name}.",
    "Sua reserva de emergência é sua paz de espírito, {name}.",
    "{name}, invista em você e nos seus sonhos de longo prazo.",
    "O juro composto é o melhor amigo do investidor, {name}.",
    "{name}, transforme seus objetivos em realidade investindo.",
    "Menos gastos, mais investimentos. Vamos nessa, {name}?",
    "{name}, a melhor hora para começar a investir foi ontem.",
    "Planeje sua aposentadoria com nossos fundos, {name}.",
    "{name}, entenda seu perfil e comece a lucrar agora.",
    "Investir é cuidar do seu 'eu' do futuro, {name}.",
    "Sua jornada rumo à riqueza começa aqui, {name}.",
    "{name}, proteção e crescimento para o seu capital!"
]


## EXTRACT
users = pd.read_csv('planilha.csv').to_dict(orient='records')


## TRANSFORM
def generate_tip(user):
    mensagem_base = random.choice(DICAS_INVESTIMENTOS)
    mensagem_final = mensagem_base.format(name=user['name'])
    return mensagem_final[:100]



for user in users:
    tip = generate_tip(user)
    print(f"Dica escolhida: {tip}")
    user['tip'] = tip


## LOAD
with open('LOAD.txt', 'w', encoding='utf-8') as file:
    file.write("Parte load\n")
    for user in users:
        id = user['id']
        nome = user['name']
        cartao = user['card']
        dica = user['tip']

        linha = f"ID: {id} \n Usuario: {nome} \n Cartao: {cartao} \n Mensagem: {dica} \n"

        file.write(linha)

print("Etapa load concluida")