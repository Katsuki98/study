import React from 'react';

const Posts = (props) => {
    return (
        props.posts.map((post) => {
            return (
            <div className='col-3' style={{display:'inline-block'}}>
            <img className='img-fluid mt-2'  src = {post.url} alt ='Img not found' />
            <h3>{ post.title }</h3>
            <p>{ post.description }</p>
            </div>
            );
        })

    );
};

export default Posts;