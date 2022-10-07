from backend.src.parser_prescription import PrescriptionParser
import pytest

@pytest.fixture()
def doc_1_John():
    document_text = '''
    Dr John Smith, M.D
    2 Non-Important Street,
    New York, Phone (000)-111-2222
    Name: Marta Sharapova Date: 5/11/2022
    Address: 9 tennis court, new Russia, DC
    Prednisone 20 mg
    Lialda 2.4 gram
    Directions:
    Prednisone, Taper 5 mg every 3 days,
    Finish in 2.5 weeks a
    Lialda - take 2 pill everyday for 1 month
    Refill: 2 times
    '''
    return PrescriptionParser(document_text)

@pytest.fixture()
def doc_2_virat():
    document_text = '''
    Dr John Smith, M.D
    2 Non-Important Street,
    New York, Phone (000)-111-2222
    Name: Virat Date: 5/11/2022
    Address: 9 tennis court, new Russia, DC
    Prednisone 20 mg
    Lialda 2.4 gram
    Directions:
    Prednisone, Taper 5 mg every 3 days,
    Finish in 2.5 weeks a
    Lialda - take 2 pill everyday for 1 month
    Refill: 2 times
    '''
    return  PrescriptionParser(document_text)
@pytest.fixture()
def doc_3_empty():
    return  PrescriptionParser('')

def test_get_name(doc_1_John,doc_2_virat,doc_3_empty):
    assert doc_1_John.get_field('patient_name') == 'Marta Sharapova'
    assert doc_2_virat.get_field('patient_name') == 'Virat'
    assert doc_3_empty.get_field('patient_name') == None

def test_get_address(doc_1_John):
    assert doc_1_John.get_field('address') == ': 9 tennis court, new Russia, DC'

def test_parse(doc_1_John,doc_2_virat):
    record_virat = doc_2_virat.parse()
    assert record_virat['patient_name'] == 'Virat'

    record_John = doc_1_John.parse()
    assert record_John == {
        'patient_name' : 'Marta Sharapova',
        'address': ': 9 tennis court, new Russia, DC',
        'directions': 'Prednisone, Taper 5 mg every 3 days,\n'
                      '    Finish in 2.5 weeks a\n'
                      '    Lialda - take 2 pill everyday for 1 month',
        'medicines': 'Prednisone 20 mg\n    Lialda 2.4 gram',
        'patient_name': 'Marta Sharapova',
        'refill': '2'
    }
