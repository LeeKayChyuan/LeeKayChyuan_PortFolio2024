package game.item.purchaseItem;

import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.items.Item;
import edu.monash.fit2099.engine.positions.Location;
import game.action.MoveToAction;

import java.util.Random;

/**
 * Representing an item type in the game environment, a Theseus.
 *
 * Theseus is an item that can be purchased by an actor and used within the game.
 * It implements the PurchaseItemSpecial and Consumable interfaces.
 *
 * After the player places Theseus on the ground,
 * the player can use THESEUS to teleport randomly.
 *
 * @author Chen Ching Tung
 * @version 1.0.0
 * @since 2024-05-31
 */
public class Theseus extends Item implements PurchaseItemSpecial {
    private final int price = 100;

    /**
     * Constructor for Theseus.
     */
    public Theseus() {
        super("THESEUS ", '^', true);
    }

    /**
     * Returns a list of actions that can be performed on the Theseus item at the given location.
     * This includes the option to move to a random location on the current map.
     *
     * @param location The location of the Theseus item.
     * @return An ActionList of allowable actions.
     */
    @Override
    public ActionList allowableActions(Location location) {
        int width = location.map().getXRange().max();
        int height = location.map().getYRange().max();
        Location teleportLocation;
        do {
            Random random = new Random();
            teleportLocation = location.map().at(random.nextInt(width), random.nextInt(height));
        } while (teleportLocation.getActor() != null);

        ActionList actions = super.allowableActions(location);
        actions.add(new ActionList(new MoveToAction(teleportLocation, "current map!")));

        return actions;
    }

    /**
     * Special action for purchasing the Theseus item.
     * If the actor has enough balance, the item is added to the actor's inventory.
     *
     * @param actor The actor attempting to purchase the Theseus item.
     * @return A string indicating the result of the purchase.
     */
    @Override
    public String special(Actor actor) {
        if (actor.getBalance() >= this.price) {
            actor.deductBalance(this.price);
            actor.addItemToInventory(this);
            return "Purchase successful!!\nYou spent " + this.price + " credits and you get a " + this;
        }
        return "Sorry, Purchase fail.\nYou need to have " + this.price + " credits.";
    }

    /**
     * Returns the price of the Theseus item.
     *
     * @return The price of the Theseus item.
     */
    @Override
    public int getprice() {
        return this.price;
    }

}
