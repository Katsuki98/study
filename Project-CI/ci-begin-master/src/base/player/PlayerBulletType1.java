package base.player;

import base.game.Settings;
import base.renderer.AnimationRenderer;
import tklibs.SpriteUtils;

import java.awt.image.BufferedImage;
import java.util.ArrayList;

public class PlayerBulletType1 extends PlayerBullet {
    public PlayerBulletType1() {
        super();
//        BufferedImage image = SpriteUtils.loadImage("assets/images/player-bullets/a/0.png");
//        this.renderer = new SingleImageRenderer(image);
        this.createRenderer();
    }

    private void createRenderer() {
        ArrayList<BufferedImage> images = SpriteUtils.loadImages(
                "assets/images/player-bullets/a/0.png",
                "assets/images/player-bullets/a/1.png",
                "assets/images/player-bullets/a/2.png",
                "assets/images/player-bullets/a/3.png"
        );
        this.renderer = new AnimationRenderer(images);
    }

}
