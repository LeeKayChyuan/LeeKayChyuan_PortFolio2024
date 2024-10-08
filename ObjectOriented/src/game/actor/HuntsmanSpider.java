package game.actor;

import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.weapons.IntrinsicWeapon;
import game.Ability;
import game.behavior.AttackBehavior;
import game.behavior.WanderBehaviour;


/**
 * Class representing a hostile huntsman spider actor in the game world.
 * HuntsmanSpider extends the HostileActor class and represents a spider enemy that wanders around the map.
 *
 * Extends the {@link Actor} class.
 *
 * @author Chen Ching Tung
 * @version 1.0.0
 * @since 2024-04-19
 */
public class HuntsmanSpider extends HostileActor {

    /**
     * Constructor for creating a HuntsmanSpider instance.
     * Sets its name, display character, and initial hit points.
     * Initializes its behavior to wander and its weapon to long legs with 1 base damage and 25 hitRate.
     */
    public HuntsmanSpider() {
        super("Huntsman Spider", '8', 1);
        this.behaviours.put(999, new WanderBehaviour());  // Add WanderBehaviour to the list of behaviors
        this.weapon = new IntrinsicWeapon(1, "long legs", 25);  // Initialize the weapon
        this.addCapability(Ability.CANT_OVER_FLOOR);
        this.behaviours.put(1, new AttackBehavior(weapon));
    }

}
