package base.game;

import base.Background;
import base.GameObject;
import base.player.Player;
import base.scene.MenuScene;
import base.scene.Scene;
import base.scene.SceneManager;

import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;

public class GameCanvas extends JPanel {

    public GameCanvas() {  //hàm tạo
        Background background = GameObject.recycle(Background.class);
        Player player = GameObject.recycle(Player.class);
        this.setPreferredSize(new Dimension(Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT));
    }

    public void gameLoop() {
        int delay = 1000 / 60;
        long lastRun = 0;
        while (true) {
            long currentTime = System.currentTimeMillis();
            if (currentTime - lastRun > delay) {
                this.runAll();
                this.renderAll();
                lastRun = currentTime;
            }
        }
    }


    private void runAll() {
//        for (GameObject gameObject: GameObject.gameObjects) {
        for (int i = 0; i < GameObject.gameObjects.size(); i++) {
            GameObject gameObject = GameObject.gameObjects.get(i);
            if (gameObject.isActive) {
                gameObject.run();
            }
        }
        System.out.println(GameObject.gameObjects.size());
    }


    @Override // ghi đè method
    protected void paintComponent(Graphics g) {
//        for (GameObject gameObject: GameObject.gameObjects) {
        g.setColor(Color.black);
        g.fillRect(0, 0, Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT);
        for (int i = 0; i < GameObject.gameObjects.size(); i++) {
            GameObject gameObject = GameObject.gameObjects.get(i);
            if (gameObject.isActive) {
                gameObject.render(g);
            }
        }
    }


    private void renderAll() {
        this.repaint();
    }
}
