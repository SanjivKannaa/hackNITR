const fetch = (...args) =>
	import('node-fetch').then(({default: fetch}) => fetch(...args));
const express = require('express');
const app = express();
// var app = express.createServer();
const { auth } = require('express-openid-connect');
const { requiresAuth } = require('express-openid-connect');
app.set('views', __dirname + '/public');
app.engine('html', require('ejs').renderFile);



const config = {
  authRequired: false,
  auth0Logout: true,
  secret: 'a long, randomly-generated string stored in env',
  baseURL: 'https://hacknitr-project.sanjiv-kannaaka.repl.co',
  clientID: '6exgxDeNWCV4IEXAcxEHIJLnHYQvhais',
  issuerBaseURL: 'https://dev-t5z2g0pynzxghq4i.us.auth0.com'
};



app.use(auth(config));
// const checkJwt = auth({
//   audience: 'https://dev-t5z2g0pynzxghq4i.us.auth0.com/api/v2/',
//   issuerBaseURL: `localhost:5000`,
// });



app.get('/auth', (req, res) => {
  res.send(req.oidc.isAuthenticated() ? 'Logged in' : 'Logged out');
});


app.get('/previousQP_api', async function (req, res)  {
  // res.send(fetch('https://hackNITR-api.sanjiv-kannaaka.repl.co'));
	const url =
		'https://hackNITR-api.sanjiv-kannaaka.repl.co';
	const options = {
		method: 'GET'
	};
	// promise syntax
	fetch(url, options)
		.then(res => res.json())
		.then(json => console.log(json))
		.catch(err => console.error('error:' + err));
	try {
		let response = await fetch(url, options);
		response = await response.json();
		// res.status(200).json(response);
		res.send(response)
	} catch (err) {
		console.log(err);
		res.status(500).json({msg: `Internal Server Error.`});
	}
});


app.get('/previousQP', (req, res) => {
  res.render('qp.html');
});


// app.get('/', (req, res) => {
// 	res.send('Home Page')
// });


port = 5000
app.listen(port, () => {
	console.log('server started on port ', port);
});
