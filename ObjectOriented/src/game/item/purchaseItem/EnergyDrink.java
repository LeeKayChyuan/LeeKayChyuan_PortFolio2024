package game.item.purchaseItem;

import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.items.Item;
import game.action.ConsumeAction;
import game.actor.HostileActor;
import game.item.Consumable;
import game.item.Sellable;

import java.util.Random;
/**
 * Represents a special item, Energy Drink, which extends the Item class and implements
 * the PurchaseItemSpecial and Consumable interfaces.
 *
 * The Energy Drink can be consumed by actors to restore hit points. It can also be purchased
 * by the player, with a chance of being charged double the price.
 *
 * This class provides methods to handle the special behavior of the Energy Drink when purchased
 * and consumed.
 *
 * Additionally, it allows actors to consume the Energy Drink to heal a specified amount of hit points.
 *
 * @author Toby Marsden
 * @version 1.0.0
 * @since 26/04/2024
 */
public class EnergyDrink extends Item implements PurchaseItemSpecial, Consumable {
    /**
     * The price of the item.
     */
    int price;

    /**
     * The amount of hit points the EnergyDrink heals.
     */
    private final int heal = 1;
    /**
     * Constructor.
     *
     */
    public EnergyDrink() {
        super("Energy Drink", '*', true);
        this.price = 10;
    }

    /**
     * Returns a list of actions that the Actor can do to the EnergyDrink
     * @param otherActor the Actor acting
     * @return The list of allowable actions
     */
    @Override
    public ActionList allowableActions(Actor otherActor) {
        ActionList actions = super.allowableActions(otherActor);
        actions.add(new ActionList(new ConsumeAction( this)));
        return actions;
    }

    /**
     * Special method for the EnergyDrink. Describes the process of the player being
     * charged double the cost of the item
     * @param actor The actor purchasing the EnergyDrink.
     * @return A string describing the result of the purchase.
     */
    @Override
    public String special(Actor actor) {
        Random random = new Random();
        int is_double = 1;
        if (random.nextInt(5) <1)
            is_double +=1;
        if (actor.getBalance() >= this.price * is_double){
            actor.deductBalance(this.price * is_double);
            actor.addItemToInventory(this);
            return "Purchase successful!!\nYou spent " + this.price * is_double + " credits and you get a " + this;
        }
        return "Sorry, Purchase fail.\nYou need to have " + this.price * is_double + " credits.";
    }

    /**
     * Returns the price of the EnergyDrink.
     * @return The price of the EnergyDrink.
     */
    @Override
    public int getprice() {
        return this.price;
    }

    /**
     * Method to consume the item
     * @param actor the actor that is consuming the item
     * @return a string describing the action
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
