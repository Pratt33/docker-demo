from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		user_input = request.form.get('user_input', '')
		return f"You entered: {user_input}"
	return '''
		<form method="post">
			<input type="text" name="user_input" placeholder="Enter something">
			<input type="submit" value="Submit">
		</form>
	'''

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True) #0.0.0.0 ensures the app is accessible from outside the container
