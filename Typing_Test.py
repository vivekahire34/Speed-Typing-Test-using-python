import tkinter as tk
import random
import time

class TypingSpeedTester:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Tester")
        self.root.geometry("500x300")
        self.root.configure(bg='black')

        self.words = ["JAVA", "programming", "challenge", "typing", "engineering", "thanK you", "codeclause", "open", "tkinter", "developer"]
        self.current_word = ""
        self.user_input = ""
        self.words_typed = 0
        self.start_time = 0
        self.timer_running = False

        self.word_label = tk.Label(self.root, text="", font=("Helvetica", 18), fg="light green", bg="black")
        self.word_label.pack(pady=50)

        self.entry = tk.Entry(self.root, font=("Helvetica", 16), fg="light green", bg="black")
        self.entry.pack(pady=20)
        self.entry.bind("<Return>", self.check_typing)

        self.start_button = tk.Button(self.root, text="Start Typing Test", command=self.start_test, font=("Helvetica", 14), fg="light green", bg="black")
        self.start_button.pack()

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16), fg="light green", bg="black")
        self.result_label.pack()

    def start_test(self):
        if not self.timer_running:
            self.current_word = random.choice(self.words)
            self.word_label.config(text=self.current_word)
            self.entry.delete(0, tk.END)
            self.user_input = ""
            self.words_typed = 0
            self.start_time = time.time()
            self.timer_running = True
            self.root.after(30000, self.end_test)  # Set the timer for 30 seconds
            self.start_button.config(state=tk.DISABLED)

    def check_typing(self, event):
        if self.timer_running:
            user_word = self.entry.get().strip()
            if user_word == self.current_word:
                self.words_typed += 1
            self.current_word = random.choice(self.words)
            self.word_label.config(text=self.current_word)
            self.entry.delete(0, tk.END)

    def end_test(self):
        self.timer_running = False
        elapsed_time = time.time() - self.start_time
        words_per_minute = int((self.words_typed / elapsed_time) * 60)
        result_text = f"Words typed in 30 seconds: {self.words_typed}\nWords per minute: {words_per_minute} WPM"
        self.result_label.config(text=result_text, fg="light green")
        self.start_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTester(root)
    root.mainloop()
