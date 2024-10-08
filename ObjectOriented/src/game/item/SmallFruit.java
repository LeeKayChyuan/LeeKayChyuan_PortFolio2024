package game.item;

import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.items.Item;
import game.action.ConsumeAction;
import game.actor.HostileActor;

/**
 * A class representing a small fruit as an item in the game world.
 * Small fruits are consumable items that can be eaten by actors to restore health.
 * Extends the {@link Item} class.
 * Implements functionality for allowing actors to eat the fruit.
 *
 * @author Chen Ching Tung
 * @version 1.0.0
 * @since 2024-04-19
 */
public class SmallFruit extends Item implements Consumable {
    private final int heal = 1;

    /**
     * Constructor for SmallFruit class.
     * Creates a small fruit with a name, display character, and portability status.
     */
    public SmallFruit() {
        super("Small Fruit", 'o', true);
    }

    /**
     * Generates a list of allowable actions for the small fruit.
     * Adds an eat fruit action to the list of actions for the other actor.
     *
     * @param otherActor The actor interacting with the small fruit.
     * @return An action list containing an eat fruit action.
     */
    @Override
    public ActionList allowableActions(Actor otherActor) {
        ActionList actions = super.allowableActions(otherActor);
        actions.add(new ActionList(new ConsumeAction(this)));
        return actions;
    }

    /**
     *
     * This method will implement the fetching of the sale price of the item
     *
     * @return the sale price of the item
     */
    @Override
    public String consume(Actor actor) {
        actor.removeItemFromInventory(this);
        actor.heal(this.heal);
        return String.format("The %s heals the %s by %d hit points", this, actor, this.heal);
    }

    @Override
    public String menuDescription(Actor actor) {
        return  " heal " + this.heal + " hit points";
    }
}
