package game.item.purchaseItem;

import edu.monash.fit2099.engine.actors.Actor;

/**
 * An interface representing special behavior for items that can be purchased.
 *
 * Implementing classes should define the special behavior that occurs when the item is purchased,
 * as well as provide the price of the item.
 *
 * This interface is intended to be implemented by classes representing items that can be purchased in the game.
 *
 * @author Chen Ching Tung
 * @version 1.0.0
 * @since 24/04/2024
 */
public interface PurchaseItemSpecial{
    /**
     * Defines the special behavior that occurs when the item is purchased by the specified actor.
     *
     * @param actor the actor purchasing the item
     * @return a string representing the special behavior of the item when purchased
     */
    String special( Actor actor);

    /**
     * Retrieves the price of the item.
     *
     * @return the price of the item
     */
    int getprice();

}
