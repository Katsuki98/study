import base.game.GameCanvas;
import base.game.GameWindow;

public class Program {
    public static void main(String[] args) {
        GameWindow window = new GameWindow();
        GameCanvas canvas = new GameCanvas();
        window.add(canvas);
        window.pack();
        window.setVisible(true);
        canvas.gameLoop();
    }
}


//class: - Pascal-case (GameObject)
//variable: - Camel-case (gameObject)
//package: - Snake-case (game_object)