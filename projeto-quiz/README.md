Sistema Gamificado de Quiz com Redis

Este projeto implementa um sistema gamificado de quiz para cursos online, utilizando Redis para armazenamento de dados. O objetivo é permitir que milhares de alunos participem de quizzes em tempo real, garantindo alta concorrência, baixa latência e persistência dos dados.
📋 Funcionalidades

    Quizzes e Perguntas
        Professores podem criar quizzes com perguntas de múltipla escolha.
        Cada pergunta possui 4 alternativas (A, B, C e D).

    Participação dos Alunos
        Alunos podem participar do quiz em tempo real e escolher uma alternativa por pergunta.

    Contabilização de Votos
        O sistema registra os votos em tempo real e mantém contadores para cada alternativa.

    Rankings e Métricas
        Rankings disponíveis:
            Alternativas mais votadas.
            Questões mais acertadas.
            Alunos com mais acertos, maior rapidez e ambos combinados.

    Persistência e Expiração
        Dados ficam armazenados no Redis por 30 dias, com expiração automática configurada.

🛠️ Tecnologias Utilizadas

    Backend: Python com FastAPI.
    Banco de Dados: Redis.
    Ferramentas de Teste: Postman, Locust e RedisInsight.
    Simulações de Carga: Locust para simulação de concorrência.
    Estruturas de Dados no Redis:
        Hash: Para armazenar perguntas, alternativas e contadores de votos.
        Sorted Set: Para registrar votos com timestamp.

📂 Estrutura de Arquivos

projeto-quiz/
├── api/
│   ├── vote_endpoints.py       # Endpoints de votação e rankings
├── config/
│   ├── redis_config.py         # Configuração do Redis
├── tests/
│   ├── test_data.json          # Arquivos JSON para simulação de votos
├── locustfile.py               # Arquivo para testes de carga com Locust
├── main.py                     # Arquivo principal para iniciar o servidor
└── README.md                   # Documentação do projeto

🚀 Como Executar o Projeto
Pré-requisitos

    Python 3.10 ou superior.
    Redis instalado e em execução localmente na porta padrão (6379).
    RedisInsight para monitorar os dados (opcional).

1. Configurar o Ambiente

    Clone o repositório:

git clone <url-do-repositorio>
cd projeto-quiz

Crie e ative o ambiente virtual:

python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows

Instale as dependências:

    pip install -r requirements.txt

2. Configurar o Redis

Certifique-se de que o Redis está em execução. Caso contrário, inicie o servidor Redis:

redis-server

3. Executar o Servidor FastAPI

Inicie o servidor local:

uvicorn main:app --reload

Acesse a documentação interativa em:

http://127.0.0.1:8000/docs

🧪 Testes
1. Testes Funcionais

    Use o Postman ou a interface Swagger (/docs) para testar os endpoints:
        /vote: Registrar votos.
        /rankings/alternatives: Ver alternativas mais votadas.
        /rankings/questions: Ver questões mais acertadas.
        /rankings/students: Ver rankings de alunos.

2. Testes de Carga

    Execute o Locust:

locust -f locustfile.py --host http://127.0.0.1:8000

Acesse a interface do Locust em:

    http://127.0.0.1:8089

    Simule múltiplos usuários e monitore o tempo de resposta e os erros.

📊 Estruturas de Dados no Redis
1. Perguntas

    Chave: question:<id>
    Exemplo:

HGETALL question:1

    "text": "Quanto é 2+2?"
    "options": "A,B,C,D"

2. Alternativas

    Chave: option:<question_id>:<option_id>
    Exemplo:

HGETALL option:1:C

    "text": "4"
    "votes": 12

3. Votos

    Chave: votes:<question_id>
    Exemplo:

ZRANGE votes:1 0 -1 WITHSCORES

    "aluno1:C" 1633036800

📈 Rankings Disponíveis

    Alternativas Mais Votadas
        Endpoint: /rankings/alternatives
        Retorna as alternativas mais votadas de todas as perguntas.

    Questões Mais Acertadas
        Endpoint: /rankings/questions
        Retorna as questões com maior número de respostas corretas.

    Rankings de Alunos
        Endpoint: /rankings/students
        Retorna:
            Alunos com mais acertos.
            Alunos mais rápidos.
            Combinação de ambos.

📋 Requisitos Atendidos

Registro de votos com validação.
Rankings em tempo real.
Persistência no Redis com expiração automática.

    Testes de carga com Locust.

📜 Licença

Este projeto é apenas para fins acadêmicos e foi desenvolvido como parte de um MBA em Engenharia de Dados.