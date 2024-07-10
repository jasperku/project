import os
import openai

# connect to openai
    # read local .env file
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

#openai.api_key = os.getenv("OPENAI_API_KEY")

## for azure 
openai.api_type = "azure"
openai.api_base = "https://iemopenai.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion_from_messages(messages, engine="gpt35turbo-demo", temperature=0):
    
# azure connection     
    response = openai.ChatCompletion.create(engine=engine, messages=messages, temperature=temperature)
    
    return response.choices[0].message["content"]

# use openai
'''
def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
    )

    return response.choices[0].message["content"]
'''

# user talks to the chat box
# assistant responds 
def collect_messages(_):

    inp2.visible = False

    prompt = inp1.value_input
    inp1.value = ''



    context.append({'role':'user', 'content':f"{prompt}"})

    response = get_completion_from_messages(context)

    context.append({'role':'assistant', 'content':f"{response}"})
  
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600)))

    


    #
    messages =  context.copy()

    messages.append(
    {'role':'system', 'content':'If the order is complete respond with only one word True or False.'},
    )

    response = get_completion_from_messages(messages, temperature=0)
    #


    if response == "True":

      #
      messages =  context.copy()
      
      messages.append(
      {'role':'system', 'content':'create a json summary of the previous food order. Itemize the price for each item\
       The fields should be 1) pizza, include size 2) list of toppings 3) list of drinks, include size   4) list of sides include size  5)total price '},
      )

      response = get_completion_from_messages(messages, temperature=0)
      #


      #Tell order summary
      #
      messages =  context.copy()
      
      messages.append(
      {'role':'system', 'content':'Translate summary to html with divs include price'},
      )

      response = get_completion_from_messages(messages, temperature=0)

      panels.append(
          pn.Row('Assistant:', pn.pane.HTML(response)))
      #
   



      #
      messages =  context.copy()
      
      messages.append(
      {'role':'system', 'content':'If you have thanked the customer respond with only one word Valid or notValid.'},
      )

      response = get_completion_from_messages(messages, temperature=0)

      print(response)


      if response == "Valid" :

        #Show Payment
        
        inp2.visible = True
        #
    
    

    return pn.Column(*panels)




import panel as pn
pn.extension()

panels = []

context = [ {'role':'system', 'content':"""
You are OrderBot, an automated service to collect orders for a pizza restaurant. \
You first greet the customer, then collects the order. \
You wait to collect the entire order, then summarize it \
Make sure to clarify all options, extras and sizes to uniquely \
identify the item from the menu.\
After the options have been discussed thank the customer. \
You respond in a short, very conversational friendly style. \
The menu includes \
pepperoni pizza  12.95, 10.00, 7.00 \
cheese pizza   10.95, 9.25, 6.50 \
eggplant pizza   11.95, 9.75, 6.75 \
fries 4.50, 3.50 \
greek salad 7.25 \
Toppings: \
extra cheese 2.00, \
mushrooms 1.50 \
sausage 3.00 \
canadian bacon 3.50 \
AI sauce 1.50 \
peppers 1.00 \
Drinks: \
coke 3.00, 2.00, 1.00 \
sprite 3.00, 2.00, 1.00 \
bottled water 5.00 \
"""} ]  # accumulate messages

inp1 = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')

inp2 = pn.widgets.Button(name="Pay")
button_conversation = pn.widgets.Button(name="Chat!")

inp2.visible = False

interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    inp1,
    inp2,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=400),
    sizing_mode="stretch_width",  # Set sizing_mode to stretch_width to allow horizontal stretching
)

scrollable_dashboard = pn.panel(dashboard, scroll=True, height=600)  # Use scroll=True to enable vertical scrolling

inp2.on_click(collect_messages)

# Serve
pn.template.FastListTemplate(
    site="Panel", title="Pizza House", main=[scrollable_dashboard],  # Use scrollable_dashboard instead of dashboard
).servable()
