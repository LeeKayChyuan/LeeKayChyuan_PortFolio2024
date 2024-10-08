package game.ground;

import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.Ground;
import edu.monash.fit2099.engine.positions.Location;
import game.action.MoveToAction;
import game.action.PurchaseAction;
import game.item.purchaseItem.DragonSlayerSword;
import game.item.purchaseItem.EnergyDrink;
import game.item.purchaseItem.Theseus;
import game.item.purchaseItem.ToiletPaperRoll;
import game.item.purchaseItem.device.SubscribedAstley;

import java.util.ArrayList;

/**
 * Represents a ground type in the game environment, a computer terminal.
 *
 * This ground type allows actors to interact with it by performing various actions,
 * such as purchasing items from the computer terminal.
 *
 * When an actor interacts with the computer terminal, it provides a list of allowable actions
 * related to purchasing items.
 *
 * The computer terminal offers the ability to purchase items such as the Dragon Slayer Sword,
 * Energy Drink, and Toilet Paper Roll.
 *
 * @author Toby Marsden
 * @version 1.0.0
 * @since 24/04/2024
 */
public class ComputerTerminal extends Ground {
    ArrayList<MoveToAction> moveActions;

    /**
     * Constructor.
     *
     */
    public ComputerTerminal(ArrayList<MoveToAction> moveActions) {
        super('=');
        this.moveActions = moveActions;
    }


    /**
     * Returns a list of actions that the Actor can do to the ComputerTerminal
     * @param actor the Actor acting
     * @param location the current Location
     * @param direction the direction of the Ground from the Actor
     * @return The list of allowable actions
     */
    @Override
    public ActionList allowableActions(Actor actor, Location location, String direction) {
        ActionList actions = super.allowableActions(actor, location, direction);
        actions.add(new PurchaseAction(new DragonSlayerSword()));
        actions.add(new PurchaseAction(new EnergyDrink()));
        actions.add(new PurchaseAction(new ToiletPaperRoll()));
        actions.add(new PurchaseAction(new Theseus()));
        actions.add(new PurchaseAction(new SubscribedAstley()));
        for(MoveToAction action: this.moveActions){
            if(action.map() == location.map())
                continue;
            actions.add(action);
        }

        return actions;
    }
}