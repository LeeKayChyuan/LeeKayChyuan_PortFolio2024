package game.item.purchaseItem.device;

import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.displays.Display;
import edu.monash.fit2099.engine.positions.Location;

/**
 * An unsubscribe version of AI device - Astley.
 *
 * @author Lee Kay Chyuan
 * @version 1.0.0
 * @since 29/05/2024
 */
public class UnsubscribeAstley extends Device {
    /***
     * Constructor of unsubscribe AI device - Astley.
     */
    public UnsubscribeAstley() {
        super("Astley, an AI device", 'z',true,50);
    }

    /**
     * Deduct 1 credit from balance if there is sufficient credit in actor's balance.
     * Check if the actor's balance have enough credit to pay, add new Subscribed Astley and deduct 1 credit if yes.
     *
     * @param currentLocation The location of the actor carrying this Item.
     * @param actor The actor carrying this Item.
     */
    @Override
    public void tick(Location currentLocation, Actor actor) {
        if (actor.getBalance() >= 1){
            actor.deductBalance(1);
            actor.addItemToInventory(new SubscribedAstley());
            actor.removeItemFromInventory(this);
            new Display().println("1 credit is deducted for " + this + " subscription fee");
        }
        else{
            new Display().println(this + " is unsubscribed please pay 1 credit");
        }
    }
}
