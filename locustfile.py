from locust import HttpUser, task, between

class MyWebsiteUser(HttpUser):
    # උඹේ සජීවී වෙබ් අඩවියේ URL එක
    host = "https://sasinda-1-62b398e21c9e.herokuapp.com"
    
    # 0.1 සිට 0.5 තත්පර දක්වා පරතරයක් තැබීමෙන් පීඩනය වැඩි කළ හැක
    wait_time = between(0.1, 0.5)

    @task
    def load_home_page(self):
        # සර්වර් එකේ ප්‍රතිචාරය නිරීක්ෂණය කරමින් GET ඉල්ලීම යැවීම
        with self.client.get("/", catch_response=True) as response:
            if response.status_code >= 400:
                response.failure(f"Failed with status code: {response.status_code}")
            else:
                response.success()
