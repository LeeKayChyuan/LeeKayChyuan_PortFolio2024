package game.item;

import edu.monash.fit2099.engine.actors.Actor;
/**
 * Represents an interface for consumable items in the game.
 *
 * Implementing classes should define methods to consume the item and provide a menu description.
 *
 * This interface allows actors to consume items and provides a menu description for the consumable.
 *
 * @author Chen Ching Tung & Toby Marsden
 * @version 2.0.0
 * @since 24/04/2024
 */


public interface Consumable {
    /**
     * Consumes the item and returns a string describing the effect of consuming the item.
     *
     * @param actor The actor that is consuming the item.
     * @return A string describing the effect of consuming the item.
     */
    String consume(Actor actor);

    /**
     * Returns the menu description for the consumable.
     *
     * @return The price of the item.
     */
    String menuDescription(Actor actor);
}
