const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const userRouter = require('./api/users/routes');
const postRouter = require('./api/posts/routes');
const authRouter = require('./api/auth/routes');
const expressSession = require('express-session');
const cors = require('cors');
const admin = require('firebase-admin');

const bootstrap = async () => {
    try {
        //init app
        const app = express();

        //connect mongodb
        await mongoose.connect('mongodb://localhost:27017/techkids-hotgirl');
        
        const serviceAccount = require("./techkids-hotgirl-ab932-firebase-adminsdk-r7wdb-deeb0037ed.json");
        admin.initializeApp({
            credential: admin.credential.cert(serviceAccount),
            databaseURL: "https://techkids-hotgirl-ab932.firebaseio.com"
        });


        //user middlewares + routers
        app.use(cors({
            origin: ['http://localhost:3001', 'http://localhost:3000'],
            credentials: true,
        }));
        app.use(expressSession({
            secret: 'keyboard cat',
            resave: false,
            saveUninitialized: true,
        }));
        app.use(bodyParser.urlencoded({ extended: false }));
        app.use(bodyParser.json());
        app.use('/api/users', userRouter);
        app.use('/api/posts', postRouter);
        app.use('/api/auth', authRouter);

        //start server
        await app.listen(process.env.PORT || 3001);
        console.log(`Server listen on POST ${process.env.PORT || 3001} ...`);
    } catch (error) {
        console.log('Error happen: ', error);
    }
}

bootstrap();