import argparse
import google.generativeai as genai

def search(query):
    api_key = 'AIzaSyDzjP-c_fUAjiKybq81Rd-leQSejOaqO7I'
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(f"Give decluttered answer possible. What's: {query}")
    return response.text

def main():
    parser = argparse.ArgumentParser(description='Search the internet from the terminal')
    parser.add_argument('query', nargs='+', help='Search query')
    args = parser.parse_args()
    query = ' '.join(args.query)
    result = search(query)
    print(result)

if __name__ == '__main__':
    main()