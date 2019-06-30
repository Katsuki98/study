import React from 'react';
import { Button, Modal, ModalBody, Input } from 'reactstrap';

class LoginModal extends React.Component {
  constructor (props) {
    super (props);
    this.state = {
      modal: false,
    };
    this.toggle = this.toggle.bind(this);
  }

  toggle() {
    this.setState(prevState => ({
      modal: !prevState.modal
    }));
  }

  render() {
    return (
      <div>
        <Button style={{marginRight: '20px'}} color='info' onClick={this.toggle}>Login</Button>
        <Modal isOpen={this.state.modal} toggle={this.toggle} className={this.props.className}>
          <ModalBody>
            <h2>Login</h2>
            <Input className='user-name' type='text' name='user' placeholder='Enter user name'/>
            <Input className='password mt-2' type='text' name='pass' placeholder='Enter your password'/>
            <Button className='mt-2' color="primary" onClick={this.toggle}>Login</Button>
          </ModalBody>
        </Modal>
      </div>
    );
  }
}

export default LoginModal;