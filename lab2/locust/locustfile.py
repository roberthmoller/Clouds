from locust import HttpUser, task
lower: float = 0
upper: float = 3.14159

class NumericalIntegration(HttpUser):
    @task
    def integral(self):
        self.client.get(f"/integral/{lower}/{upper}")
