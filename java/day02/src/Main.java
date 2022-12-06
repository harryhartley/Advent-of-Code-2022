import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.Map;

class Main
{ 
    public static int silver(List<String> input) {
        int sum = 0;
        Map<String, Integer> rps = Map.of(
            "A X", 4, "A Y", 8, "A Z", 3,
            "B X", 1, "B Y", 5, "B Z", 9,
            "C X", 7, "C Y", 2, "C Z", 6
        );
        for (String line: input) {
            sum += rps.get(line);
        }
        return sum;
    }

    public static int gold(List<String> input) {
        int sum = 0;
        Map<String, Integer> rps = Map.of(
            "A X", 3, "A Y", 4, "A Z", 8,
            "B X", 1, "B Y", 5, "B Z", 9,
            "C X", 2, "C Y", 6, "C Z", 7
        );
        for (String line: input) {
            sum += rps.get(line);
        }
        return sum;
    }

    public static void main(String[] args) throws IOException {
        List<String> input = Files.readAllLines(Paths.get("../input.txt"));
        System.out.println("Silver: " + silver(input));
        System.out.println("Gold: " + gold(input));
    }
}