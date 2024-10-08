package game.item;

import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.items.Item;
import edu.monash.fit2099.engine.positions.GameMap;
import game.action.ConsumeAction;
/**
 * A class representing a big fruit as an item in the game world.
 * Big fruits are consumable items that can be eaten by actors to restore health.
 * Extends the {@link Item} class.
 * Implements functionality for allowing actors to eat the fruit.
 *
 * @author Chen Ching Tung
 * @version 1.0.0
 * @since 2024-04-19
 */
public class BigFruit extends SellableItem implements Consumable, Sellable {
    private final int heal = 2;

    /**
     * Constructor for BigFruit class.
     * Creates a big fruit with a name, display character, and portability status.
     */
    public BigFruit() {
        super("Big Fruit", 'O', true, 30);
    }

    /**
     * Generates a list of allowable actions for the big fruit.
     * Adds an eat fruit action to the list of actions for the other actor.
     *
     * @param otherActor The actor interacting with the big fruit.
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
     * This method implements the consumption of edible items within the game
     *
     * @param actor the actor consuming the item
     * @return string confirming the consumption of the item
     */
    @Override
    public String consume(Actor actor) {
        actor.removeItemFromInventory(this);
        actor.heal(this.heal);
        return String.format("The %s heals the %s by %d hit points", this, actor, this.heal);
    }

    /**
     *
     * This method implements the sale of the item including any necessary special features
     *
     * @param actor the actor selling the item
     * @param map the map which the player is standing on
     * @return string confirming the sale of the item
     */
    @Override
    public String sell(Actor actor, GameMap map){
        actor.removeItemFromInventory(this);
        actor.addBalance(this.getSalePrice());
        return actor + " sold the " + this + " for " + this.getSalePrice() + " credits";
    }

    @Override
    public String menuDescription(Actor actor) {
        return  " heal " + this.heal + " hit points";
    }
}
