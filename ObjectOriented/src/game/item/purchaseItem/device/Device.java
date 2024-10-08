package game.item.purchaseItem.device;

import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.items.Item;
import edu.monash.fit2099.engine.positions.Location;
import game.item.purchaseItem.PurchaseItemSpecial;

/**
 * Represent a device that actor can buy and interact with.
 * It is a special item that extend Item and implement PurchaseItemSpecial
 *
 * @author Lee Kay Chyuan
 * @version 1.0.0
 * @since 29/05/2024
 */
public abstract class Device extends Item implements PurchaseItemSpecial {

    /**
     * The selling price of the Device.
     */
    int price;

    /**
     * The lifetime of the device when it is inside inventory.
     */
    int lifeTime = 0;

    /***
     * Constructor for Device.
     */
    public Device(String name, char displayChar, boolean portable, int price ) {
        super(name, displayChar, portable);
        this.price = price;
    }


    /**
     * Retrieves the allowable actions of Device when it is in other actor's inventory.
     * @param otherActor the actor that owns the item
     * @return a list of allowable actions.
     */
    @Override
    public ActionList allowableActions(Actor otherActor) {
        return super.allowableActions(otherActor);
    }

    /**
     * Defines the special behaviour of the Device when purchased by actor.
     *
     * @param actor the actor purchasing the item
     * @return A string that described the special behaviour.
     */
    @Override
    public String special(Actor actor) {
        int price = this.price;
        if (actor.getBalance() >= price){
            actor.deductBalance(price);
            actor.addItemToInventory(this);
            return "Purchase successful!!\nYou spent " + price + " credits and you get a " + this;
        }
        return "Sorry, Purchase fail.\nYou need to have " + price + " credits.";
    }

    /**
     * Retrieve the price of this Device.
     *
     * @return the price of the Device.
     */
    @Override
    public int getprice() {
        return this.price;
    }

    /**
     * Add the lifetime of the Device by 1.
     */
    public void addLifeTime (){
        this.lifeTime ++;
    }

    /**
     * Retrieve the lifetime of the Device.
     * @return Lifetime of the Device.
     */
    public int getLifeTime (){
        return lifeTime;
    }

}
