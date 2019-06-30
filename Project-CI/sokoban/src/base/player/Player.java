package base.player;

import base.FrameCounter;
import base.GameObject;
import base.KeyEventPress;
import base.game.Settings;
import base.physics.BoxCollider;
import base.physics.Physics;
import base.renderer.BoxRenderer;

import java.awt.*;

public class Player extends GameObject implements Physics {
    BoxCollider boxCollider;
    FrameCounter moveCounter;
    public Player() {
        this.boxCollider = new BoxCollider(this.position, 16, 16);
        this.renderer = new BoxRenderer(this.boxCollider, Color.CYAN, true);
        this.position.set(210, 310);
        this.moveCounter = new FrameCounter(15);
    }

    @Override
    public void run() {
        this.move();
    }

    private void move() {
        if (KeyEventPress.isUpPress) {
            this.position.addThis(0, -Settings.WAY_SIZE);
        }
        if (KeyEventPress.isDownPress) {
            this.position.addThis(0, Settings.WAY_SIZE);
        }
        if (KeyEventPress.isLeftPress) {
            this.position.addThis(-Settings.WAY_SIZE, 0);
        }
        if (KeyEventPress.isRightPress) {
            this.position.addThis(Settings.WAY_SIZE, 0);
        }
    }

    @Override
    public BoxCollider getBoxCollider() {
        return this.boxCollider;
    }
}
