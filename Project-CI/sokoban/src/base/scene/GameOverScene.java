package base.scene;

import base.CoverGameOverScene;
import base.GameObject;

public class GameOverScene extends Scene {
    @Override
    public void init() {
        GameObject cover = GameObject.recycle(CoverGameOverScene.class);
    }

    @Override
    public void clear() {
        GameObject.clearAll();
    }
}
