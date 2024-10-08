package game.actor;

import edu.monash.fit2099.engine.weapons.IntrinsicWeapon;
import game.behavior.AttackBehavior;
import game.behavior.WanderBehaviour;

/**
 * Class representing a hostile Suspicious Astronaut actor in the game world.
 * Suspicious Astronaut extends the HostileActor class and represents a hostile astronaut that wander around the map.
 * Suspicious is stronk that instant kill a Player.
 * Extends the {@link HostileActor} class.
 *
 * @author Chen Ching Tung & Lee Kay Chyuan
 * @version 1.0.0
 * @since 2024-04-19
 */
public class SuspiciousAstronaut extends HostileActor {

    /**
     * Constructor for creating a Suspicious Astronaut instance.
     * Sets its name, display character, and initial hit points.
     * Initializes its behavior to wander and instant kill a player when it is in ite range.
     */
    public SuspiciousAstronaut() {
        super("Suspicious Astronaut", 'ඞ', 99);
        this.weapon = new IntrinsicWeapon(Integer.MAX_VALUE, "bonk", 100);
        this.behaviours.put(999, new WanderBehaviour());
        this.behaviours.put(998, new AttackBehavior(weapon));
    }

}
