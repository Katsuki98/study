package base;

import base.game.Settings;

import java.awt.*;

public class Background extends GameObject {
    @Override
    public void render(Graphics g) {
        g.setColor(Color.RED);
        for (int i = 0; i < Settings.ROW_COUNT; i++) {
            g.drawLine(0, i * Settings.WAY_SIZE, Settings.SCREEN_WIDTH,i * Settings.WAY_SIZE);
        }
        for (int i = 0; i < Settings.COL_COUNT; i++) {
            g.drawLine(i * Settings.WAY_SIZE, 0, i * Settings.WAY_SIZE, Settings.SCREEN_HEIGHT);
        }
    }
}
