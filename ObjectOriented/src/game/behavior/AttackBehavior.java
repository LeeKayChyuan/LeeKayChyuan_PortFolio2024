package game.behavior;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.actors.Behaviour;
import edu.monash.fit2099.engine.positions.Exit;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.positions.Location;
import edu.monash.fit2099.engine.weapons.Weapon;
import game.Status;
import game.action.AttackAction;

import java.util.Random;

/**
 * Represents a behavior where an actor attacks another actor using a specified weapon.
 * This behavior is typically used by hostile actors to attack enemy actors within their vicinity.
 *
 * Implements the {@link edu.monash.fit2099.engine.actors.Behaviour} interface.
 *
 * @author Chen Ching Tung
 * @modifiedby Chen Ching Tung and Andrew Chong Han Wen
 * @version 1.0.0
 * @since 2024-04-19
 */
public class AttackBehavior implements Behaviour {

    private final Weapon weapon;  // The weapon used for the attack

    /**
     * Constructor for creating an AttackBehavior.
     *
     * @param weapon     the weapon used for the attack
     */
    public AttackBehavior(Weapon weapon) {
        this.weapon = weapon;
    }

    public Action detectNearActors(Actor mine,GameMap map){
        Actor actors[] = new Actor[8];
        int index = 0;
        Location myLocation = map.locationOf(mine);
        for (Exit exit: myLocation.getExits()){
            Location location = exit.getDestination();
            Actor actor = location.getActor();
            if (actor == null)
                continue;
            if ( actor.hasCapability(Status.HOSTILE_TO_ENEMY)){
                actors[index] = actor;
                index += 1;
            }
        }
        if (index != 0){
            Random random = new Random();
            return new AttackAction( actors[random.nextInt(index)],"", weapon);
        }
        return null;
    }

    /**
     * Returns an AttackAction to attack the specified actor using the specified weapon.
     *
     * @param actor the actor performing the behavior
     * @param map   the game map in which the actor is located
     * @return an AttackAction to attack the specified actor
     */
    @Override
    public Action getAction(Actor actor, GameMap map) {

        // Return an AttackAction to attack the specified actor with the specified weapon
        return detectNearActors(actor, map);
    }

}


