import PyPDF2
import streamlit as st
import os

st.title("PDF Merger")

path= st.text_input("Provide folder path where all PDFs stored")
if path:
    files = [f for f in os.listdir(path) if f.endswith('.pdf')]
    pdf_writer = PyPDF2.PdfWriter ()
    uploaded_files = st.multiselect("Select a file:",files)
    if st.button("Merge PDFs") and uploaded_files:

        file_name=[]
        for file in uploaded_files:
            pdf_path= (path + '\\' +file)
            file_name.append(pdf_path)
            st.write(pdf_path)

            for filename in file_name:
                with open(filename, 'rb') as f:
                    pdf_reader = PyPDF2.PdfReader (f)
                    for page_num in range(len(pdf_reader.pages)):
                        pdf_writer.add_page(pdf_reader.pages[page_num]) 

            # Save the merged PDF file
                        with open(path+"//"+'merged_file.pdf', 'wb') as f:
                          pdf_writer.write(f)
                          
        st.success(f"Your file is ready at location: {path}")