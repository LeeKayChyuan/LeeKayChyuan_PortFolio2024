package game.item.purchaseItem;

import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.items.Item;
import edu.monash.fit2099.engine.positions.GameMap;
import game.actor.HostileActor;
import game.item.Sellable;
import game.item.SellableItem;

import java.util.Random;
/**
 * Represents a special item, Toilet Paper Roll, which extends the Item class and implements
 * the PurchaseItemSpecial interface.
 *
 * The Toilet Paper Roll has a special ability that reduces its price when purchased.
 * It can be purchased by the player, and the price is randomly set to either 1 or 5 credits.
 *
 * This class provides methods to handle the special behavior of the Toilet Paper Roll when purchased.
 *
 * @author Toby Marsden
 * @version 1.0.0
 * @since 26/04/2024
 */
public class ToiletPaperRoll extends SellableItem implements PurchaseItemSpecial, Sellable {
    /**
     * The price of the item.
     */
    int price = 5;

    /**
     * Constructor.
     */
    public ToiletPaperRoll() {
        super("Toilet Paper Roll", 's', true, 1);
    }

    /**
     * Special method for the ToiletPaperRoll. Describes the process of the player being
     * charged 1 credit for the item instead of 5
     * @param actor The actor purchasing the ToiletPaperRoll.
     * @return A string describing the result of the purchase.
     */
    @Override
    public String special(Actor actor) {
        Random random = new Random();
        int price = this.price;
        if(random.nextInt(4) >0)
            price = 1;
        if (actor.getBalance() >= price){
            actor.deductBalance(price);
            actor.addItemToInventory(this);
            return "Purchase successful!!\nYou spent " + price + " credits and you get a " + this;
        }
        return "Sorry, Purchase fail.\nYou need to have " + price + " credits.";
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
    public String sell(Actor actor, GameMap map) {
        Random random = new Random();

        if (random.nextInt(100) > 50) {
            actor.removeItemFromInventory(this);
            actor.addBalance(this.getSalePrice());
            return actor + " sold the " + this + " for " + this.getSalePrice() + " credits";
        }
        else {

            System.out.println("The factory does not want your toilet paper and decides to kill you.\n");
            actor.unconscious(map);
            return actor + " died at the hands of the Humanoid Figure";
        }
    }


    /**
     * Returns the price of the item.
     *
     * @return The price of the item.
     */
    @Override
    public int getprice() {
        return this.price;
    }
}
