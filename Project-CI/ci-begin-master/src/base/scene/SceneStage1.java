package base.scene;

import base.Background;
import base.GameObject;
import base.enemy.EnemySummoner;
import base.player.Player;

public class SceneStage1 extends Scene {

    public static GameObject background;
    public static GameObject player;
    public EnemySummoner enemySummoner;

    @Override
    public void init() {
        this.background = GameObject.recycle(Background.class); //khởi tạo
        this.player = GameObject.recycle(Player.class); //new Player
//        Enemy enemy = GameObject.recycle(Enemy.class); //new Enemy
        this.enemySummoner = GameObject.recycle(EnemySummoner.class);
    }

    @Override
    public void clear() {
        GameObject.clearAll();
    }
}
