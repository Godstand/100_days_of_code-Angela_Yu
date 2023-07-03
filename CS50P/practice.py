from fpdf import FPDF


class Shirt(FPDF):
    def header(self):
        # Set up the font properties for the header
        self.set_font("helvetica", "B", 24)
        self.cell(0, 60, "CS50 Shirtificate", align="C", fill=False)
        self.ln(20)

    def shirt(self, name):
        # Set up the page properties
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page(orientation="P", format=(210, 297))

        # Add the shirt image
        self.image("shirtificate.png", x=25, y=60, w=150, h=150)

        # Add the user's name on top of the shirt
        self.set_font("helvetica", "B", 18)
        self.set_text_color(255, 255, 255)  # White text color
        self.cell(w=180, h=150, txt=name, align="C", fill=False)

        # Output the PDF
        self.output("shirtificate.pdf")


def main():
    # Prompt the user for their name
    name = input("Enter your name: ")
    # Generate the shirtificate PDF
    shirtificate = Shirt()
    shirtificate.shirt(name)


if __name__ == "__main__":
    main()
