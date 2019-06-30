import React from 'react';
import { Button, Modal, ModalBody, Input } from 'reactstrap';
import LoginModal from './LoginModal';

class RegisterModal extends React.Component {
  constructor (props) {
    super (props);
    this.state = {
      modal: false
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
        <Button color='danger' onClick={this.toggle}>Register</Button>
        <Modal isOpen={this.state.modal} toggle={this.toggle} className={this.props.className}>
          <ModalBody>
            <LoginModal/>
            <div className='container text-center'>
              <div className='row'>
                <div className='col-6'>
                  <img className='img-fluid mt-5' src='https://i.imgflip.com/1xxoxm.jpg' alt='not found'/>
                </div>
                <div className='col-6'>
                  <Button className='mt-2' color="primary" onClick={this.toggle}>Continue with Facebook</Button>
                  <p className='mt-2'>Or</p>
                  <Input className='user-name' type='text' name='user' placeholder='Enter user name'/>
                  <Input className='password mt-2' type='text' name='pass' placeholder='Enter your password'/>
                  <Input className='password mt-2' type='text' name='pass' placeholder='Enter your password'/>
                  <Button className='mt-2' color="info" onClick={this.toggle}>Register</Button>
                </div>
              </div>
            </div>
          </ModalBody>
        </Modal>
      </div>
    );
  }
}

export default RegisterModal;