import os

class StudentRanker:
    def __init__(self):
        self.students = []

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def bubble_sort(self, data, key=lambda x: x):
        n = len(data)
        for i in range(n):
            for j in range(n - i - 1):
                if key(data[j]) < key(data[j + 1]):
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

    def show_example(self):
        example_scores = [10, 23, 24, 5, 53, 12, 8]
        sorted_scores = self.bubble_sort(example_scores[:])
        print("\n=== Example Result ===")
        print(", ".join(str(score) for score in sorted_scores))

    def add_student(self):
        name = input("ชื่อนักเรียน: ").strip()
        if not name:
            print("ชื่อต้องไม่ว่าง")
            return

        while True:
            try:
                score = float(input("คะแนน: ").strip())
                break
            except ValueError:
                print("!! กรุณากรอกคะแนนเป็นตัวเลข")

        self.students.append({"name": name, "score": score})
        print(f"เพิ่ม {name} เรียบร้อยแล้ว")

    def show_ranking(self):
        if not self.students:
            print("!! ยังไม่มีข้อมูลนักเรียน")
            return
            
        example_scores = [10, 23, 24, 5, 53, 12, 8]
        for i in range(len(example_scores)):
            score = example_scores[i]
            self.students.append({"name": f"example {i + 1}", "score": float(score)})

        sorted_students = self.bubble_sort(self.students[:], key=lambda x: x['score'])
        print("\n=== อันดับนักเรียนตามคะแนน ===")
        for i, student in enumerate(sorted_students, start=1):
            print(f"อันดับ {i}: {student['name']} ได้ {student['score']} คะแนน")

    def student_menu(self):
        while True:
            self.clear_screen()
            print("\n=== เมนูการใส่ข้อมูลนักเรียน ===")
            print("1. เพิ่มนักเรียน")
            print("2. แสดงอันดับและกลับเมนูหลัก")
            choice = input("เลือกเมนูย่อย (1 หรือ 2): ").strip()

            if choice == '1':
                self.add_student()
                input("\nกด Enter เพื่อกลับเมนูย่อย...")
            elif choice == '2':
                self.show_ranking()
                input("\nกด Enter เพื่อกลับเมนูหลัก...")
                break
            else:
                print("!! กรุณาเลือกแค่ 1 หรือ 2 เท่านั้น")
                input("\nกด Enter เพื่อเลือกใหม่...")

    def main_menu(self):
        while True:
            self.clear_screen()
            print("\n=== Main Menu ===")
            print("1. แสดงผลตัวอย่าง [10, 23, 24, 5, 53, 12, 8]")
            print("2. ใส่ข้อมูลนักเรียน และ คะแนน [optional]")
            print("3. จบการทำงาน")
            choice = input("เลือกเมนู (1, 2 หรือ 3): ").strip()

            if choice == '1':
                self.clear_screen()
                self.show_example()
                input("\nกด Enter เพื่อกลับเมนูหลัก...")
            elif choice == '2':
                self.student_menu()
            elif choice == '3':
                break
            else:
                print("!! กรุณาเลือกแค่ 1, 2 หรือ 3 เท่านั้น")
                input("\nกด Enter เพื่อเลือกใหม่...")

if __name__ == "__main__":
    ranker = StudentRanker()
    ranker.main_menu()
