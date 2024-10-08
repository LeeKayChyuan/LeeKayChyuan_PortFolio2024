package game.action;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.items.Item;
import edu.monash.fit2099.engine.positions.GameMap;
import game.actor.HostileActor;
import game.item.Sellable;


/**
 * A new action that returns the sell method of each sellable item within the game
 * that sell method holds the implementation for the sale process
 *
 * Extends the {@link Action} class.
 *
 * @author Toby Marsden
 * @version 1.0.0
 * @since 2024-05-18
 */
public class SellAction extends Action {

    /**
     * the item being sold
     */
    private Sellable item;

    /**
     * default constuctor for the sell action
     * @param item the item being sold
     */
    public SellAction(Sellable item){
        this.item = item;
    }


    /**
     * executes teh sell method in the item's class thus facilitating the sale
     * of that item
     *
     * @param actor The actor performing the action.
     * @param map The map the actor is on.
     * @return the outcome of the sell method
     */
    @Override
    public String execute(Actor actor, GameMap map) {
        return this.item.sell(actor, map);
    }

    /**
     * displays the sell action to the main menu for the player to select
     * @param actor The actor performing the action.
     * @return
     */
    @Override
    public String menuDescription(Actor actor) {
        return actor + " sell " + this.item + " to Humanoid Figure for " + item.getSalePrice() + " credits";
    }

}
