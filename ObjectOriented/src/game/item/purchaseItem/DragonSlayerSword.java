package game.item.purchaseItem;

import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.Exit;
import edu.monash.fit2099.engine.positions.Location;
import edu.monash.fit2099.engine.weapons.WeaponItem;
import game.Status;
import game.action.AttackAction;


import java.util.Random;

/**
 * Represents a special weapon item, the Dragon Slayer Sword, which extends the WeaponItem class and implements
 * the PurchaseItemSpecial interface.
 *
 * The Dragon Slayer Sword has a special ability that allows the player to attack hostile actors nearby.
 * It can also be purchased by the player, with a chance of success determined by a random roll.
 *
 * This class provides methods to handle the special behavior of the Dragon Slayer Sword when purchased,
 * as well as its allowable actions when wielded by the player.
 *
 * @author Chen Ching Tung & Toby Marsden
 * @version 2.0.0
 * @since 26/04/2024
 */
public class DragonSlayerSword extends WeaponItem implements PurchaseItemSpecial{

    /**
     * The current location of the Dragon Slayer Sword.
     */
    Location currentLocation;

    /**
     * The price of the Dragon Slayer Sword.
     */
    int price;

    /**
     * Constructor for DragonSlayerSword.
     */
    public DragonSlayerSword() {
        super("Dragon Slayer Sword", 'x', 50 , "hits", 75);
        this.price = 100;
    }

    /**
     * Sets the current location of the Dragon Slayer Sword.
     *
     * @param currentLocation the current location of the Dragon Slayer Sword
     * @param actor           the actor carrying the Dragon Slayer Sword
     */
    public void tick(Location currentLocation, Actor actor) {
        super.tick(currentLocation, actor);
        this.currentLocation = currentLocation;

    }

    /**
     * Retrieves the allowable actions for the Dragon Slayer Sword when wielded by the player.
     *
     * @param otherActor the actor targeted by the Dragon Slayer Sword
     * @param location   the location where the action is performed
     * @return a list of allowable actions for the Dragon Slayer Sword
     */
    public ActionList allowableActions(Actor otherActor, Location location) {
        ActionList actions = new ActionList();
        if (otherActor.hasCapability(Status.HOSTILE_TO_PLAYER)) {
            for (Exit exit : this.currentLocation.getExits()) {
                Location destination = exit.getDestination();
                Actor actor = destination.getActor();
                if (actor == otherActor)
                    actions.add(new AttackAction(actor, exit.getName(), this));
            }
        }
        return actions;
    }

    /**
     * Defines the special behavior of the Dragon Slayer Sword when purchased by the specified actor.
     *
     * @param actor the actor purchasing the Dragon Slayer Sword
     * @return a string representing the outcome of the purchase
     */
    @Override
    public String special( Actor actor) {
        Random random = new Random();
        if (actor.getBalance() < this.price)
            return "Sorry, Purchase fail.\nYou need to have " + this.price + " credits.";
        actor.deductBalance(this.price);
        if(random.nextInt(100) < 50){
            actor.addItemToInventory(this);
            return "Purchase successful!!\nYou get a " + this;
        }
        return "Sorry, computer got an error.\nYou lose 100 credits";
    }
    /**
     * Retrieves the price of the Dragon Slayer Sword.
     *
     * @return the price of the Dragon Slayer Sword
     */
    @Override
    public int getprice() {
        return this.price;
    }
}
