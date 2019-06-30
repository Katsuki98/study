const express = require('express');
const authRouter = express.Router();
const bcryptjs = require('bcryptjs');
const userModel = require('../users/model');
const admin = require('firebase-admin');

authRouter.post('/register', async (req, res) => {
    try {
        const userInfo = req.body;

        //hash password
        const hashPassword = bcryptjs.hashSync(userInfo.password, 10);

        //save to database
        const newUser = new userModel({
            ...userInfo,
            password: hashPassword,
        });
        await newUser.save();
        res.status(201).json({
            id: newUser._id,
        });
    } catch (error) {
        res.status(error.status || 500).end(error.message || 'Internal server error');
    }
});

authRouter.post('/login', async (req, res) => {
    try {
        const username = req.body.username;
        const password = req.body.password;

        const exitsUser = await userModel.findOne({username: username}).exec();
        if (exitsUser) {
            //check user
            if (bcryptjs.compareSync(password, exitsUser.password)) {
                //save user to session storage
                req.session.authUser = {
                    id: exitsUser._id,
                    username: exitsUser.username,
                    fullName: exitsUser.fullName,
                };
                req.session.save();
                
                res.status(200).json({
                    success: true,
                    message: 'Login success',
                    userId: exitsUser.id,
                    username: exitsUser.username,
                });
            } else {
                res.status(200).json({
                    success: false,
                    message: 'Password is not correct'
                });
            }
        } else {
            res.status(404).json({
                success: false,
                message: 'Username not found'
            });
        }
    } catch (error) {
        res.status(error.status || 500).end(error.message || 'Internal server error');
    }
})

authRouter.post('facebookOauth', async (req, res) => {
    try {
        const idToken = req.body.idToken;
        const result = await admin.auth().verifyIdToken(idToken);
        console.log(result);

        res.status(200).json({
            success: true,
        });
    } catch (error) {
        res.status(error.status || 500).end(error.message || 'Internal server error');
    }
})

module.exports = authRouter;