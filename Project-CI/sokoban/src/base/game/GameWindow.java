package base.game;

import base.KeyEventPress;

import javax.swing.*;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class GameWindow extends JFrame {
    public GameWindow() {
        this.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        this.setTitle("Game Touhou");
        this.setResizable(false);
        this.addKeyEvent();
    }

    private void addKeyEvent() {
        this.addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                KeyEventPress.isAnyKeyPress = true;
                if(e.getKeyCode() == Settings.UP_BUTTON) {
                    KeyEventPress.isUpPress = true;
                }
                if(e.getKeyCode() == Settings.DOWN_BUTTON) {
                    KeyEventPress.isDownPress = true;
                }
                if(e.getKeyCode() == Settings.LEFT_BUTTON) {
                    KeyEventPress.isLeftPress = true;
                }
                if(e.getKeyCode() == Settings.RIGHT_BUTTON) {
                    KeyEventPress.isRightPress = true;
                }
            }

            @Override
            public void keyReleased(KeyEvent e) {
                KeyEventPress.isAnyKeyPress = false;
                if(e.getKeyCode() == Settings.UP_BUTTON) {
                    KeyEventPress.isUpPress = false;
                }
                if(e.getKeyCode() == Settings.DOWN_BUTTON) {
                    KeyEventPress.isDownPress = false;
                }
                if(e.getKeyCode() == Settings.LEFT_BUTTON) {
                    KeyEventPress.isLeftPress = false;
                }
                if(e.getKeyCode() == Settings.RIGHT_BUTTON) {
                    KeyEventPress.isRightPress = false;
                }
            }
        });
    }
}
