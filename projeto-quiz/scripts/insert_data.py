from config.redis_config import get_redis_connection

def insert_example_data():
    redis_conn = get_redis_connection()

    # Inserir Quiz
    redis_conn.hset('quiz:1', mapping={
        'name': 'Quiz de Matemática',
        'duration': 120,
        'questions': '1,2'
    })
    redis_conn.expire('quiz:1', 2592000)  # Expira em 30 dias

    # Inserir Perguntas
    redis_conn.hset('question:1', mapping={
        'text': 'Quanto é 2+2?',
        'options': '1,2,3,4'
    })
    redis_conn.expire('question:1', 2592000)

    redis_conn.hset('question:2', mapping={
        'text': 'Quanto é 5x5?',
        'options': '5,6,7,8'
    })
    redis_conn.expire('question:2', 2592000)

    print("Dados inseridos com sucesso e configurados para expiração!")

if __name__ == '__main__':
    insert_example_data()
