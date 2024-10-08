package game.ground.inheritree;

/**
 * Sprout class is a phase of tree that does not produce any fruits
 *
 * @author Andrew Chong Han Wen
 */
public class Sprout extends NoFruitTree{

    /**
     * Constructor method for sprout class, sets the age threshold and the next tree phase
     */
    public Sprout() {
        super(',');
        super.age_threshold = 3;
        super.setTree = new Sapling();
    }
}

