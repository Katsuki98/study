import React from 'react';

// class TodoList extends React.Component {
//     state = {
//         todos: [
//             {content: 'Manga', finish: false},
//             {content: 'Anime', finish: true},
//         ],
//     };
//     render () {
//         return (
//             <div>
//                 <p>{this.todos[0].content}</p>
//             </div>
//         );
//     }
// }

const TodoList = (props) => {
    //condition && trueCode
    return (
        <div>
            <h3>Todo List</h3>
            <div>
                {props.todoItems.map((item) => {
                    return( item.finished ? (
                        <p key={item.id}>
                        <del>{item.content}</del>
                        <button onClick={() => {props.deleteItem(item.id)}}>DELETE</button>
                        </p>
                        ) : (
                        <p key={item.id}>{item.content} 
                            <button onClick={() => {props.updateItem(item.id)}}>DONE</button>
                            <button onClick={() => {props.deleteItem(item.id)}}>DELETE</button>
                        </p>
                        )
                    );
                })}
            </div>
        </div>
    );
};

export default TodoList;