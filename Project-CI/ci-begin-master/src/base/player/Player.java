package base.player;

import base.*;
import base.action.Action;
import base.game.GameCanvas;
import base.game.Settings;
import base.physics.BoxCollider;
import base.physics.Physics;
import base.renderer.AnimationRenderer;
import base.renderer.SingleImageRenderer;
import base.scene.GameOverScene;
import base.scene.SceneManager;
import tklibs.SpriteUtils;

import java.awt.image.BufferedImage;
import java.util.ArrayList;

public class Player extends GameObject implements Physics {
    Action action;
    BoxCollider boxCollider;
    public int health;
    public Player() {
        super();
//        BufferedImage image = SpriteUtils.loadImage("assets/images/players/straight/0.png");
//        this.renderer = new SingleImageRenderer(image);
        this.createRenderer();
        this.position.set(200, 300);
        this.boxCollider = new BoxCollider(this.position, 32, 48);
        this.health = 3;
        this.action = new ActionFire(3);
    }

    private void createRenderer() {
        //ArrayList<BufferedImage> images
        ArrayList<BufferedImage> images = new ArrayList<>();
        images.add(SpriteUtils.loadImage("assets/images/players/straight/0.png"));
        images.add(SpriteUtils.loadImage("assets/images/players/straight/1.png"));
        images.add(SpriteUtils.loadImage("assets/images/players/straight/2.png"));
        images.add(SpriteUtils.loadImage("assets/images/players/straight/3.png"));
        images.add(SpriteUtils.loadImage("assets/images/players/straight/4.png"));
        images.add(SpriteUtils.loadImage("assets/images/players/straight/5.png"));
        images.add(SpriteUtils.loadImage("assets/images/players/straight/6.png"));
        //AnimationRenderer(images)
        this.renderer = new AnimationRenderer(images);
    }

    @Override
    public void run() {
        this.move(); //change velocity
        this.action.run(this);
        super.run(); //this.position.addThis(this.velocity)
    }

    private void move() {
        int vx = 0;
        int vy = 0;
        if (KeyEventPress.isUpPress && this.position.y > 0) {
            vy -= 4;
        }
        if (KeyEventPress.isDownPress && this.position.y < 510) {
            vy += 4;
        }
        if (KeyEventPress.isLeftPress && this.position.x > 0) {
            vx -= 4;
        }
        if (KeyEventPress.isRightPress && this.position.x < Settings.BACKGROUND_WIDTH - 30) {
            vx += 4;
        }
        this.velocity.set(vx, vy);
    }



    @Override
    public BoxCollider getBoxCollider() {
        return this.boxCollider;
    }

    @Override
    public void destroy() {
        super.destroy();
        SceneManager.signNewScene(new GameOverScene());
    }
}
