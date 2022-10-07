import re

from backend.src.parse_generic import  MedicalDocParser

class PatientDetailsParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return  {
             'patient_name': self.get_patient_name(),
             'phone_number': self.get_patient_phone_number(),
             'medical_problems': self.get_medical_problems(),
             'hepatitis_b_vaccination': self.get_hepatitis_b_vaccination()
        }

    def get_patient_name(self):
        pattern = 'Patient Information(.*?)\(\d{3}\)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        name = ''
        if matches:
            name = self.remove_noise_from_name(matches[0])
        return name

    def get_patient_phone_number(self):
        pattern = 'Patient Information(.*?)(\(\d{3}\) \d{3}-\d{4})'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            return matches[0][-1]


    def get_hepatitis_b_vaccination(self):
        pattern = 'Have you had the Hepatitis B vaccination\?.*(Yes|No)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            return matches[0].strip()

    def get_medical_problems(self):
        pattern = 'List any Medical Problems .*?:(.*)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            return matches[0].strip()

    def remove_noise_from_name(self, name):
        name = name.replace("Birth Date", "").strip()
        date_pattern = '((Jan|Feb|March|April|May|June|July|Aug|Sep|Oct|Nov|Dec)[ \d]+)'
        date_matches = re.findall(date_pattern, name)

        if date_matches:
            date = date_matches[0][0]
            name = name.replace(date, '').strip()
        return name

if __name__ == '__main__':
    document_text = '''   
Patient Medical Record

        Patient Information
        Navya Pellakuru

        (279) 920-8204

        4218 Wheeler Ridge Dr
        Buffalo, New York, 14201
        United States

        In Case of Emergency

        -_ OCC OO eee

        Joe Lucas

        Home phone

        General Medical History



        Chicken Pox (Varicelia):
        IMMUNE
        Have you had the Hepatitis B vaccination?

        Yes”

        Birth Date
        May 2 1998

        Weight:
        57

        Height:
        170

        4218 Wheeler Ridge Dr
        Buffalo, New York, 14201
        United States

        Work phone

        Measles: .

        NOT IMMUNE

        List any Medical Problems (asthma, seizures, headaches):

        N/A
'''

    pp = PatientDetailsParser(document_text)
    print(pp.parse())
