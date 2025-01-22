class QuizGame:
    def __init__(self):
        self.questions = [
            {
                "question": "Vad är huvudstaden i Sverige?",
                "options": ["1. Göteborg", "2. Malmö", "3. Stockholm", "4. Uppsala"],
                "answer": 3
            },
            {
                "question": "Vilket år börjadre andra världskriget?",
                "options": ["1. 1935", "2. 1939", "3. 1941", "4. 1945"],
                "answer": 2
            },
            {
                "question": "Vad är 5 + 7?",
                "options": ["1. 10", "2. 12", "3. 14", "4. 15"],
                "answer": 2
            },
            {
                "question": "vilken planet är käönd som den röda planeten",
                "options": ["1. Jupiter", "2. mars", "3. venus", "4. saturnus"],
                "answer": 2
            },
            {
                "question": "vilket ämne har den kemiska betekningen h2o?",
                "options": ["1. väte", "2. syre", "3. vatten", "4. koldioxid"],
                "answer": 3
            },
            {
                "question": "vad är 15 * 3?",
                "options": ["1. 45", "2. 50", "3. 55", "4. 60"],
                "answer": 1
            },
            {
                "question": "Vem skrev 'Romeo och Julia'?",
                "options": ["1. Charles Dickens", "2. William Shakespeare", "3. Mark Twain", "4. Jane Austen"],
                "answer": 2
            },
            {
                "question": "Vilken färg har himlen oftast på en klar dag?",
                "options": ["1. Grön", "2. Blå", "3. Gul", "4. Vit"],
                "answer": 2
            },
            {
                "question": "Vad är huvudstaden i Norge?",
                "options": ["1. Oslo", "2. Bergen", "3. Trondheim", "4. Stavanger"],
                "answer": 1
            },
            {
                "question": "Hur många kontinenter finns det?",
                "options": ["1. Fem", "2. Sex", "3. Sju", "4. Åtta"],
                "answer": 3
            }
        ]
        self.score = 0 

    def display_question(self, question_data):
        print("\n" + question_data["question"])
        for option in question_data["options"]:
            print(option)

        while True:
            try:
                user_answer = int(input("ditt svar (ange siffran): "))
                if 1 <= user_answer <= 4:
                    return user_answer
                else:
                    print("ogiltigt val. ange en siffra mellan 1 och 4.")
            except ValueError:
                print("ogilitig input. ange en siffra.")

    def play(self):
        print("välkommen till quizspelet!")
        for index, question_data in enumerate(self.questions, start=1):
            print(f"\nfråga {index} av {len(self.questions)}")
            user_answer = self.display_question(question_data)
            if user_answer == question_data["answer"]:
                print("rätt svar")
                self.score += 1
            else:
                print(f"fel svar, rätt svar {question_data['answer']}: {question_data['option'][question_data['answer'] - 1]}")

                
        print(f"\nSpelet är slut! Din poäng: {self.score} av {len(self.questions)}.")
        print("Tack för att du spelade!")

if __name__ == "__main__":
    game = QuizGame()
    game.play()
