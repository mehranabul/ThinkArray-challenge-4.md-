import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import PyPDF2
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class resume_scanner:
    def get_script(self, pdf_pages):
        script = []
        for i in range (0,len(pdf_pages)):
            page=pdf_pages[i]
            text=page.extract_text()
            script.append(text)
        return script

    def file_contain(self, file):    
        file_open=open(file,'rb')
        pdf_cv=PyPDF2.PdfReader(file_open)
        pdf_pages = pdf_cv.pages
        script_result = self.get_script(pdf_pages = pdf_pages)
        script=''.join(script_result)
        clear_cv=script.replace("\n","")
        return clear_cv

    def get_report(self, cv_clear, req_clear):
        match_test=[cv_clear, req_clear]
        cv=CountVectorizer()
        count_matrix=cv.fit_transform(match_test)
        #print('Similarity is :',cosine_similarity(count_matrix))
        # report['Similarity'] = cosine_similarity(count_matrix)
        matchpercentage=cosine_similarity(count_matrix)[0][1]*100
        report = round(matchpercentage,2)
        #print('Match Percentage is :'+ str(matchpercentage)+'% to Requirement')
        return report
    
    def run_scanner(self, text):
        path = r"resume_data/"

        candidate_data = pd.read_csv("candidate_data.csv")
        resume_list = list(candidate_data['cv_name'])

        similarity_list = []

        req_clear = text.replace("\n","")
    
        for file in resume_list:
            full_name = path+file
            clear_cv = self.file_contain(file=full_name)
            report = self.get_report(clear_cv, req_clear)
            similarity_list.append(report)

        candidate_data['match'] = similarity_list

        return candidate_data
    