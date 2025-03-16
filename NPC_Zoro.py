import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import json
import importlib

def read_and_assign_variables(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()

            # Assign each line to a variable
            k = lines[0].strip()
            m = lines[1].strip()
            d = lines[2].strip()
            g = lines[3].strip()

            return k, m,d,g
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")


def fetch_data_from_website(url):
    try:
        # Send a GET request to the website
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("Data fetched successfully!")
            # Print the content of the page
            return(response.text)  # or response.content for binary data
        else:
            return(f"Failed to fetch data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        return(f"An error occurred: {e}")

k,a,d,g = read_and_assign_variables("Preprocess_data.txt")
gni = importlib.import_module(a)
# Function to  chatbot processing based on user input
def chatbot_response(user_input, crop_data):
    # Tokenizing the input text
    tokens = word_tokenize(user_input.lower())
    
    # Removing stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    # Check for crop name in user input
    crop_mentioned = [word for word in filtered_tokens if word in crop_data]
    
    if crop_mentioned:
        crop = crop_mentioned[0]
        crop_info = crop_data[crop]
        
        # Check if the soil type is mentioned
        soil_type = None
        for word in filtered_tokens:
            if word in ['loamy', 'clay', 'sandy']:
                soil_type = word
        
        # Provide feedback based on the input
        response = f"You're interested in growing {crop}."
        
        if soil_type:
            if soil_type == crop_info['ideal_soil']:
                response += f" The soil type {soil_type} is perfect for {crop}."
            else:
                response += f" The soil type {soil_type} is not ideal for {crop}. Try {crop_info['ideal_soil']} soil."
        
        # Add more insights based on temperature and rainfall
        response += f" Ideal temperature for {crop} is {crop_info['ideal_temp']}°C."
        response += f" You need {crop_info['rainfall']} rainfall for best yield."
        response += f" Market price for {crop} is approximately {crop_info['price']} per unit."
        response += f" Ideal pH for {crop} is {crop_info['pH']}."
        response += f" Fertilizer usage should be {crop_info['fertilizer']}."
        
        return response
    
    else:
        return "Sorry, I couldn't find any relevant crop information. Could you specify the crop?"



gni.configure(api_key=k)
def ask_ai(prompt):
    try:
        model = gni.GenerativeModel(g)  
        response = model.generate_content(f"{d}:Now answer: {prompt}")
        
        if response and response.text:
            return response.text.strip()
        else:
            return "Sorry, I couldn't process that request."
    except Exception as e:
        return f"Error: {e}"
# Function to  periodic updates
def periodic_update():
    # Periodic update simulation, can be expanded to fetch from a live source
    new_data = crop_data
    return new_data

# Function to  error handling
def handle_error(error_type):
    if error_type == "invalid_input":
        return "Sorry, I didn't quite understand that. Could you rephrase?"
    elif error_type == "no_crop_found":
        return "It looks like I couldn't find the crop in the system. Please try another crop."
    else:
        return "An unknown error occurred. Please try again later."

# Main function  user interaction
def start_conversation():
    print("Hello, I am your farming assistant. Ask me about crops!")
    print("Example: 'Tell me about wheat' or 'What about rice in clay soil?'")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "exit":
            print("Goodbye! Happy farming!")
            break
        
        try:
            response = chatbot_response(user_input, crop_data)
            if "Error" in response:
                response = "I couldn't process this request for now"
            print("Bot:", response)
        except Exception as e:
            print("Bot:", handle_error("invalid_input"))

# a periodic fetch of new agricultural data every 5 iterations
def fetchperiod():
    fetch_count = 0
    while fetch_count < 5:
        start_conversation()
        fetch_count += 1
        if fetch_count % 2 == 0:  #  periodic update every 2nd iteration
            crop_data = periodic_update()




def chatbot():
    print("The Agrarian Alchemist-NPC:Zoro ")
 
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Zoro: Goodbye! Happy farming!")
            break
        
        response = ask_ai(user_input)
        if "Error" in response:
                response = "Don't Rush! One Step at a time"
        print(f"Zoro: {response}")

if __name__ == "__main__":
    chatbot()
