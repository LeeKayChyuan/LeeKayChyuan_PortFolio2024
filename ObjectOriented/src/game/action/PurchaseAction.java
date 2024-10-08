package game.action;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.GameMap;
import game.item.purchaseItem.PurchaseItemSpecial;

/**
 * Represents an action where an actor purchases an item from a computer terminal.
 *
 * This action allows the actor to purchase a specified item from the computer terminal.
 * Upon execution, the item is added to the actor's inventory, and the actor's balance
 * is deducted by the specified amount.
 *
 * This action is typically used when interacting with a computer terminal or a shop
 * in the game environment.
 *
 * @author Toby Marsden
 * @version 1.0.0
 * @since 28/04/2024
 */
public class PurchaseAction extends Action {

    /**
     * The item to be purchased from the computer terminal.
     */
    PurchaseItemSpecial item;


    /**
     * Constructor.
     *
     * @param item The item to be purchased from the computer terminal.
     */
    public PurchaseAction(PurchaseItemSpecial item){
        this.item = item;
    }

    /**
     * Executes the purchase action.
     * Adds the item to the actor's inventory and charges the actor the specified amount.
     *
     * @param actor The actor performing the action.
     * @param map The map the actor is on.
     * @return A description of the result of the purchase action.
     */
    @Override
    public String execute(Actor actor, GameMap map) {
        return this.item.special(actor);
    }


    /**
     * Provides a description of the purchase action for display in the menu.
     *
     * @param actor The actor performing the action.
     * @return A description of the purchase action.
     */

    @Override
    public String menuDescription(Actor actor) {
        return String.format("Purchase a %s by %d credits", item, item.getprice());
    }
}
