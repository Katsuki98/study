package base.player;

import base.GameObject;
import base.Vector2D;
import base.enemy.Enemy;
import base.game.Settings;
import base.renderer.AnimationRenderer;
import base.renderer.SingleImageRenderer;
import tklibs.SpriteUtils;

import java.awt.image.BufferedImage;
import java.util.ArrayList;

public class PlayerBulletType2 extends PlayerBullet {
    public PlayerBulletType2() {
        super();
        this.createRenderer();
        this.velocity.set(0, -5);
    }

    private void createRenderer() {
        ArrayList<BufferedImage> images = SpriteUtils.loadImages(
                "assets/images/enemies/bullets/cyan.png",
                "assets/images/enemies/bullets/blue.png",
                "assets/images/enemies/bullets/green.png",
                "assets/images/enemies/bullets/red.png"
        );
        this.renderer = new AnimationRenderer(images);
    }

    @Override
    public void run() {
        super.run();
        this.moveToEnemy();
    }

    private void moveToEnemy() {
        //enemy
        Enemy enemy = null;
        for (GameObject gameObject : GameObject.gameObjects) {
            if (gameObject.isActive && gameObject instanceof Enemy) {
                enemy = (Enemy) gameObject;
                break;
            }
        }
        if (enemy != null) {
            //enemy.position
            Vector2D enemyPosition = enemy.position;
            Vector2D result = enemyPosition.substract(this.position);
            result.addThis(this.velocity);
            result.setLength(5);
            this.velocity.set(result);
        }
    }
}
