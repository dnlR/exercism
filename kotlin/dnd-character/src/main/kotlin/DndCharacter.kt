import kotlin.math.floor
import kotlin.random.Random

class DndCharacter {

    val strength: Int = diceRoll()
    val dexterity: Int = diceRoll()
    val constitution: Int = diceRoll()
    val intelligence: Int = diceRoll()
    val wisdom: Int = diceRoll()
    val charisma: Int = diceRoll()
    val hitpoints: Int = diceRoll()

    public fun diceRoll(): Int {
        var diceThrows = List(4) { Random.nextInt(1, 7) }
        return diceThrows.sorted().drop(1).sum()
    }

    fun calculateHitpoints() {

    }

    companion object {

        fun ability(): Int {
            TODO("Implement the function to complete the task")
        }

        fun modifier(score: Int): Int {
            return floor().toInt()
        }
    }

}
