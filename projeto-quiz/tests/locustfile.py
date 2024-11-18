from locust import HttpUser, TaskSet, task, between

class VoteTasks(TaskSet):
    @task
    def vote(self):
        import random
        student_id = f"aluno{random.randint(1, 100)}"
        question_id = random.randint(1, 10)
        option_id = random.choice(["A", "B", "C", "D"])
        self.client.post("/api/vote", json={
            "student_id": student_id,
            "question_id": str(question_id),
            "option_id": option_id
        })

class WebsiteUser(HttpUser):
    tasks = [VoteTasks]
    wait_time = between(1, 5)  # Simula intervalos entre requisições
