import React from 'react';
import { Navbar, Container, Input, Button, NavbarBrand, Modal, ModalBody, Form } from 'reactstrap';
import './Header.css';

export const Header = (props) => {
    return (
        <Navbar color='dark'>
            <Container className='header-container'>
                <Input style={{display: 'inline-block', width: '30%'}} className='search' type='text' name='search-title' placeholder='Enter your search ...'></Input>
                <NavbarBrand href='/'>Techkids Hotgirls</NavbarBrand>
                {props.authUser.userId ? (
                    <div>Welcome, {props.authUser.username}</div>
                ) : (
                    <div className='button'>
                        <Button style={{marginRight: '10px'}} color='primary' onClick={props.login.toggle}>Login</Button>
                        <Button color='danger'>Register</Button>
                    </div>
                )}

                <Modal className='login-model' isOpen={props.loginModalVisible} toggle={props.login.toggle}>
                    <ModalBody>
                        <Form onSubmit>
                            <Input 
                                type='text' 
                                placeholder='Username' 
                                value={props.login.username}
                                onChange={(e) => props.login.loginInfoChange({username: e.target.value})} 
                            />

                            <Input
                                type='password' 
                                placeholder='Password' 
                                value={props.login.password}
                                onChange={(e) => props.login.loginInfoChange({password: e.target.value})} 
                            />

                            <Button onClick={props.login.submitForm}>Login</Button>
                            <Button onClick={props.login.loginWithFacebook}>Continue with Facebook</Button>
                        </Form>
                    </ModalBody>
                </Modal>
                
            </Container>
        </Navbar>
    )
}