package game.action;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.items.Item;
import edu.monash.fit2099.engine.positions.GameMap;

/**
 * A class representing a speak action of others in the world.
 * SpeakAction allows an item to perform speaking.
 * Extends the {@link edu.monash.fit2099.engine.actions.Action} class.
 *
 *
 * @author Lee Kay Chyuan
 * @version 1.0.0
 * @since 29/05/2024
 */
public class SpeakAction extends Action {

    /**
     * The word to speak.
     */
    String word;

    /**
     * The item to speak.
     */
    Item item;

    /**
     * Constructor of speak action.
     * @param word A string that the word the item wanted to speak
     * @param item The item that speak.
     */
    public SpeakAction(String word, Item item) {
        this.word = word;
        this.item = item;
    }

    /**
     * Execute the speak action.
     * Shows the item is speaking.
     *
     * @param actor The actor performing the action.
     * @param map The map the actor is on.
     * @return A string of word that the item speaks.
     */
    @Override
    public String execute(Actor actor, GameMap map) {
        return item + " : " + word;
    }

    /**
     * A menu description when interacting with the item
     * @param actor The actor performing the action.
     * @return A string of menu description to interact with the item.
     */
    @Override
    public String menuDescription(Actor actor) {
        return actor + " interact with the " + item;
    }
}
