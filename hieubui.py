import tkinter as tk
from tkinter import messagebox, ttk
import datetime

class StudyManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📌 Quản Lý Học Tập Thông Minh")
        self.root.geometry("600x700")
        self.root.configure(bg='#f4f4f4')

        self.schedule = []
        self.exams = []
        self.notes = []
        self.important_lessons = []
        self.deadlines = []

        # Tiêu đề chính
        tk.Label(root, text="📘 QUẢN LÝ HỌC TẬP CÁ NHÂN", font=("Arial", 24, "bold"), bg='#f4f4f4', fg='#2c3e50').pack(pady=10)

        # Tabs setup
        self.tabs = ttk.Notebook(root)
        style = ttk.Style()
        style.configure('TNotebook.Tab', font=('Arial', 12, 'bold'), padding=[10, 5], background='#dfe6e9')
        style.map('TNotebook.Tab', background=[('selected', '#2ecc71')], foreground=[('selected', '#ffffff')])

        self.create_timetable_tab()
        self.create_exam_tab()
        self.create_notes_tab()
        self.create_lessons_tab()
        self.create_deadline_tab()
        self.tabs.pack(expand=1, fill="both")

        # Cập nhật thời gian và nhắc nhở
        self.update_time()

    def create_tab_layout(self, tab, icon, title):
        tk.Label(tab, text=f"{icon} {title}", font=("Arial", 18, "bold"), fg="#34495e").pack(pady=5)
        tk.Label(tab, text="Nhập thông tin dưới đây: ", font=("Arial", 12, "italic"), fg="#7f8c8d").pack(pady=5)

    def create_timetable_tab(self):
        timetable_tab = ttk.Frame(self.tabs)
        self.tabs.add(timetable_tab, text='📚 Lịch học')
        self.create_tab_layout(timetable_tab, "📚", "Lịch Học")

        self.create_input_section(timetable_tab, "Môn học:", "Ngày (dd-mm-yyyy):", "Giờ (HH:MM):", self.add_schedule, "Thêm vào lịch học")
        self.schedule_list = self.create_listbox(timetable_tab)

    def create_exam_tab(self):
        exam_tab = ttk.Frame(self.tabs)
        self.tabs.add(exam_tab, text='📝 Lịch thi')
        self.create_tab_layout(exam_tab, "📝", "Lịch Thi")

        self.create_input_section(exam_tab, "Môn thi:", "Ngày thi (dd-mm-yyyy):", "Giờ thi (HH:MM):", self.add_exam, "Thêm vào lịch thi")
        self.exam_list = self.create_listbox(exam_tab)

    def create_notes_tab(self):
        notes_tab = ttk.Frame(self.tabs)
        self.tabs.add(notes_tab, text='📒 Ghi chú')
        self.create_tab_layout(notes_tab, "📒", "Ghi Chú")

        self.note_entry = tk.Entry(notes_tab, width=50, font=("Arial", 12))
        self.note_entry.pack(pady=5)
        tk.Button(notes_tab, text="Thêm ghi chú", font=("Arial", 12), bg='#3498db', fg='white', command=self.add_note).pack(pady=10)
        self.note_list = self.create_listbox(notes_tab)

    def create_lessons_tab(self):
        lessons_tab = ttk.Frame(self.tabs)
        self.tabs.add(lessons_tab, text='⭐ Bài giảng quan trọng')
        self.create_tab_layout(lessons_tab, "⭐", "Bài Giảng Quan Trọng")

        self.lesson_entry = tk.Entry(lessons_tab, width=50, font=("Arial", 12))
        self.lesson_entry.pack(pady=5)
        tk.Button(lessons_tab, text="Thêm bài giảng", font=("Arial", 12), bg='#e67e22', fg='white', command=self.add_lesson).pack(pady=10)
        self.lesson_list = self.create_listbox(lessons_tab)

    def create_deadline_tab(self):
        deadline_tab = ttk.Frame(self.tabs)
        self.tabs.add(deadline_tab, text='⏳ Deadline')
        self.create_tab_layout(deadline_tab, "⏳", "Deadline")

        self.create_input_section(deadline_tab, "Bài tập cần làm:", "Ngày nộp (dd-mm-yyyy HH:MM):", None, self.add_deadline, "Thêm Deadline")
        self.deadline_list = self.create_listbox(deadline_tab)

    def create_input_section(self, tab, label1, label2, label3, command, button_text):
        self.entry1 = tk.Entry(tab, width=50, font=("Arial", 12))
        self.entry1.pack(pady=5)
        self.entry2 = tk.Entry(tab, width=30, font=("Arial", 12))
        self.entry2.pack(pady=5)
        if label3:
            self.entry3 = tk.Entry(tab, width=15, font=("Arial", 12))
            self.entry3.pack(pady=5)
        tk.Button(tab, text=button_text, font=("Arial", 12), bg='#2ecc71', fg='white', command=command).pack(pady=10)

    def create_listbox(self, tab):
        return tk.Listbox(tab, width=60, height=10, font=("Arial", 12), bg='#ecf0f1', fg='#2c3e50').pack(pady=10)

    def add_schedule(self):
        self.schedule.append(self.entry1.get())

    def add_exam(self):
        self.exams.append(self.entry1.get())

    def add_note(self):
        self.notes.append(self.note_entry.get())

    def add_lesson(self):
        self.important_lessons.append(self.lesson_entry.get())

    def add_deadline(self):
        self.deadlines.append(self.entry1.get())

    def update_time(self):
        self.root.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudyManagerApp(root)
    root.mainloop()
