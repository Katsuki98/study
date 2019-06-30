package base.enemy;

import base.FrameCounter;
import base.GameObject;
import base.action.Action;
import base.action.ActionParallel;
import base.game.GameCanvas;
import base.game.Settings;
import base.physics.BoxCollider;
import base.physics.Physics;
import base.renderer.AnimationRenderer;
import base.renderer.SingleImageRenderer;
import tklibs.SpriteUtils;

import javax.print.DocFlavor;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.util.ArrayList;
import java.util.Objects;


public class Enemy extends GameObject implements Physics {
    BoxCollider boxCollider;
    FrameCounter fireCounter;
    int hp;
    boolean immune;
    FrameCounter immuneCounter;
    Action action;

    public Enemy() {
        super(); //kế thừa hàm tạo bên GameObject(image, position)
        this.position.set(50, 50);
        this.velocity.set(0, 3);
        this.createRender();
        this.fireCounter = new FrameCounter(20);
        this.boxCollider = new BoxCollider(this.position, 28, 28);
        this.hp = 3;
        this.immune = false;
        this.immuneCounter = new FrameCounter(120);
        this.action = this.createAction();
    }

    private Action createAction() {
        Action actionRun = new Action() {
            @Override
            public boolean run(GameObject master) {
                master.velocity.set(1, 0);
                if (master.position.x > Settings.SCREEN_WIDTH * 3/4) {
                    return true;
                } else {
                    return false;
                }
            }

            @Override
            public void reset() {
            }
        };
        Action actionFire = new Action() {
            @Override
            public boolean run(GameObject master) {
                Enemy enemy = (Enemy) master;
                enemy.fire();
                return false;
            }

            @Override
            public void reset() {
                fireCounter.reset();
            }
        };
        Action actionParallel = new ActionParallel(actionRun, actionFire);
        return actionParallel;
    }

    private void createRender() {
        ArrayList<BufferedImage> images = SpriteUtils.loadImages(
                "assets/images/enemies/level0/blue/0.png",
                "assets/images/enemies/level0/blue/1.png",
                "assets/images/enemies/level0/blue/2.png",
                "assets/images/enemies/level0/blue/3.png"
        );
        this.renderer = new AnimationRenderer(images);
    }

    @Override
    public void run() {
        super.run();
//        if (this.position.y >= 300) {
//            this.velocity.set(0, 0);
//        }
//        this.fire();
        this.action.run(this);
    }


    private void fire() {
        if (this.fireCounter.run()) {
            EnemyBullet enemyBullet = GameObject.recycle(EnemyBullet.class);
            enemyBullet.position.set(this.position);
            this.fireCounter.reset();
        }
    }

    public void takeDamage(int damage) {
        if (this.immune)
            return;
        this.hp -= damage;
        if (this.hp <= 0) {
            this.hp = 0;
            this.destroy();
        } else {
            this.immune = true;
            this.immuneCounter.reset();
        }
    }

    @Override
    public void destroy() {
        super.destroy();
        EnemyExplosion explosion = GameObject.recycle(EnemyExplosion.class);
        explosion.position.set(this.position);
    }

    @Override
    public void reset() {
        super.reset();
        this.velocity.set(0, 3);
        this.immune = false;
        this.immuneCounter.reset();
        this.hp = 3;
    }

    @Override
    public BoxCollider getBoxCollider() {
        return this.boxCollider;
    }

    @Override
    public void render(Graphics g) {
        if (this.immune) {
            if (this.immuneCounter.run()) {
                this.immune = false;
            }
            if (this.immuneCounter.count % 4 == 0) {
                super.render(g);
            }
        } else {
            super.render(g);
        }
    }
}
