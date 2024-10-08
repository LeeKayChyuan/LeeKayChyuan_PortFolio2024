package game.action;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.GameMap;
import game.item.Consumable;

/**
 * A class representing an action to consume consumable item in the game world.
 * ConsumeAction allows an actor to consume a consumable item from their inventory to heal themselves or other consume methods.
 * Extends the {@link Action} class.
 *
 * When executed, the action removes the consumable item from the actor's inventory and run the consume method.
 *
 * @author Chen Ching Tung
 * @version 2.0.0
 * @since 2024-05-09
 */
public class ConsumeAction extends Action {


    /**
     * The consumable item to be consumed.
     */
    private final Consumable item;
    /**
     * Constructor for ConsumeAction.
     *
     * @param item the consumable item to be consumed
     */
    public ConsumeAction(Consumable item) {
        this.item = item;
    }

    /**
     * Executes the consume action by calling the consume method of the consumable item.
     *
     * @param actor the actor performing the action
     * @param map   the game map in which the actor is located
     * @return a string representing the result of consuming the item
     */
    @Override
    public String execute(Actor actor, GameMap map) {

        return this.item.consume(actor);
    }


    /**
     * Provides a description of the eat fruit action for display in the menu.
     *
     * @param actor The actor performing the action.
     * @return A description of the eat fruit action.
     */
    @Override
    public String menuDescription(Actor actor) {
        return actor + " consumes the " + this.item + " to" + this.item.menuDescription(actor);
    }
}
