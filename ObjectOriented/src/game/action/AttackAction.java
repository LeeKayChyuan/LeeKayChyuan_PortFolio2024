package game.action;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.items.Item;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.positions.Location;
import edu.monash.fit2099.engine.weapons.Weapon;

import java.util.Random;

/**
 * A class representing an attack action in the game world.
 * AttackAction allows an actor to perform an attack on another actor using a weapon.
 * Extends the {@link edu.monash.fit2099.engine.actions.Action} class.
 *
 * The attack action calculates the chance to hit and damage based on the actor's weapon,
 * and applies the damage to the target actor if the attack is successful.
 *
 * @author Chen Ching Tung
 * @version 1.0.0
 * @since 2024-04-19
 */
public class AttackAction extends Action {

    /**
     * The Actor that is to be attacked
     */
    private Actor target;

    /**
     * The direction of incoming attack.
     */
    private String direction;

    /**
     * Random number generator
     */
    private Random rand = new Random();

    /**
     * Weapon used for the attack
     */
    private Weapon weapon;

    /**
     * Constructor.
     *
     * @param target the Actor to attack
     * @param direction the direction where the attack should be performed (only used for display purposes)
     * @param weapon the weapon used for the attack
     */
    public AttackAction(Actor target, String direction, Weapon weapon) {
        this.target = target;
        this.direction = direction;
        this.weapon = weapon;
    }

    /**
     * Constructor with intrinsic weapon as default
     *
     * @param target the actor to attack
     * @param direction the direction where the attack should be performed (only used for display purposes)
     */
    public AttackAction(Actor target, String direction) {
        this.target = target;
        this.direction = direction;
    }

    /**
     * Executes the attack action.
     * Calculates the chance to hit and damage, applies damage to the target actor if the attack is successful,
     * and returns a description of the result.
     *
     * @param actor The actor performing the action.
     * @param map The map the actor is on.
     * @return A description of the result of the attack action.
     */
    @Override
    public String execute(Actor actor, GameMap map) {
        if (weapon == null) {
            weapon = actor.getIntrinsicWeapon();
        }

        if (!(rand.nextInt(100) <= weapon.chanceToHit())) {
            return actor + " misses " + target + ".";
        }


        int damage = weapon.damage();
        String result = actor + " " + weapon.verb() + " " + target + " for " + damage + " damage.";
        target.hurt(damage);
        if (!target.isConscious()) {
            Location location = map.locationOf(target);
            for(Item item : target.getItemInventory())
                location.addItem(item);
            result += "\n" + target.unconscious(actor, map);
        }

        return result;
    }

    /**
     * Provides a description of the attack action for display in the menu.
     *
     * @param actor The actor performing the action.
     * @return A description of the attack action.
     */
    @Override
    public String menuDescription(Actor actor) {
        return actor + " attacks " + target + " at " + direction + " with " + (weapon != null ? weapon : "Intrinsic Weapon");
    }
}