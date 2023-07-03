from fpdf import FPDF


class Shirtificate(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 16)
        self.cell(w=40, h=10, txt='CS50 Shirtificate', align='C', fill=False)
        self.ln(20)

    def shirt(self, name_of_student):
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page(orientation="P", format=(210, 297))
        self.image("shirtificate.png", x=5, y=50, w=200, h=220)  # Adjust the dimensions as per your requirement
        self.set_font("helvetica", "B", 24)
        self.set_text_color(255, 255, 255)
        self.cell(w=100, h=220, txt=name_of_student, align='C', fill=False)
        self.output("Godstand.pdf")


def main():
    name = input("Student name: ")
    shirtificate = Shirtificate()
    shirtificate.shirt(name)


if __name__ == "__main__":
    main()
