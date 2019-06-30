import React, { Component } from 'react';
import './App.css';
import TodoList from './components/TodoList';
import CreateTodoForm from './components/CreateTodoForm';

class App extends Component {
  state = {
    todoItems: [
      {id: 0, content: 'Trans', finished: false, createdAt: new Date()},
      {id: 1, content: 'Read', finished: false, createdAt: new Date()},
      {id: 2, content: 'Edit', finished: true, createdAt: new Date()},
      {id: 3, content: 'Dev', finished: true, createdAt: new Date()},
      {id: 4, content: 'Code', finished: false, createdAt: new Date()},
    ],
  };

  addItem = (input) => {
    this.setState({
      todoItems: [...this.state.todoItems, {id: this.state.todoItems.length, content: input.newItem, finished: false, createAt: new Date()}],
    });
  };
  
  updateItem = (itemId) => {
    this.setState({
      todoItems: this.state.todoItems.map((item) => {
        if (item.id === itemId) {
          const newItemInfo = {
            ...item,
            finished: true,
          };

          return newItemInfo;
        } else {
          return item;
        }
      }),
    });
  };

  deleteItem = (itemId) => {
    this.setState({
      todoItems: this.state.todoItems.filter((item) => {
        if (item.id === itemId) {
          return false;
        } else {
          return true;
        }
      }),
    });
  };

  render() {
    return (
      <div className="App">
        <TodoList 
          todoItems={this.state.todoItems} 
          updateItem={this.updateItem}
          deleteItem={this.deleteItem}
        />
        <CreateTodoForm addItem={this.addItem}/>
      </div>
    );
  }
}

export default App;
