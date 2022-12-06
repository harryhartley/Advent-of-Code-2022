import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

class Main
{ 
    public static int silver(List<String> input) {
        int best = 0;
        int sum = 0;
        for (String cal: input) {
            if (cal.isEmpty()) {
                if (sum > best) {
                    best = sum;
                }
                sum = 0;
            }
            else {
                sum += Integer.parseInt(cal);
            }
        }
        return best;
    }

    public static int gold(List<String> input) {
        ArrayList<Integer> bestList = new ArrayList<Integer>();
        int sum = 0;
        for (String cal: input) {
            if (cal.isEmpty()) {
                if (bestList.size() < 3) {
                    bestList.add(sum);
                    bestList.sort(null);
                }
                else if (sum > bestList.get(0)) {
                    bestList.remove(0);
                    bestList.add(sum);
                    bestList.sort(null);
                }
                sum = 0;
            }
            else {
                sum += Integer.parseInt(cal);
            }
        }
        int best = 0;
        for (Integer x: bestList) {
            best += x;
        }
        return best;
    }

    public static void main(String[] args) throws IOException {
        List<String> input = Files.readAllLines(Paths.get("../input.txt"));
        System.out.println("Silver: " + silver(input));
        System.out.println("Gold: " + gold(input));
    }
}