package game.behavior;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.actors.Behaviour;
import edu.monash.fit2099.engine.items.Item;
import edu.monash.fit2099.engine.items.PickUpAction;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.positions.Location;

import java.util.List;
import java.util.Random;

/**
 * Class for PickUp behaviour, allows the actor to pick up items in the game world\
 * @Author Andrew Chong Han Wen
 */
public class PickUpBehavior implements Behaviour {

    /**
     * getAction method checks if there is an item on the current location of the actor, if there is, a PickUpAction is
     * added to the available actions that can be done by the actor.
     * @param actor the Actor acting
     * @param map the GameMap containing the Actor
     * @return PickUpAction if actor in on an item, or null if no items detected.
     */
    @Override
    public Action getAction(Actor actor, GameMap map) {
        Location myLocation = map.locationOf(actor);
        Random random = new Random();
        List<Item> items = myLocation.getItems();
        if (items.size() != 0){
            int index = random.nextInt(items.size());
            return new PickUpAction(items.get(index));
        }
        return null;
    }
}
