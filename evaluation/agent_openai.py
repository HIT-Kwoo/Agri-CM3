import time
from openai import OpenAI

class Agent_OpenAI():
    def __init__(self, args):
        super(Agent_OpenAI, self).__init__()
        self.name = args.model_name
        self.temperature = args.temperature
        self.max_tokens = args.max_tokens
        self.model_name = args.model_name
        self.api_key = args.api_key
        self.api_url = args.api_url
        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.api_url
        )
        
    def generate_response(self, messages, max_depth=0) -> str:
        try:
            completion = self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                timeout=180,
            )
        except Exception as ex:
            print(f"Find Error: {ex}")
            if max_depth > 10:
                print("The maximum number of call rounds is exceeded.")
                return "The maximum number of call rounds is exceeded."
             
            print("Sleep 2s ...")
            time.sleep(2)
            return self.generate_response(messages, max_depth=max_depth+1)

        return completion.choices[0].message.content
    
    def forward(self, messages) -> str:
        response = self.generate_response(messages)
        return response