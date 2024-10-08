package game.item.purchaseItem.device;

import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.actors.attributes.BaseActorAttributes;
import edu.monash.fit2099.engine.displays.Display;
import edu.monash.fit2099.engine.positions.Location;
import game.Monologue;
import game.action.SpeakAction;

import java.util.ArrayList;
import java.util.Random;

/**
 * A subscribe version of AI device - Astley.
 *
 * @author Lee Kay Chyuan
 * @version 1.0.0
 * @since 29/05/2024
 */
public class SubscribedAstley extends Device {

    /**
     * An array list of monologues
     */
    ArrayList<String> monologues = new ArrayList<>();

    /***
     * Constructor of subscribed Astley.
     *
     * Lifetime is reset for every new subscribe.
     * Basic monologue is added to the arraylist monologues.
     */
    public SubscribedAstley() {
        super("Astley, an AI device", 'z',true,50);

        monologues.add(Monologue.Basic1);
        monologues.add(Monologue.Basic2);
        monologues.add(Monologue.Basic3);
    }

    /**
     * Deduct 1 credit from balance if there is sufficient credit in actor's balance.
     *
     * Check if the actor's balance have enough credit to pay, add new Subscribed Astley and deduct 1 credit if yes.
     * If the actor's balance does not have enough credit, a new unsubscribed Astley is added.
     *
     * @param currentLocation The location of the actor carrying this Item.
     * @param actor The actor carrying this Item.
     */
    @Override
    public void tick(Location currentLocation, Actor actor) {
        if (getLifeTime() == 5){
            if (actor.getBalance() >= 1){
                actor.deductBalance(1);
                new Display().println("1 credit is deducted for " + this + " subscription fee");

                actor.addItemToInventory(new SubscribedAstley());
            }
            else {
                actor.addItemToInventory(new UnsubscribeAstley());
                new Display().println(this + " is unsubscribed please pay 1 credit");
            }
            actor.removeItemFromInventory(this);
        }
    }

    /**
     * Retrieves the allowable actions of the Subscribed Device.
     * Specific actions will be retrieved when conditions are met.
     *
     * @param otherActor the actor that owns the item
     * @return the action that are allowed by the actor to perform with the device.
     */
    @Override
    public ActionList allowableActions(Actor otherActor) {
        addLifeTime();
        ActionList actions = new ActionList();
        Random random = new Random();
        if (otherActor.getBalance() > 50){
            monologues.add(Monologue.MoreThan50Credits);
        }
        if (otherActor.getItemInventory().size() > 10){
            monologues.add(Monologue.MoreThan10Item);
        }
        if (otherActor.getAttribute(BaseActorAttributes.HEALTH)<2){
            monologues.add(Monologue.HealthBelow2);
        }
        actions.add(new SpeakAction(monologues.get(random.nextInt(monologues.size())), this));

        return actions;
    }
}
