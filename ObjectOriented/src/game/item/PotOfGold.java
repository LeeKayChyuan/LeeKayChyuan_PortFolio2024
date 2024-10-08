package game.item;

import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.items.Item;
import edu.monash.fit2099.engine.positions.GameMap;
import game.action.ConsumeAction;

import java.util.Random;

/**
 * A class that represents a Pot of Gold as an Item in the game world.
 * Pot of Gold can be picked up and take out the gold by the actor
 * Extends the {@link Item} class.
 * Implements the {@link Consumable} class.
 *
 * @author Chen Ching Tung
 * @version 1.0.0
 * @since 2024-05-05
 */
public class PotOfGold extends SellableItem implements Consumable, Sellable {

    private final int balance = 10;


    /***
     * Constructor of PotOfGold class.
     * Create PotOfGold with name, display character and portability status.
     */
    public PotOfGold() {
        super("a Pot of Gold", '$', true, 500);
    }

    /**
     * Generates a list of allowable actions of the Pot of Gold.
     * Adds a consume action to the list of actions for the other actor.
     * @param owner The actor interacting with the Pot of Gold.
     * @return An action list containing the action that can be performed by other actor.
     */
    @Override
    public ActionList allowableActions(Actor owner) {
        ActionList actions = super.allowableActions(owner);
        actions.add(new ActionList(new ConsumeAction( this)));
        return actions;
    }

    /**
     * Execute the take-out the gold of a Pot of Gold by the actor interacting with it.
     * Remove this item from the actor's inventory.
     * Add 10 credits to the actor wallet's
     * @param actor the actor that are interacting with this Pot of Gold.
     * @return A string that shows the gold is added to the wallet.
     */
    @Override
    public String consume(Actor actor) {
        actor.addBalance(this.balance);
        actor.removeItemFromInventory(this);
        return "increasing " + actor + " wallet amount by " + this.balance + " credits.";
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
    public String sell(Actor actor ,GameMap map){
        Random random = new Random();

        if (random.nextInt(100) > 25) {
            actor.removeItemFromInventory(this);
            actor.addBalance(this.getSalePrice());
            return actor + " sold the " + this + " for " + this.getSalePrice() + " credits";
        }
        else {
            int discountPrice = 0;
            actor.removeItemFromInventory(this);
            actor.addBalance(discountPrice);
            System.out.println("The factory believes the gold is fake and will not pay for it.");
            return actor + " sold the " + this + " for " + discountPrice + " credits";
        }
    }

    /**
     * Provides a description of the take-out the gold of a Pot of Gold for display in the menu.
     *
     * @param actor The actor interacting with this Pot of Gold.
     * @return A description of the eat a Pot of Gold.
     */
    @Override
    public String menuDescription(Actor actor) {
        return " get " + this.balance + " balances";
    }
}
