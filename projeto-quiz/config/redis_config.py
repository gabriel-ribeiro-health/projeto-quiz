import redis

def get_redis_connection():
    return redis.Redis(host='127.0.0.1', port=6379, db=0)
