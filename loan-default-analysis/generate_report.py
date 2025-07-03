from fpdf import FPDF

def generate_pdf_report(data, prediction, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Loan Default Risk Report", ln=True, align='C')
    pdf.ln(10)

    for col, val in data.iloc[0].items():
        pdf.cell(200, 10, txt=f"{col}: {val}", ln=True)

    result = "High Risk of Default" if prediction == 1 else "Low Risk of Default"
    pdf.ln(10)
    pdf.set_text_color(255, 0, 0) if prediction == 1 else pdf.set_text_color(0, 128, 0)
    pdf.cell(200, 10, txt=f"Prediction: {result}", ln=True)

    pdf.output(filename)
