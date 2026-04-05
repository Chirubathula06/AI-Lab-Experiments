import wikipedia
import wolframalpha

# Initialize WolframAlpha client
app_id = "542P7PXX8Q"
client = wolframalpha.Client(app_id)

while True:
    query = input("Ask me (or type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    # Try WolframAlpha
    try:
        res = client.query(query)
        answer = next(res.results).text
        print("WolframAlpha:", answer)
    except:
        # Try Wikipedia
        try:
            print("Wikipedia:", wikipedia.summary(query, sentences=2))
        except:
            print("Sorry, I could not find an answer.")  
