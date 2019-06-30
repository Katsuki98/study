const express = require('express');
const userRouter = require('./users/routes');
const postRouter = require('./posts/routes');

const apiRouter = express.Router();

apiRouter.use('/api/users', userRouter);
apiRouter.use('/api/posts', postRouter);

module.exports = apiRouter;