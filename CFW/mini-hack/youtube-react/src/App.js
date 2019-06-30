import React, { Component } from 'react';
import { Logo } from './components/Logo';
import './App.css';
import { SearchInput } from './components/SearchInput';
import { ListItem } from './components/ListItem';

class App extends Component {
  state = {
    loading: false,
    searchInput: '',
    result: [],
    nextPageToken: '',
  };

  componentDidMount() {
    window.addEventListener('scroll', () => {
      console.log(window.scrollY);
    })
  }

  handleInputChange = async (newSearchInput) => {
    this.setState({
      searchInput: newSearchInput,
      leading: true,
    });

    const result = await fetch(`https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q=${newSearchInput}&type=video&key=AIzaSyA9gQZ-oYomFypZN7PsupZJtOfQqA6Q3qw`, {
      method: 'GET',
    }).then((res) => res.json());
    console.log(result);

    this.setState({
      loading: false,
      nextPageToken: result.nextPageToken,
      result: [...this.state.result, ...result.items],
    });
  }

  render() {
    return (
      <div className="App container">
        <Logo/>

        <SearchInput handleInputChange={this.handleInputChange} />

        {this.state.loading && (
          <div className='row'>
            <div className='col-md-12 text-center'>
              <div class="spinner-border" role="status">
                <span class="sr-only">Loading...</span>
              </div>
            </div>
          </div>
        )}

        {this.state.result.map((item, index) => {
          return(<ListItem key={index} item={item}/>);
        })}
      </div>
    );
  }
}

export default App;
