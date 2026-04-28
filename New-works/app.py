from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return '''
        <h2>Enter a Number</h2>
        <form action="/check">
            <input type="number" name="n" required>
            <button type="submit">Check</button>
        </form>
    '''

@app.route("/check")
def check():
    n = int(request.args.get("n"))

    if n >= 10:
        return f'''
            <h3>n is greatest</h3>
            <h4>Give your review</h4>
            <form action="/review" method="post">
                <input type="text" name="review" placeholder="Enter your review" required>
                <button type="submit">Submit Review</button>
            </form>
        '''
    else:
        return f'''
            <h3>n is not greatest</h3>
            <h4>Give your review</h4>
            <form action="/review" method="post">
                <input type="text" name="review" placeholder="Enter your review" required>
                <button type="submit">Submit Review</button>
            </form>
        '''

@app.route("/review", methods=["POST"])
def review():
    user_review = request.form.get("review")

    return f'''
        <h3>Review submitted successfully ✅</h3>
        <p>Your review: {user_review}</p>
        <p>Thanks for your feedback! 😊</p>
        <a href="/">Go back</a>
    '''

app.run(host="0.0.0.0", port=5000)
