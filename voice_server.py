from flask import Flask, Response

app = Flask(__name__)

@app.route("/voice", methods=["GET"])
def voice_response():
    xml_response = """
    <Response>
        <Say language="hin-IN" voice="female">
            Namaste! Hamare dukan par is hafte vishesh chhoot mil rahi hai.
            Kapdon par 30 pratishat tak ki chhoot sirf Ravivaar tak. Dhanyavaad!
        </Say>
    </Response>
    """
    return Response(xml_response.strip(), mimetype='text/xml')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
