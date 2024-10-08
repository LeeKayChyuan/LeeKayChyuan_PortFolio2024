package game.ground;

import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.Ground;
import game.Ability;

/**
 * A class that represents the floor inside a building.
 * Created by: Chen Ching Tung
 * @author Riordan D. Alfredo
 * Modified by: Chen Ching Tung
 *
 */
public class Floor extends Ground {
    public Floor() {
        super('_');
    }

    @Override
    public boolean canActorEnter(Actor actor) {
        if (actor.hasCapability(Ability.CANT_OVER_FLOOR))
            return false;
        return super.canActorEnter(actor);
    }
}
