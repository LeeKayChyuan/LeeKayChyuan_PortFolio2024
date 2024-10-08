package game.actor;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actions.DoNothingAction;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.displays.Display;
import edu.monash.fit2099.engine.items.Item;
import edu.monash.fit2099.engine.positions.GameMap;
import game.Status;


/**
 * A class that implements the new Humanoid Figure actor which the player
 * can sell items to and make money within the game, the actor has the
 * capability buyer and will serve no purpose if the player is not
 * interacting with it
 *
 * Extends the {@link Actor} class.
 *
 * @author Toby Marsden
 * @version 1.0.0
 * @since 2024-05-18
 */
public class HumanoidFigure extends Actor {


    /**
     * default constuctor for the humanoid figure
     */
    public HumanoidFigure(){
        super("Humanoid Figure", 'H', 999);
        this.addCapability(Status.BUYER);
    }

    /**
     *
     * @param actions    collection of possible Actions for this Actor
     * @param lastAction The Action this Actor took last turn. Can do interesting things in conjunction with Action.getNextAction()
     * @param map        the map containing the Actor
     * @param display    the I/O object to which messages may be written
     * @return the do nothing action
     */
    @Override
    public Action playTurn(ActionList actions, Action lastAction, GameMap map, Display display) {
        return new DoNothingAction();
    }

}
