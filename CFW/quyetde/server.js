const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const app = express();
const mongoose = require('mongoose');
const QuestionModel = require('./models/question');

mongoose.connect('mongodb://localhost:27017/web18', (error) => {
    if(error) {
        console.log(error);
    } else{
        console.log('Connect to mongodb success');
    }
});

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(express.static('public'));

//router for page
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/html/index.html');
});

app.get('/ask', (req, res) => {
    res.sendFile(__dirname + '/public/html/ask.html');
});

app.get('/answer/:questionId', (req, res) => {
    res.sendFile(__dirname + '/public/html/answer.html');
});

//router for json data
// get => get DataCue
// post => create new
// put => update Data
// delete => delete data
app.post('/api/questions', async(req, res) => {
	try {
		const { questionContent } = req.body;
		const newQuestion = {
			content: questionContent,
			yes: 0,
            no: 0,
			createdAt: new Date(),
        }
        const result = await QuestionModel.create([newQuestion]);
        console.log(result);

		res.json({
			success: true,
		});
	} catch (error) {
		res.json({
			success: false,
			message: error.message,
		});
	}
});

app.get('/api/questions/getRandomQuestion', (req, res) => {
	try {
		let questions = [];
		try {
			questions = JSON.parse(fs.readFileSync("database.json"));
		} catch (error) {
			console.log(error);
			res.status(500).end(error.message);
		}

		const randomNumber = Math.floor(Math.random() * questions.length)
		const randomQuestion = questions[randomNumber];

		res.json(randomQuestion);
	} catch (error) {
		res.json({
			success: false,
			message: error.message,
		});
	}
});

app.get('/api/questions/getQuestionById/:questionId', (req, res) => {
	try {
		const { questionId } = req.params;

		let questions = [];
		try {
			questions = JSON.parse(fs.readFileSync("database.json"));
		} catch (error) {
			console.log(error);
			res.status(500).end(error.message);
		}

		const seletedQuestion = questions.filter((item) => item.id.toString() === questionId.toString())[0];
		if (seletedQuestion) {
			res.json(seletedQuestion);
		} else {
			res.json({
				success: false,
				message: 'Question not found'
			});
		}
	} catch (error) {
		res.json({
			success: false,
			message: error.message,
		});
	}
});

app.put('/api/questions', (req, res) => {
	try {
		const questionId = req.body.questionId;
		const vote = req.body.vote;

		let questions = [];
		try {
			questions = JSON.parse(fs.readFileSync("database.json"));
		} catch (error) {
			console.log(error);
			res.status(500).end(error.message);
		}
		questions.forEach((item) => {
			if (item.id.toString() === questionId.toString()) {
				vote === 'yes' ? item.yes += 1 : item.no += 1;
			}
		});
		fs.writeFileSync("database.json", JSON.stringify(questions));
		
		res.json({
			success: true,
		});
	} catch (error) {
		res.json({
			success: false,
			message: error.message,
		});
	}
});

// app.get("/api/questions", (req, res) => {
//     const { questionId, result } = req.params;
//     let questions = [];
//     try {
//         questions = JSON.parse(fs.readFileSync("database.json"));
//     } catch (error) {
//         console.log(error);
//     }
//     questions.forEach((item, index) => {
//         if(item.id == questionId) {
//             result === 'yes' ? questions[index].yes += 1 : questions[index].no += 1;
//         }
//     });
//     fs.writeFileSync("database.json", JSON.stringify(questions));
//     res.redirect("/questions/${}");
// })

// app.get("/question/:questionId", async(req, res) => {
//     const { questionId } = req.params;
//     let questions = [];
//     try {
//         questions = JSON.parse(fs.readFileSync("database.json"));
//         console.log(questions);
//     } catch (error) {
//         console.log(error);
//     }
//     const selectedQuestion = questions.filter((item) => item.id === questionId)[0];
//     if(selectedQuestion) {
//         const yesPercent = Math.round(selectedQuestion.yes / (selectedQuestion.yes + selectedQuestion.no) * 100).toFixed(2);
//         const noPercent = 100 - yesPercent;
//         res.send(`
//         <h1>${selectedQuestion.content}</h1>
//         <p>${selectedQuestion.yes + selectedQuestion.no}</p>
//         <p>Yes: ${yesPercent}%</p>
//         <p>No: ${noPercent}%</p>
//         `);
//     } else {
//         res.status(404).end('Could not find the question');
//     }
// });




// // app.get('/vote/yes/:questionId', (req, res) => {
// //     const { questionId } = req.params;
// //     let questions = [];
// //     try {
// //         questions = JSON.parse(fs.readFileSync('database.json'));
// //     } catch (error) {
// //         // console.log(error);
// //     }
// //     // const question = questions.index;
// //     // const question = questions.filter(item => item.id === questionId)[0];
// //     questions.forEach((item, index) => {
// //         console.log(item, questionId)
// //         if(item.id == questionId) {
// //             questions[index].yes += 1;
// //         }
// //     });
// //     fs.writeFileSync('database.json', JSON.stringify(questions));
// //     res.redirect('/');
// // });

// app.get('/getTotalQuestions', (req, res) => {
//     console.log('Request received');
//     let questions = [];
//     try {
//         questions = JSON.parse(fs.readFileSync("database.json"));
//     } catch (error) {
//         console.log(error);
//     }
//     res.status(200).send({totalQuestions: questions.length});
// });

// app.get('/vote/no/:questionId', (req, res) => {
    
// })

// app.get('/ask', (req, res) => {
//     res.sendFile(__dirname + '/public/ask.html');
// });

// app.post('/addquestion', (req, res) => {
//     console.log('Sent');
//     console.log(req.body);
//     // const questionContent = req.body.questionContent;
//     const { questionContent } = req.body;
//     let questions = [];
//     try {
//         questions = JSON.parse(fs.readFileSync('database.json'));
//     } catch (error) {
//         console.log(error);
//     }
//     console.log(questions);
//     const newQuestion = {
//         id: questionContent.length,
//         content: questionContent,
//         yes: 0,
//         no: 0,
//     }
//     questions.push(newQuestion);
//     fs.writeFileSync('database.json', JSON.stringify(questions));
//     res.redirect('/');
// });

app.listen('4869', (err) => {
    if(err) console.log(err)
    else console.log('Server start success');
});

