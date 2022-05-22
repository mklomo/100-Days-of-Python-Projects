from tkinter import *

import requests

URI = "https://api.kanye.rest/"

def get_quote():
    """
    This function sends a request to the URI and returns the text to the canvas
    """
    response = requests.get(URI)
    # Raise an exception if something goes wrong
    response.raise_for_status()
    # Save the response data
    data_quote_response = response.json()["quote"]
    canvas.itemconfig(quote_text, text=data_quote_response)



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
