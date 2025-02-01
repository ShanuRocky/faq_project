import requests
import json

BASE_URL = 'http://localhost:8000/api'

def test_create_faq():
    url = f'{BASE_URL}/faqs/'
    data = {
        'question': 'What is the capital of France?',
        'answer': 'The capital of France is <b>Paris</b>.'
    }
    response = requests.post(url, data=data)
    print(f"Create FAQ: Status Code {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    return response.json()['id']

def test_get_faq(faq_id, lang=None):
    url = f'{BASE_URL}/faqs/{faq_id}/'
    if lang:
        url += f'?lang={lang}'
    response = requests.get(url)
    print(f"Get FAQ (lang={lang}): Status Code {response.status_code}")
    print(json.dumps(response.json(), indent=2))

def test_list_faqs(lang=None):
    url = f'{BASE_URL}/faqs/'
    if lang:
        url += f'?lang={lang}'
    response = requests.get(url)
    print(f"List FAQs (lang={lang}): Status Code {response.status_code}")
    print(json.dumps(response.json(), indent=2))

def test_supported_languages():
    url = f'{BASE_URL}/supported-languages/'
    response = requests.get(url)
    print(f"Supported Languages: Status Code {response.status_code}")
    print(json.dumps(response.json(), indent=2))

def run_tests():
    print("Testing FAQ System API")
    print("=====================")
    
    # Test supported languages
    print("\nTesting Supported Languages:")
    test_supported_languages()
    
    # Create a new FAQ
    print("\nCreating a new FAQ:")
    faq_id = test_create_faq()
    
    # Get the FAQ in different languages
    print("\nTesting FAQ retrieval in different languages:")
    test_get_faq(faq_id)
    test_get_faq(faq_id, 'fr')
    test_get_faq(faq_id, 'es')
    test_get_faq(faq_id, 'de')
    
    # List all FAQs in different languages
    print("\nListing all FAQs in different languages:")
    test_list_faqs()
    test_list_faqs('fr')
    test_list_faqs('es')

if __name__ == '__main__':
    run_tests()