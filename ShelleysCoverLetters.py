
import customtkinter as ctk

from pathlib import Path
from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import SingleColumnLayout
from borb.pdf import Paragraph
from borb.pdf import PDF

## das logic 

def pdfgen():
    pdf = Document()
    name = entry1.get()
    coname = entry2.get()
    jobname = entry3.get()
    location = entry4.get()
    dafont = combobox.get()
    sub = "Subject: {}".format(jobname)
    title = "{}_coverletter.pdf".format(coname)
    txt1 = entry5.get()
    txt2 = entry6.get()
    txt3 = entry7.get()
    txt4 = entry8.get()
    page = Page()
    pdf.add_page(page)
    layout = SingleColumnLayout(page)
    layout.add(Paragraph(coname, font=dafont))
    layout.add(Paragraph(location, font=dafont))
    layout.add(Paragraph(sub, font=dafont))
    layout.add(Paragraph(txt1.format(jobname), font=dafont))
    layout.add(Paragraph(txt2, font=dafont))
    layout.add(Paragraph(txt3, font=dafont))
    layout.add(Paragraph(txt4, font=dafont))
    layout.add(Paragraph("Regards,", font=dafont))
    layout.add(Paragraph(name, font=dafont))
    with open(Path(title), "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, pdf)


## User Interface modules 

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("750x650") 
root.title("Shelley's Insta-Cover")

tabs = ctk.CTkTabview(master=root)
tabs.pack(pady=20, padx=60, fill="both", expand=True)
tabs.add("Shelley")
tabs.add("Settings")

#Shelley

label = ctk.CTkLabel(master=tabs.tab("Shelley"), text="Instant Cover letters w/ shelly")
label.pack(pady=20, padx=10)

entry1 = ctk.CTkEntry(master=tabs.tab("Shelley"), placeholder_text="Your Full Name")
entry1.pack(pady=12, padx=10)

entry2 = ctk.CTkEntry(master=tabs.tab("Shelley"), placeholder_text="Company Name")
entry2.pack(pady=12, padx=10)

entry3 = ctk.CTkEntry(master=tabs.tab("Shelley"), placeholder_text="Job/ Position Title")
entry3.pack(pady=12, padx=10)

entry4 = ctk.CTkEntry(master=tabs.tab("Shelley"), placeholder_text="Company Location")
entry4.pack(pady=12, padx=10)

butt = ctk.CTkButton(master=tabs.tab("Shelley"), text="Generate PDF",command=pdfgen)
butt.pack(padx=20, pady=20)

# Settings 

frame = ctk.CTkScrollableFrame(master=tabs.tab("Settings"))
frame.pack(pady=20, padx=60, fill="both", expand=True)

combobox = ctk.CTkOptionMenu(master=frame, 
                                       values=["Courier", "Courier-bold", "Courier-bold-oblique", "Courier-oblique", "Helvetica", "Helvetica-bold", "Helvetica-bold-oblique", "Helvetica-oblique", "Times-bold", "Times-bold-oblique", "Times-oblique", "Times-roman"])
combobox.pack(padx=20, pady=10)
combobox.set("Times-roman")  

label = ctk.CTkLabel(master=frame, text="use {} to refer to Job Position you are applying to")
label.pack(pady=20, padx=10)

label = ctk.CTkLabel(master=frame, text="Introduction")
label.pack(pady=20, padx=10)
entry5 = ctk.CTkTextbox(master=frame, width=425, height=220)
entry5.pack(pady=12, padx=10)

label = ctk.CTkLabel(master=frame, text="Experience 1")
label.pack(pady=20, padx=10)
entry6 = ctk.CTkTextbox(master=frame, width=425, height=220)
entry6.pack(pady=12, padx=10)

label = ctk.CTkLabel(master=frame, text="Experience 2")
label.pack(pady=20, padx=10)
entry7 = ctk.CTkTextbox(master=frame, width=425, height=220) 
entry7.pack(pady=12, padx=10)

label = ctk.CTkLabel(master=frame, text="Outro")
label.pack(pady=20, padx=10)
entry8 = ctk.CTkTextbox(master=frame, width=425, height=220)
entry8.pack(pady=12, padx=10)

root.mainloop()




