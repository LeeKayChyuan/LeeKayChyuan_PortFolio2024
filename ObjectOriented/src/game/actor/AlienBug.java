package game.actor;

import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.GameMap;
import game.Ability;
import game.behavior.FollowBehavior;
import game.behavior.PickUpBehavior;
import game.behavior.WanderBehaviour;

/**
 * Class representing the Alien Bug hostile actor in the game world.
 * The alien bug class extends from the hostile actor abstract class.
 * @Author Andrew Chong Han Wen
 */
public class AlienBug extends HostileActor{
    /**
     * Constructor for creating a new HostileActor.
     *
     */
    Actor target;
    public AlienBug(int id, Actor target) {
        super("Feature-" + id, 'a', 2);
        super.removeCapability(Ability.CANT_OVER_FLOOR);
        this.target = target;
        this.behaviours.put(999, new WanderBehaviour());
        this.behaviours.put(1, new PickUpBehavior());
    }

    @Override
    public ActionList allowableActions(Actor otherActor, String direction, GameMap map) {
        if (otherActor == target)
            this.behaviours.put(2, new FollowBehavior(target));
        return  super.allowableActions(otherActor, direction, map);
    }
}


