package game.ground;

import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.Ground;

/**
 * Created by: Chen Ching Tung
 * @author Riordan D. Alfredo
 * Modified by: Chen Ching Tung
 *
 */
public class Wall extends Ground {

    public Wall() {
        super('#');
    }

    @Override
    public boolean canActorEnter(Actor actor) {
        return false;
    }
}
