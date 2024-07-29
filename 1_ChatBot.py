class SimpleChatbot:
    def __init__(self):
        self.memory = {}
        self.questions = ["What's your name?", "How old are you?", "What's your favorite color?"]
        self.responses = {
            "hello": "Hi there! How can I help you today?",
            "how are you": "I'm good,How are you?",
            "what's your name": "I'm a simple chatbot created to assist you.",
            "what can you do": "I can respond to basic questions, remember our interactions, and have a simple conversation.",
            "bye": "Goodbye! Have a great day!"
        }
        self.default_response = "I'm sorry, I didn't understand that. Can you please rephrase?"
        self.farewell_message = "Goodbye! Have a great day!"
    
    def greet(self):
        return "Hello! I'm your friendly chatbot. How can I assist you today?"
    
    def farewell(self):
        return self.farewell_message
    
    def ask_questions(self):
        for question in self.questions:
            answer = input(question + " ")
            key = question.strip("?").lower()
            self.memory[key] = answer
            print(f"Got it! {key.capitalize()} is {answer}.")
    
    def respond(self, user_input):
        user_input = user_input.lower()
        return self.responses.get(user_input, self.default_response)
    
    def recall_context(self):
        if self.memory:
            context = "Here's what I remember from our conversation: "
            context += " ".join([f"{key.capitalize()} is {value}." for key, value in self.memory.items()])
            return context
        return "I don't have any previous interactions recorded."
    
    def handle_interaction(self):
        print(self.greet())
        self.ask_questions()
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() == "bye":
                print(self.farewell())
                break
            elif user_input.lower() == "recall":
                print(self.recall_context())
            else:
                print(self.respond(user_input))


chatbot = SimpleChatbot()
chatbot.handle_interaction()
