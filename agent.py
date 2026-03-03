import openai
import logging
import time

# Configuring logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AutonomousAgent:
    def __init__(self, model, iteration_limit=10):
        self.model = model
        self.iteration_limit = iteration_limit
        self.current_iteration = 0

    def log(self, message):
        logging.info(message)
        
    def handle_error(self, error):
        logging.error(f'Error occurred: {error}')

    def run(self, prompt):
        while self.current_iteration < self.iteration_limit:
            try:
                self.log(f'Starting iteration {self.current_iteration + 1}')
                response = openai.ChatCompletion.create(
                    model=self.model,
                    messages=[{'role': 'user', 'content': prompt}]
                )
                self.log(f'Response: {response}')
                self.current_iteration += 1
                time.sleep(1)  # Pause to avoid rate limit issues
            except Exception as e:
                self.handle_error(e)
                break

if __name__ == '__main__':
    agent = AutonomousAgent(model='gpt-3.5-turbo')
    agent.run('What is the future of AI?')